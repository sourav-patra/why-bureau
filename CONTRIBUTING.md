# Contributing

## Proposing a change

1. Open an issue that says what you want to change and why.
2. Send a pull request that makes the change. Keep it small.
3. Run `python schemas/check.py` and make sure it exits with status 0.
4. The pull request is reviewed by a person other than its author before it is merged.

## Changing METHOD.md or CHARTER.md

METHOD.md and CHARTER.md are adopted texts. For each, a record in `decisions/` pins the exact SHA-256 at which it was adopted.

- Every adopted file has a SHA-256 sidecar file next to it, named after the file with `.sha256` added, in `sha256sum` format (`METHOD.md.sha256`, `CHARTER.md.sha256`). Check both with `sha256sum -c METHOD.md.sha256 CHARTER.md.sha256`.
- Changing an adopted file means writing a new decision record naming the file's new SHA-256 and its refreshed sidecar. Until that record exists, the changed file does not count as adopted.
- A copy is the adopted text only when its hash equals the one its sidecar holds.
- When the repository holds a copy of a text locked elsewhere, the copy is identified in two ways: the source digest identifies the original it came from, and the copy's own sidecar identifies the copy. The copy's lock is distinct from the original's lock, and the copy establishes no enforcement at runtime.
- Adopting a text records no owner signature and no runtime check. It changes only the adopted description and the digest.
- The text adopted by the latest decision record is the one in force. Superseded versions stay only in version control history.
- Adopting a text gives it no new signature and qualifies no runtime.
- Adopted texts, their sidecars and any adoption index live either in `docs/texts/` or at a path named in `.gitattributes`. Every file under `docs/texts/`, and every file `.gitattributes` names, is stored byte-exact with no line-ending conversion. Do not let an editor or a tool rewrite their line endings.

## Labels and the grade-only rule

- Every control in the method, the charter and the specification carries a label: **Required** or **Suggested**. In the specification, a Required control names the safeguard, tenet or charter section it repeats. A Suggested control is never written as a rule.
- Rules name grades (build, build-lite, fast, review, senior, top) and never a vendor or a specific model. Specific models are named only in private model rosters and in factual run records.

## What belongs in this repository

- General rules, public ideas and normative controls.
- Not private records, censuses of projects, local measurements, machine paths, people, or framing specific to one organisation.
- Building, testing and releasing need no dispatch history, no post archives and no private overlays. A contributor is free to use a memory of their own, or to work without one.
