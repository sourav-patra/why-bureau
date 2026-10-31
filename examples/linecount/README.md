# Worked example: adding a flag to linecount

linecount is a made-up, small public command-line tool that counts lines in files. This example follows one change through the method, the charter and the specification. Every name, model and number is a placeholder.

## 1. Purpose

The owner writes a purpose item and locks it before work starts:

- Id: `REQ-01`.
- Goal: add `--exclude PATTERN`, which skips files whose path matches the pattern.
- Reason: users count lines in source trees and want to leave out generated files.
- Reserved acceptance: `tests/acceptance/test_exclude.py` and its fixtures under `tests/acceptance/fixtures/`. The lock records their SHA-256.

The owner also signs off the run authorisation: the outcome is `REQ-01`; writable paths are `src/linecount/` and `tests/dev/`; the action types are reversible internal writes plus opening one pull request; data may go only to the approved provider; the budget is 12 USD with 4 USD reserved for verification; it expires in five days.

## 2. Roles and posts

- The builder role is in [builder.role.json](builder.role.json): minimum grade `build`, isolation grade G2, permission class approved-item fix, write scope `src/linecount/` and `tests/dev/`, and record kind `code` only. The reserved acceptance tests are outside its write scope.
- Its escalation path is in [builder.escalation-path.json](builder.escalation-path.json): one round at `build`, one at `senior`, three at `top`, then the project owner. These counts are the example project's own choice; MODEL.md gives the suggested ones. Changes under `src/linecount/security/` use an area override that goes from `senior` straight to the owner.
- A reviewer post, separate from the builder post, reviews the change.
- The operator's private model roster maps `build` to a placeholder model, `model-a`, at `provider-a`. The repository never names the model; the run record does, because it is a factual record.

## 3. First attempt

The host runs its entry check: the role's request against the run authorisation, minimum grade, destination eligibility, quota holds, budget. The dispatcher proposes `model-a`, and the host accepts the pick. To follow the work, the case lead opens a progress table inside the task ledger the project already keeps:

| State and evidence | Task or agent | Parent | Last update | Current action |
|---|---|---|---|---|
| running | asg-0007 attempt 1 | REQ-01 | 2026-10-30T08:40:00Z | running tests |

The builder edits `src/linecount/cli.py`, adds a development test, and reports "done". The host runs the reserved acceptance tests itself: exit code 1. The worker's "done" stays a claim. The run ends in the failure state engineering failure. See [run-0040.run-record.json](run-0040.run-record.json).

## 4. Escalation

The escalation path gives one round at the `build` grade, already used, so the next step is `senior`. The round opens with the failing test output, the purpose item, the earlier attempt and a changed diagnosis: the pattern was matched against the file name instead of the full path. The senior round diagnoses and rescopes, then hands implementation back to the builder role at its own grade. It gains no extra permissions.

## 5. Second attempt and review

The second attempt passes the reserved acceptance tests on the host. A reviewer post then works in a session of its own, using a model whose vendor family is not the builder's. It reads the diff and the surrounding source, and ties its verdict to both the candidate digest and the acceptance digest. The run record is [run-0042.run-record.json](run-0042.run-record.json). It was launched without a dispatcher, so it carries the marker `local` with a reason and an evidence digest.

The progress table now reads:

| State and evidence | Task or agent | Parent | Last update | Current action |
|---|---|---|---|---|
| failed: run-0040, acceptance exit 1 | asg-0007 attempt 1 | REQ-01 | 2026-10-30T08:52:30Z | none |
| completed: run-0042, acceptance exit 0, verdict-0043 | asg-0007 attempt 2 | REQ-01 | 2026-10-30T09:14:10Z | none |

## 6. Merge and retention

Merging into the protected `main` branch is irreversible and high value, so the owner approves it through the protected approval mechanism (S2). The scratch tree from attempt 2 is past its retention date and is marked `unavailable` in the run record; its digest stays. The failed attempt 1 and its evidence are kept, because adverse records stay protected even after a later success.

## Checking the files

```
python schemas/check.py
```

The check validates every `*.role.json`, `*.escalation-path.json` and `*.run-record.json` file in this folder.
