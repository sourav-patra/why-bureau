# The operating model

Part of specification 0.1. Status: draft specification; no reference implementation yet.

This file names the parts of an accountable team of people and AI agents, shows how the parts fit, and says what happens when work fails. Labels follow the README: a **Required** control names the safeguard, tenet or charter section it repeats, and a **Suggested** control is something to trial and evaluate.

## Tenets this specification relies on

- **Required** (repeats decision 0001). The specification carries, in its own words, each tenet it depends on, so it needs no other document to be understood. They are:
  - Only verifiable work is delegated: the agent needs a check that it can run and would struggle to cheat (tenet 5).
  - Extra structure arrives only after the simpler arrangement is measured, at an equal token budget, and found wanting (tenet 7).
  - Nobody grades work they did themselves; a separate checker with a fresh context does (tenet 10).
  - State that has to live through a crash or into a new session is written to a durable record (tenet 11).
  - What checks and records show is the result; a claim of completion is not (tenet 12).
  - Code checks what the model proposes, text is data and never authority, and a new model never brings wider permissions (tenets 2 and 3, S4 and S5).
- **Required** (repeats decision 0001). Where this specification and the method disagree, whichever rule is stricter governs, and the disagreement is entered as an open question of the specification, in the "Open questions" section of ROADMAP.md.
- **Required** (repeats decision 0002). If this specification and the charter conflict, the conflict is logged in that same open-questions section.

## The nine elements

In alphabetical order:

- Assignment. The unit of work: exactly one bounded outcome, serving exactly one purpose item. It carries three identifiers (its own id, its run id, and its parent), and the host must have seen its acceptance checks pass before it is complete.
- Authority rules. Which people may approve which actions, written so that no model or provider is mentioned.
- Grade. A capability class that belongs to no model and no provider.
- Memory. What lets a post resume: search across authoritative documents, post briefs with a size cap, recall notes that have been checked against where they came from, and typed entries.
- Model roster. A dated mapping, owned by the operator and kept apart from the repository's rules, that says which concrete model fills each grade, which providers are approved, and what the declared fallbacks are.
- Post. An accountable identity that persists over many sessions, filling one role on one project and keeping its own handoff, in-tray and memory.
- Purpose. The locked statement of the wanted outcome and its motive, together with the reserved set of acceptance checks that defines done.
- Role. A job, described by the minimum grade it needs, the write scope it may use, the permissions it asks for and what it is for.
- Run record. The permanent account of a run, binding authenticated host observations and worker claims, kept apart, to the artifacts involved.

- Accountability belongs to the post. The model roster just records which model is filling each grade right now.
- A roster switch changes nothing about a post's memory boundaries, its obligations or its identity.
- **Suggested.** Use the nine elements the same way everywhere.

How they connect:

- The meaning of done is fixed by the purpose before work starts.
- The authenticated run authorisation is the source of authority, and what a role asks for is measured against it.
- The protected host observes the evidence, model rosters pick the models, and grades set the minimum capability.
- Outcomes, revisions and identities are derived by the host; workers only make requests.

## Design principles

- When consequences are higher, the reviewing model must differ from the author's and be of equal or higher grade, preferably from another vendor family. Every review looks at the real candidate under an independent identity.
- Model confidence proves nothing passed. A cheaper build model is fine only where checks are adequate and review is independent.
- Handoffs are bounded in size, and memory is checked against sources.
- Controls are qualified before any unattended work, and the yardstick for choosing between options is what each accepted outcome costs.
- No approval or grant can come from retrieved instructions, memory records or role prose.

## Roles

- Starting roles, in alphabetical order: builder, coordinator, fixer, planner, reviewer, security reviewer. A project is free to define extra roles; a designer is one example.
- What a role is called gives it no authority.

A role definition holds these fields (the schema uses the same order):

