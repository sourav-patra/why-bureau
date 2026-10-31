# 0002. Adopt the why-bureau charter 0.1

Date: 2026-10-30. Status: accepted.

Adopted file: `CHARTER.md`, SHA-256 `3542771519880470aa44daa23cc8f37574c09c9f12d420790aa110a343888a49`.

Sidecar: `CHARTER.md.sha256`, which holds the same SHA-256 in `sha256sum` format.

## Decision

1. **Required.** This repository is governed by charter 0.1, as identified by the SHA-256 given above.
2. **Required.** Every section of the charter except section 10 (team model) takes precedence. Section 10 holds Suggested controls, and its lines marked Required only repeat a safeguard or another section of the charter.
3. **Required.** When the specification and the charter disagree, the disagreement is recorded in the specification's open-questions section.
4. **Required.** Any later charter revision takes effect only through a fresh decision record stating its SHA-256.
5. **Required.** A copy of CHARTER.md is the adopted text only when its hash equals the one its sidecar holds.

## What this decision does not do

- No signature from the owner comes with this decision, and nothing was verified at runtime. It changes only the adopted description and the digest.

## How to verify

```
sha256sum -c CHARTER.md.sha256
```

The check must report `CHARTER.md: OK`, and the sidecar must hold the SHA-256 named above.
