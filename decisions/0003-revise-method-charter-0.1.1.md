# 0003. Revise the method and the charter to 0.1.1

Date: 2026-10-31. Status: accepted.

Revised files:
- `METHOD.md`, SHA-256 `1695fd4c6d41af26c4471a59d1e33133c6280574ef405bddd5187f4f13cd4038`.
- `CHARTER.md`, SHA-256 `074196758c0060f1687d7876da63d0cd32b47c7fcf05bfaa29ff8972d0ad5aa1`.

Sidecars: `METHOD.md.sha256` and `CHARTER.md.sha256` hold the same values in `sha256sum` format. These hashes replace the ones in decisions 0001 and 0002; every other item of those two records still applies.

## Decision

1. **Required.** This repository now follows the 0.1.1 texts of the method and of the charter, each fixed by its SHA-256 above.
2. **Required.** The revision changes labels and wording only. It adds no control and removes none:
   - METHOD.md, the label legend: a team adopting the method is held only to safeguards S1 to S5, and lines labelled Required bind this repository.
   - METHOD.md, section 7.6: the bullet on reviews of security changes, plans and approve-and-freeze decisions drops its closing "must", so its wording matches its Suggested label.
   - CHARTER.md, section 5: the bullet on a failure in a shared dependency carries the Suggested label, which matches its own "should" wording.
   - Both files: version 0.1.1 and a pointer to this record.
   - All specification files: every rule line carries the Required or Suggested label that its strength gives it, and a rule that holds both strengths is split into one Required bullet and one Suggested bullet, with the split text reworded where needed. In MODEL.md, ADAPTERS.md, RECORDS.md and ROADMAP.md, each added Required label names what it repeats, as the README requires. A Suggested line that said "must" or "required" now says "should" or "advised" (for example the METHOD.md line on logging the session's age, the tool and the model), and the ADAPTERS.md opening sentence and one heading no longer say that the file carries no label or sets conditions that must be met.

## What this decision does not do

- No signature from the owner comes with this decision, and nothing was verified at runtime. It changes only the adopted description and the digests.

## How to verify

```
sha256sum -c METHOD.md.sha256 CHARTER.md.sha256
```

The check must report `METHOD.md: OK` and `CHARTER.md: OK`, and each sidecar must hold the SHA-256 named above.