| Field | What it holds |
|---|---|
| Name and purpose | A stable id, and the job the role exists to do. |
| Permission class | The class requested under the adopted charter, checked against an existing run authorisation. |
| Write scope | Repository paths and permitted record kinds, with reserved acceptance kept apart from development tests. |
| Tools | Which tools the role wants; every one is still checked for destination and authority. |
| Isolation grade | The isolation and enforcement it needs (G0 to G3 in the method). |
| Minimum grade | The lowest capability class allowed; more complex tasks can raise it. |
| Independence | What it needs in non-author review and in review from another vendor family. |
| Escalation path | Ordered steps, each with its rounds; the budgets and any area overrides; and finally a person. |
| Sentinel set | Where in the repository the role's few qualification tasks are kept. |

- Role definitions come through one of two supported interfaces: role files that `AGENTS.md` already references, or a TOML team file at `roles.toml`.
- Purpose items, for instance in a `docs/purpose/` folder, have identifiers, reserved acceptance and locked revisions; every assignment names its item and that item's locked digest. Layouts a project already has can be mapped onto the schema.

The machine-readable form is `schemas/role.schema.json`.

## Grades

- fast: quick, simple jobs. It may run locally, but only once that is measured and qualified.
- build-lite: minor fixes and modest implementation jobs; nothing about acceptance or review is relaxed for them.
- build: ordinary implementation within one bounded assignment.
- review: judging work carefully in a session of its own, and from another vendor family wherever policy demands one.
- senior: dependable everyday reasoning for planning, for bounded engineering rulings, and for reviewing locks.
- top: the most capable approved model currently on offer, usually reached by escalating. A person must decide explicitly before it becomes any role's minimum grade.

- More complex tasks may push a role's minimum grade up, but never down.
- Rules speak only of grades. Concrete models appear in private model rosters and in factual run records, nowhere else.
- Placeholder examples may show a roster with local models, with several providers, or with only one provider.
- If the roster has only one provider, any review that must come from another vendor family goes to a person instead, or else waits.

## The seven layers

| Layer | Short name | What it contains | Who looks after it |
|---|---|---|---|
| Layer 0 | Ground rules | The guarded home of policy and authority: the limits the organisation puts on roles, how much each run and how much human attention may cost, signing, independence requirements, approvals, and which permission classes exist. | Drafted by the charter maintainer; an authorised person then accepts it and freezes it. |
| Layer 1 | Role catalogue | Every role definition the repository has approved, with its tools, minimum grade, capability requests, sentinels, sandbox needs, independence, escalation path and per-record-kind write scope. | The project's maintainers, changing it only through review. |
| Layer 2 | Operator's model choices | A layer the operator lays over the rest: approved providers, a dated assignment of models to grades, per-role individual settings, and the fallback sequence. | The operator, inside whatever room the rest of the stack leaves. |
| Layer 3 | Work routing | A proposal, per assignment, of which effort, tool and model to use, based on holds, usage, availability and capability; the proposal comes from a dispatcher or from a local adapter choosing for itself. | The dispatch maintainer. |
| Layer 4 | Launch and run | The machinery that executes work: a runtime that executes inside a sandbox, a trusted writer of records, a ledger that books budget in advance, a broker that hands out credentials on request, and a guarded host that decides whether a launch may go ahead. It offers one way to launch attended work and one for unattended work. | Whoever maintains the host and the runtime. |
| Layer 5 | Recall | Storage for handoffs and typed entries, recall notes checked against their sources, moving a post from one holder to another, post briefs with a size cap, and search over authoritative documents. | Whoever maintains memory and retrieval. |
| Layer 6 | Proof and learning | Protected run records, a service that joins dispatch events to session logs, evaluation, retrospectives, sentinels and a compliance checker. | Posts look after their own records, and evaluation is the method maintainer's job. |

Across layers:

