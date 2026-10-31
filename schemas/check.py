"""Validate why-bureau example documents against their JSON Schemas.

Uses only the Python standard library. It implements the subset of JSON
Schema (draft 2020-12) that the schemas in this folder use.

Usage:
    python schemas/check.py                     check every example
    python schemas/check.py SCHEMA DOCUMENT     check one document

Example files are found in two places:
    schemas/examples/<schema>.valid-<n>.json    must pass
    schemas/examples/<schema>.invalid-<n>.json  must fail
    examples/**/<anything>.<schema>.json        must pass
where <schema> is the schema file name without ".schema.json".

Exit status is 0 when every document behaves as expected, 1 otherwise.
"""

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent

TYPES = {
    "object": lambda v: isinstance(v, dict),
    "array": lambda v: isinstance(v, list),
    "string": lambda v: isinstance(v, str),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "null": lambda v: v is None,
}

SUPPORTED = {
    "$schema", "$id", "$comment", "$defs", "$ref", "title", "description",
    "type", "enum", "const", "required", "properties", "additionalProperties",
    "items", "minItems", "minimum", "exclusiveMinimum", "minLength", "pattern",
    "allOf", "if", "then", "else",
}


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def resolve(ref, root, root_path):
    """Resolve '#/$defs/x' inside the current schema or 'file.json' beside it."""
    if ref.startswith("#/"):
        node = root
        for part in ref[2:].split("/"):
            node = node[part]
        return node, root, root_path
    target = root_path.parent / ref
    other = load(target)
    return other, other, target


def equal(a, b):
    # JSON equality: True must not equal 1.
    return a == b and isinstance(a, bool) == isinstance(b, bool)


def validate(value, schema, root, root_path, at="$"):
    errors = []
    unknown = set(schema) - SUPPORTED
    if unknown:
        raise ValueError(f"{root_path.name}: unsupported keywords {sorted(unknown)} at {at}")

    if "$ref" in schema:
        sub, sub_root, sub_path = resolve(schema["$ref"], root, root_path)
        errors += validate(value, sub, sub_root, sub_path, at)

    if "type" in schema:
        allowed = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(TYPES[t](value) for t in allowed):
            return errors + [f"{at}: expected type {'/'.join(allowed)}"]

    if "const" in schema and not equal(value, schema["const"]):
        errors.append(f"{at}: must equal {json.dumps(schema['const'])}")
    if "enum" in schema and not any(equal(value, e) for e in schema["enum"]):
        errors.append(f"{at}: must be one of {schema['enum']}")

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{at}: shorter than {schema['minLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{at}: does not match {schema['pattern']}")

    if TYPES["number"](value):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{at}: below minimum {schema['minimum']}")
        if "exclusiveMinimum" in schema and value <= schema["exclusiveMinimum"]:
            errors.append(f"{at}: must be greater than {schema['exclusiveMinimum']}")

    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{at}: needs at least {schema['minItems']} items")
        if "items" in schema:
            for i, item in enumerate(value):
                errors += validate(item, schema["items"], root, root_path, f"{at}[{i}]")

    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{at}: missing required field '{key}'")
        props = schema.get("properties", {})
        for key, sub in props.items():
            if key in value:
                errors += validate(value[key], sub, root, root_path, f"{at}.{key}")
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errors.append(f"{at}: field '{key}' is not allowed")

    for sub in schema.get("allOf", []):
        errors += validate(value, sub, root, root_path, at)

    if "if" in schema:
        if not validate(value, schema["if"], root, root_path, at):
            if "then" in schema:
                errors += validate(value, schema["then"], root, root_path, at)
        elif "else" in schema:
            errors += validate(value, schema["else"], root, root_path, at)

    return errors


def check_file(schema_path, doc_path):
    schema = load(schema_path)
    return validate(load(doc_path), schema, schema, schema_path)


def cases():
    """Yield (schema path, document path, expected to pass)."""
    for schema_path in sorted(HERE.glob("*.schema.json")):
        name = schema_path.name[: -len(".schema.json")]
        for doc in sorted((HERE / "examples").glob(f"{name}.valid-*.json")):
            yield schema_path, doc, True
        for doc in sorted((HERE / "examples").glob(f"{name}.invalid-*.json")):
            yield schema_path, doc, False
        for doc in sorted((REPO / "examples").rglob(f"*.{name}.json")):
            yield schema_path, doc, True


def main(argv):
    if len(argv) == 3:
        errors = check_file(Path(argv[1]), Path(argv[2]))
        for e in errors:
            print(e)
        print("valid" if not errors else f"invalid ({len(errors)} errors)")
        return 0 if not errors else 1
    if len(argv) != 1:
        print(__doc__)
        return 2

    failures = 0
    seen = {True: 0, False: 0}
    for schema_path, doc, should_pass in cases():
        errors = check_file(schema_path, doc)
        seen[should_pass] += 1
        ok = (not errors) == should_pass
        failures += not ok
        expect = "valid" if should_pass else "invalid"
        print(f"{'ok  ' if ok else 'FAIL'} {doc.relative_to(REPO).as_posix()} (expected {expect})")
        if not should_pass and errors:
            print(f"     first error: {errors[0]}")
        if not ok:
            for e in errors:
                print(f"     {e}")
    for schema_path in sorted(HERE.glob("*.schema.json")):
        name = schema_path.name[: -len(".schema.json")]
        for kind in ("valid", "invalid"):
            n = len(list((HERE / "examples").glob(f"{name}.{kind}-*.json")))
            if n < 2:
                print(f"FAIL {name}: needs a pair of {kind} examples, found {n}")
                failures += 1
    print(f"{seen[True]} expected valid, {seen[False]} expected invalid, {failures} unexpected")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
