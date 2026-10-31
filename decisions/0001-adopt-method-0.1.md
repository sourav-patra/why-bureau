# 0001. Adopt the why-bureau method 0.1

Date: 2026-10-30. Status: accepted.

Adopted file: `METHOD.md`, SHA-256 `821237703725341b99470620f1693a0d0bad69335803bf102774fa3677ad48c5`.

Sidecar: `METHOD.md.sha256`, which holds the same SHA-256 in `sha256sum` format.

## Decision

1. **Required.** A copy of METHOD.md is the adopted text only when its hash equals the one its sidecar holds.
2. **Required.** Any later revision of the method takes effect only through a fresh decision record stating that revision's SHA-256.
3. **Required.** The safeguards S1 to S5 and the fourteen tenets of method 0.1 govern this repository: the specification now, and any reference code that is added later.
4. **Required.** Where the specification and the method conflict, the stricter of the two applies, and the conflict is logged in the specification as an open question.
5. **Required.** The specification spells out, in its own words, every tenet it relies on; a reader needs no other document to follow it.
6. **Required.** The team-model guidance in the method is advice: Suggested controls come first, and they become rules only once real runs have produced data.

## What this decision does not do

- No signature from the owner comes with this decision, and nothing was verified at runtime. It changes only the adopted description and the digest.
- Where a copy of a text locked elsewhere is adopted, the copy's lock is distinct from the original's lock, and the copy establishes no enforcement at runtime.
- Only the text adopted by the latest decision record is in force; superseded versions remain only in version control history.

## How to verify

```
sha256sum -c METHOD.md.sha256
```

The check must report `METHOD.md: OK`, and the sidecar must hold the SHA-256 named above.