- Model rosters need default mappings, and they report overrides that have gone stale.
- Usage figures are advice only, until both the collection of usage and the settling of reservations have passed checks on the real path.
- Several projects may share posts for observation, retrieval, memory and dispatch; owning such a post grants no access to content.
- Every project, and within it every trust zone, gets its own separate records, caches, in-trays, indexes and memory.
- No session reads data unless its role and its provider eligibility allow it; data crosses from one trust zone to another only through an export someone explicitly approved.
- Project posts stay separate for each project and each role.
- With more and more projects, the load of coordinating them is counted as the human interventions each accepted outcome needed.

## Failure states

| State | What happened | What comes next | Label |
|---|---|---|---|
| unknown | The host has no way to establish how it ended. | Anything that depends on it waits until the operation, and every effect it had, have been reconciled. | **Required** (repeats charter section 8) |
| wait | Quota, dispatch or budget controls are holding the assignment. | Wait, or take an alternative that is explicitly permitted; never lower the minimum grade to get past the hold. | **Required** (repeats charter sections 6 and 8) |
| refusal | A policy or a model refused. | Apply the adopted refusal policy; switching the task to another model happens only where written policy plainly permits it. | **Required** (repeats S5) |
| timeout | The run reached its time cap and was stopped. | Bring every descendant process and every outside effect into line with the record before anything else; after that, handle the run as an engineering failure. | **Required** (repeats charter section 8) |
| cancellation | Someone stopped the work. | No retry happens until someone gives a fresh instruction. | **Suggested** |
| engineering failure | The host saw the run end with failing checks. | Try again, following the approved escalation path step by step. | **Suggested** |

- **Required** (repeats charter section 8). Nobody may rename an unknown, cancellation, wait or refusal as some other state in order to get a different model; each of the four stays what it is.

## The escalation path

- **Suggested.** Each role has an escalation path, approved and adjustable, made of ordered steps; each step points at a grade or at a person and allows any number of rounds, zero included, and overrides for particular areas or paths may be added.
- **Suggested.** A deployment may make a person the only step; model steps beyond that are optional.
- **Suggested.** No configuration can take the final person off an escalation path.

How a path is described:

- **Suggested.** A path is a list of steps, each aimed at either a grade or a person. Each step allows a number of rounds (tries); a step given zero rounds is passed over. The adopting policy fixes the real numbers. The suggested default climbs like this:

| Climb | Who tries | Suggested tries |
|---|---|---|
| 1st | Whatever grade the assignment already has | 1 |
| 2nd | The build grade one size up | 1 |
| 3rd | senior | 2 |
| 4th | top | 2 |
| last | A person | no count set; the path ends here |

- **Suggested.** An area override replaces the path for work matching a label or a path. By default there are none. A security area is the one suggested exception: it may climb from senior directly to the person, leaving out top.
- **Required** (repeats charter section 8). A budget ceiling is reserved ahead of each round, within the assignment's budget and its reserved verification allowance.
- **Suggested.** Above a step that failed, a vendor preference may lean toward a provider of another family, though never outside the destinations cleared for that data class or the refusal bindings already in place; that destination limit is **Required** (repeats S3).

What always holds:

- **Suggested.** A person is always the final step. A grade with no mapping is skipped and the reason recorded, while destination limits, independence and minimum grades stay in force.
- **Suggested.** A question about priority, scope, permissions, credentials or a lock does not climb the model steps at all; it goes straight to a person, since authority that is absent cannot come from any model.
- **Required** (repeats S5). The senior and top rounds diagnose and cut the job down to size, after which building returns to the grade the role normally uses; a more capable model gets no extra builder permissions.
- **Suggested.** A round opens with four things: the evidence against the last attempt, the purpose item, the history of attempts, and a diagnosis that has changed. Every step further up starts from a clean context but keeps the assignment's existing run authorisation, and that this authorisation does not change is **Required** (repeats S5).
- **Suggested.** When the path reaches the person, an arbiter that was authorised beforehand may stand in, but only inside its limits.
- **Suggested.** When a fix round fails, file an issue; switch to some other assignment only if its required dependencies are still verified.
- **Suggested.** A role that fails three times running is stood down.
- **Suggested.** Every round, skip, step and reason is logged in the run record, and budget is reserved before it is spent.
- **Suggested.** Escalation follows the role's protected escalation path and its invariants: every round and skip leaves a run record, budget is reserved, the run authorisation does not change, the person comes last, and authority questions go straight to that person.

