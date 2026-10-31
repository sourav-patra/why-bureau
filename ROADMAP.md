# Roadmap

Part of specification 0.1. Status: draft specification; no reference implementation yet.

The prototype grows in numbered steps, and a step's acceptance items must all pass before the next step begins.

## Guiding rule

**Suggested.** Begin with attended work, and qualify the real launch path before automating more.

## Where things stand

This repository already holds the first slice of step 1, the schemas and their check. Nothing else in the plan has started, including the minimal reference adapter with its render and escalation configuration, and the compliance check.

## Steps

| Step | Working name | What gets made | Finished when | Label |
|---|---|---|---|---|
| 1 | Foundations | Machine-readable definitions of roles and run records, the smallest workable escalation path, rendering of configuration, one adapter and one host. | Two reviewers independent of the authors sign off, and one of those reviews looks at security; launch tests exercise a run whose authority is withdrawn partway through, a request sent twice, hostile file paths, and a crash that happens before anything is recorded; any attempt to loosen an entrenched field is turned away; and an area override configured in the escalation path is honoured. | **Required** (repeats charter sections 2 and 6: independent review; relaxed sealed fields turned away); **Suggested** (the rest, except the area-override acceptance description, which carries no label) |
| 2 | First real project | Run records the host authenticates, each carrying the required run ids and usage figures; the operator's own settings layer; and a sample project. | The sample project's own checks are green; edits by workers, replayed records and records stitched together from parts are all turned away; tampered memory makes nothing happen; and every review is tied to the precise candidate it judged. | **Required** (repeats S4 and charter section 7: run ids on every record; tampered memory makes nothing happen); **Suggested** (the rest) |
| 3 | Routing | The dispatcher, wired in. | Assignments that are harder get a higher grade; destinations nobody approved are refused; and a refusal or a wait stays in force with no route around it. | **Required** (repeats S3 and charter section 8: destinations nobody approved are refused; host refusals and quota holds stay in force); **Suggested** (the rest) |
| 4 | Watched pilot | Joins across observations, plus a pilot that a person watches throughout. | Seven days of reports exist, broken down by grade and by role, covering cost and human interventions for each accepted outcome, how escalations were closed, and which observations were missing. | **Suggested** |
| 5 | Self-checking | The compliance checker and the sentinels. | Projects using the model report on independence, run records, sentinels, minimum grades and schemas; and the checker cannot sign off changes to itself. | **Required** (repeats charter section 8: the checker cannot sign off changes to itself); **Suggested** (the rest) |
| 6 | Running alone | The runtime for unattended work, delivered in two stages, the first before the second. | Stage one: usage collection has been verified and reservations settle correctly. Stage two: a full unattended day on a qualified setup, with an entry check every time the runtime wakes and run limits enforced. | **Suggested** |
| 7 | Clearing old evidence | The protected records sweep. | When the sweep rehearses a deletion, its list spares both evidence that something cites and adverse records that nothing cites; and the tests take in the markers that stand in for deleted payloads, memory sources that recall notes quote, references that are ambiguous or unreadable, and each reference source and form. | **Required** (repeats charter section 8: adverse records that nothing cites are spared); **Suggested** (the rest) |

### First slice of step 1

- The schema check runs on the standard library alone, so any machine can run it without installing anything.
- The slice is done once that check passes and the leak scan finds nothing on that commit.
- `schemas/` holds JSON Schema files for the run record, the role and the escalation path.
- Every schema comes with a pair of sample documents that pass, a pair that fail, and a check anyone can run.
- Each control is encoded as Required or Suggested, and no Suggested control becomes a required field.
- Every control in the specification must carry its label before this slice starts and before the step 1 acceptance item on area overrides takes effect. In this repository every control is labelled, so both conditions are met.

## Open questions

Choices for the first reference implementation:

- What protected storage and what authentication mechanisms should hold retention indexes, run records and run authorisations?
- Which attention budgets, escalation counts, per-area overrides and arbiter wait interval suit the first project that adopts the model?
- Which pilot results and role sentinels would show that a grade's capability minimum is enough?
- The first reference implementation needs a target: what host and runtime, and which of that host's controls could it realistically qualify?

Not yet measured:

- Is the model wanted? Uptake has not been researched, and nothing has yet been evaluated side by side with alternatives.
- Whether the security controls actually hold, shown by putting each boundary to adverse qualification on the real launch path; no implementation results exist yet.
- The load the model puts on people: for each accepted outcome, how many approvals, overrides, questions and rulings it took, coordination of shared posts counted in.
- Whether sending work by grade saves money while keeping accepted outcomes level. Settling that means breaking acceptance, latency, tokens and money down by grade and by role, with verification, reviews and retries all counted.
- Where in the escalation path failures get resolved: per grade, how often a failure is closed there, and how often only the person closes it, with no success rate taken for granted at top.
- Whether cross-family review uncovers defects that same-family review would not; answering it takes defects that were confirmed, verdicts given independently and comparable candidates, and the family's effect has to be separated from the reviewer's capability.
- Whether durable post memory lowers context cost, comparing a bounded post start with rebuilding history and measuring tokens and source correctness.
- Whether outcomes get better when purpose is traced and retention is managed, judged by rework against the locked purpose and by how much storage is kept or deleted with no protected evidence lost.

Disagreements between this specification and the method or the charter: none recorded.
