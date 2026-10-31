# Schemas

JSON Schemas (draft 2020-12), version 0.1, for three documents of the specification.

| Schema | Describes | Text |
|---|---|---|
| `role.schema.json` | A role definition. | MODEL.md, "Roles" |
| `escalation-path.schema.json` | A role's escalation path. | MODEL.md, "The escalation path" |
| `run-record.schema.json` | The permanent record of one run. | RECORDS.md, "Run record fields" |

## How labels become schema rules

- A Required control that a schema can express is enforced: a `required` field, a `const`, or an `if`/`then` rule for fields that are mandatory only in some cases.
- A Suggested control never becomes a required field. Where a schema has a field for a Suggested control, the field is optional.

Examples of the split:

- Non-author review is Required, so `independence.non_author_review` must be `true`. A reviewer from another vendor family is only Suggested, so `independence.different_vendor_review` may be left out.
- The per-round budget of an escalation path is Required, so `budget_per_round` must be present. Vendor preference is Suggested, so `vendor_preference` is optional; when it is present, its destination limit is Required, so `approved_destinations_only` must be `true`.
- Declaring a minimum grade, the record kinds a role writes, and an escalation path are Suggested, so `minimum_grade`, `write_scope.record_kinds` and `escalation_path` are optional. The steps of an escalation path and the rounds at each step are Suggested too, so `steps` and `rounds` are optional. When any of these fields is present, it must still have the shape the schema gives it (`role.valid-3`, `escalation-path.valid-3` and `escalation-path.valid-4` omit them; `role.invalid-3`, `role.invalid-4`, `escalation-path.invalid-3` and `escalation-path.invalid-4` break their shape).
- A person as the last escalation step is Suggested, so the schema does not enforce it. The compliance checker (ADAPTERS.md) reports it, and an organisation can entrench it as a layer field.
- In a run record, every field group is mandatory; `run-record.invalid-3` to `run-record.invalid-9` each leave out one required field from a different group. `qualification_id` is mandatory when `live_launch` is `true`, `render_digest` when `rendered_config` is `true`, and a `local` dispatch needs a `reason` and `evidence`.

A schema can only vouch for the shape of a document; the authenticity and bindings of a run record are settled against protected records.

## Running the check

From the repository root:

```
python schemas/check.py
```

The script needs Python 3.8 or later and nothing else; it uses only the standard library and implements the subset of JSON Schema these files use. It checks:

- `schemas/examples/<schema>.valid-<n>.json` must pass, and `<schema>.invalid-<n>.json` must fail. Each schema has at least two of each.
- Every `examples/**/*.<schema>.json` file must pass.

It prints one line per document and exits with status 0 when every document behaves as expected, 1 otherwise.

To check one document:

```
python schemas/check.py schemas/run-record.schema.json path/to/record.json
```

This prints the errors and exits with status 0 if the document is valid, 1 if not.