The machine-readable form is `schemas/escalation-path.schema.json`.

## Posts, handoffs and sessions

- A post declares how it hands off, what it may write, what it may read, and its purpose.
- A handoff never contains transcripts. It carries the acceptance evidence, pointers to sources, the item id and the item's state.
- During a session an agent backs what it claims with first-hand evidence, keeps within its role, leaves trust labels intact, and halts at a refusal.
- At the close of a session, the agent states what was run and what is still not known.

## Run sequence

A run moves through three phases, always in the same sequence.

- Preparation. The runtime first writes down the purpose being served. Code then claims the work item, sends it where the declared routing table says, and makes sure the budget can cover it.
- Work. Code opens a post inside the one sandbox that post is permitted. The post loads its memory, does everything through tool boundaries that are checked, and wraps its output in an envelope.
- Hand-back. The parent folds that output in only after the run records it depends on are in its hands.

## Messages between agents

- A message envelope is versioned and carries a hash of the content, a trust label and the source.
- Grants are never carried inside message envelopes; they use a separate channel that the host authenticates.
- A durable outbox commits each state change together with its outgoing events, so one never happens without the other.
- Passing through the gateway (the policy enforcement point) means four checks: on the effect, on the scope, on the session, and on who is calling.

Sources: REFERENCES.md entries 94 and 102.

## Memory

Seven memory types are kept apart. They fall into three groups:

- About the model and the task: warnings about what the model knows, and commitments.
- What lasts: facts, procedures, and retrieval.
- The current thread: session history and working context.

Writing memory:

- Memory is written by deterministic code alone. Taking in new material, sorting it, tying it to its source and putting together the briefing are all done without asking a model.
- A recall note quotes its source, and the quote is confirmed to exist in that source twice over: once before the note is saved, and again on every later read.
- **Required** (repeats charter section 7). Any author attribute on memory is a claim.
- **Suggested.** Whatever is ingested or retrieved keeps its revocation status, its source revision, its trust label and authenticated provenance.
- **Suggested.** Recall notes are checked against their sources, and superseded or stale sources are dealt with.
- Outdated facts are refreshed or retired.
- Private data held in memory is fenced by access boundaries and kept only under safe retention.

Reading memory:

- **Required** (repeats S4). Only the protected authority store originates executable policy and approvals. Summaries, role prose, retrieved text, typed entries and in-tray messages can create neither approvals nor privileged post-start instructions.
- Briefing and lookup work like this. The briefing an agent starts with never exceeds its size allowance, and its parts always appear in the same sequence. It holds summaries; a memory's complete text is pulled in later, and only if the work calls for it. Retrieval stays silent until someone asks, and then it must return what bears on the question, since a reliable origin alone does not make an item relevant. Any answer drawn from memory names the recall notes behind it by id, and if memory holds nothing on the point, the answer says so.

Keeping memory healthy:

- Operators can see what was left out, what was retrieved and what was stored.
- Memory is shaped to suit whatever tools and interfaces consume it.
- Memory storage remains manageable as history grows.
- Eight memory tests, MT1 to MT8, in three groups: safety (poisoning, isolation and redaction); fidelity (grounding, determinism, and recall from a cold start); and limits and recovery (budget and restoration).
- Risks to guard against in action: disclosing data, ignoring the governing rules, acting outside the authorised scope, and erratic behaviour while a run is in progress. What counters them: records under protection, verification, and limits on what agents can do.
