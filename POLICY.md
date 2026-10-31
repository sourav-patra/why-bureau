# Policy rules

Part of specification 0.1. Status: draft specification; no reference implementation yet.

These rules cover budgets, switches of model roster, the arbiter, who writes which record kind, and how a role's request meets a run authorisation. A **Required** control names the safeguard or charter section it repeats; a **Suggested** control is something to trial and evaluate.

## Budget

- **Required** (repeats charter section 8). Verification capacity is reserved before implementation has a chance to consume it.
- **Suggested.** A protected budget ledger, organised as a hierarchy, makes atomic reservations ahead of every launch and every paid call, covering providers, shared posts, reviews, escalations, children and retries.
- **Suggested.** Spending is held while consumption has not been reconciled.
- **Suggested.** Processes, concurrency, time and tokens all have enforced limits, and cancelling a run ends every descendant.
- **Suggested.** Budgets for human attention are declared and then measured.

## Model roster switches

- **Required** (repeats S3). Validate the real accounts, endpoints and providers that sit behind a roster.
- **Required** (repeats S3 and S5). Switching rosters changes nothing about which destinations are eligible, which refusals are bound, or which run authorisations exist.
- **Suggested.** A roster switch keeps post identity and role minimum grades.
- **Suggested.** The record of each roster switch holds its reason, its time and its revision.
- **Suggested.** With no eligible model left, the work waits.

## The arbiter

- **Suggested.** Once the planner is stuck and the person has gone 30 minutes without answering (or whatever other interval was adopted), an arbiter may decide engineering choices, staying inside the existing run authorisation. The arbiter must be authenticated, must have been named beforehand by someone authorised to do so, and must not be among the authors.
- **Suggested.** Silence gives the arbiter nothing.
- **Required** (repeats charter sections 6 and 9). The arbiter cannot decide permissions, reserved acceptance, new effects or conflicts of authority; those remain blocked until the person decides.
- **Required** (repeats S2 and charter section 7). Delegation to the arbiter never extends to signing, tagging, merging or changing locks.
- **Suggested.** Record the ruling, the clauses it applied, the delegation and the question that was put.

## Record kinds and who writes them

- **Suggested.** An assignment groups its inputs by record kind and pins each one to a revision and a digest.
- **Suggested.** The repository is classified, and retrieval works, with one shared set of record kinds; locked purpose outranks explanatory material.

| Record kind | Written by | Holds | Label |
|---|---|---|---|
| evidence | The authoritative facts come from protected services, verdicts from reviewers, and claims from workers. | Cited artifacts, reviews and run records. | **Required** (repeats charter section 7) |
| code | Builder or fixer, but only inside the paths they declared. | The implementation itself, together with development tests. | **Required** (repeats charter section 9) |
| knowledge | A role that has been given this kind explicitly, and no other. | Documents that explain things or serve as reference. | **Suggested** |
| design | The designer, within the assignment's run authorisation. | Decision records and designs. | **Suggested** |
| purpose | Either the planner or the acceptance steward, by way of protected approval given before the run. | Every reserved acceptance check, the desired result, and the reason for it. | **Required** (repeats charter section 8) |

- **Required** (repeats charter section 8). Purpose or reserved acceptance changes only with a newly locked revision and explicit approval.
- **Required** (repeats charter section 8). Reserved acceptance can be changed by the acceptance steward alone, only ahead of the run, and only by approving and locking the change.
- **Required** (repeats charter section 9). Development tests written as code are welcome from builders, but the reserved acceptance that grades their work is off limits to them.
- **Suggested.** The assignment pins the whole reserved acceptance set by digest.
- **Suggested.** Within one assignment, a single role may not write both a piece of code and the purpose that judges it.
- **Suggested.** Reviewers write verdicts and never quietly alter the candidate they are reviewing.
- **Required** (repeats charter section 8). No candidate can switch on a changed rule that would then govern how that same candidate is executed or approved.

## Roles ask, run authorisations decide

- **Required** (repeats charter section 8). No candidate governs its own run or its own approval.
- **Required** (repeats charter section 8). Every definition comes from a revision that was approved and can no longer change.
- **Required** (repeats charter section 6). A role's request is granted only where it overlaps with an authenticated run authorisation that is still in date and with the organisation's protected controls, and the host computes that overlap.
- **Required** (repeats charter section 6). A role asks for capabilities and for the right to write certain record kinds, and grants nothing itself.

## Permission classes

Each role requests one of the charter's five permission classes. Charter section 9 says, for each class, what it allows, what it must leave alone, and which evidence and review it needs. The host checks the requested class against an existing run authorisation.
