# The why-bureau charter

Version 0.1.1. Current status: draft specification; no reference implementation yet. Adopted by decision record 0002 and revised by decision record 0003.

This charter settles who may decide what. It follows the bounded mandate: people fix the purpose and the limits, agents work within them, and code checks that the limits hold. There are two mandatory parts, and both must be read: the core, sections 1 to 11, and the security annex, section 12.

Labels: **Required** controls bind this repository; **Suggested** controls are proposals to try and measure; unlabelled lines are definitions, facts or explanation.

## 1. The bounded mandate

- **Required.** An agent's room to act comes from two things together: the outcome someone approved and the operating limits attached to it. Each run keeps a single progress table inside a ledger it already has (section 4).
- **Required.** People return to the loop when an action calls for them, or when work has drifted outside what was approved.
- **Required.** Having a lock, a policy document or a clean lint run proves nothing about whether enforcement holds while the system runs.

## 2. Precedence

- **Required.** The method's five safeguards, S1 to S5, all remain in force under this charter.
- **Required.** Where the organisation has rules, or a project already has approved controls, those come first and this charter second.
- **Required.** Inside the approved scope, engineering judgement is permitted, and so is work that carries on independently.
- **Required.** If a project's adopted rules are stricter, the project amends them by its own authorised route before this charter applies to it.
- **Required.** Section 10 (team model) gives way to every other section. It holds Suggested controls, and any of its lines marked Required merely repeats a safeguard or another section. For a Suggested control there to harden into a rule, a later revision has to make it one, on the strength of data gathered from real runs.
- **Required.** Charter 0.1 is written for one owner. In that form it serves projects as design input and gives none of them a runtime grant.
- **Suggested.** Compliance, eligibility of a host, implementation and adoption are four distinct claims, and none of them implies any other.

## 3. The four layers of a mandate

- **Required.** Four layers are kept apart. Evidence: changed only by recording what happened; anyone acting adds to it, as versioned operational notes, and as protected records where an action is shared or of high value. It holds what ran, the source and authority it used, and the result seen. Live facts: refreshed from trusted observation under rules on freshness and invalidation, and never a source of permission. They hold consumption, automation configuration, the evaluator in force, and what the host can currently do. Work plan: revised by agents whenever they need to, subject to the review and checks that apply, without stepping outside the existing mandate. It holds task order, design details, how the work is split, and development methods and tests. Mandate: the owner alone changes it, using the authenticated mechanism already in place, and that holds for minor mandate amendments too. It holds approved outcomes, permissions, effects that are forbidden, reserved acceptance, expiry and hard limits.

## 4. One table for the state of a run

- **Required.** As a run begins, the case lead (the agent owning the run) proposes one progress table and keeps it in the task ledger or handoff file the run already uses.
- **Required.** The combined view is the case lead's; each worker reports its updates and evidence through whatever channels are already in place.
- **Required.** A child task carries the run id of its parent, along with a task identity and an attempt identity that are its own.

| Field | Holds |
|---|---|
| State and evidence | The current state, with a pointer to the evidence. |
| Task or agent | What the row describes. |
| Parent | The task that handed this one out. |
| Last update | A timestamp, time zone included. |
| Current action | What is happening now. |

- **Required.** The table has the fields listed above.
- **Required.** Seven states are used: unknown, completed, cancelled, failed, blocked, running and planned.
- **Required.** Whatever its state, planned and finished included, each task or attempt now in play gets one row and only one.
- **Required.** The table is updated when work becomes blocked, when a task completes, when it starts, when it is delegated, and when a check gives a meaningful result.
- **Required.** Every progress report includes the table as it stands, cut down to the run in hand.
- **Required.** Earlier attempts, and why they ended, stay in the existing ledger.
- **Required.** If evidence is stale or absent, the row's state changes to unknown and notes the time the evidence was last observed.
- **Required.** Marking a task completed needs the check or the run record that the run's acceptance terms name.
- **Required.** Every run opens with this instruction: "Track each delegated task in the ledger the run already has: its state and evidence, its parent, when it was last updated and what it is doing. Bring the table up to date whenever something meaningful changes, and include it in every progress report. Carry on with work that does not depend on anything blocked, and list each blocked task with what it is waiting for."
- **Required.** Running the table takes no extra tooling: no dashboard, no orchestration product, no heartbeat service and nothing watching from the background.
- **Required.** What a row shows is operational state as someone reported it; the evidence itself lives in the linked check and the platform's record.
- **Required.** Evidence of actions still comes from protected CI and code-host records, which the table does not replace.
- **Required.** A heartbeat shows only that something is alive.
- **Required.** When a parent goes quiet, that does not show its children have stopped.
- **Required.** A parent holds off completing or integrating dependent work until it has the child run records that work needs.
- **Required.** Operational data is sent nowhere but to places cleared to receive it.
- **Required.** Records of actions and outcomes contain neither raw secrets nor hidden reasoning.
- **Required.** If platform events cannot be obtained, that limitation is labelled.
- **Required.** Claims nobody can back are never stitched together into a supposedly full history of what happened.

## 5. Checks that cannot be completed

| State | Can it count as a pass? | When it applies | Label |
|---|---|---|---|
| not applicable | It is not a check result | The evaluator in force has decided, from its declared scope, that the check does not apply | **Required** |
| unavailable | Never | Evidence or capability is missing | **Required** |
| invalid | Never | Evidence failed verification | **Required** |
| verified | Yes | The evidence was verified | **Required** |

- **Required.** The evaluator in force works out applicability from the scope it declares.
- **Required.** No check is suppressed because a worker asks for it to be not applicable.
- **Required.** Neither unavailable nor invalid ever turns into a pass.
- **Required.** If a shared dependency fails, each check depending on it keeps both its unavailable state and its behavioural tests.
- **Suggested.** A failure in a shared dependency should be explained by one causal diagnosis rather than by one per dependent check.
- **Required.** An authorised role that is not the author decides which other run authorisations are independent of a failure.
- **Required.** A compromise of a shared host, credential, recorder or evaluator can extend the stop to every lane that relies on it.
- **Required.** Once authority is withdrawn, or turns out to be genuinely invalid, anything depending on it is stopped on the spot.
- **Required.** If the sandbox cannot provide a boundary that the work needs, that work does not run.
- **Required.** Without verification of acceptance, both the matching acceptance claim and the action relying on it are blocked.
- **Required.** When a remote lock cannot be verified from a local machine, that machine may still go on with local work that has its own separate authorisation.
- **Required.** Anything relying on that check is put on hold, and the hold records exactly what is absent.
- **Required.** A stand-in for a signature line is never accepted.
- **Required.** At every boundary, check afresh the expiry, revocation, fresh activation, the action's real scope and its side effects.
- **Required.** An unchanged immutable digest or signature computation may be reused when doing so is safe.
- **Required.** Approval decisions are never cached, and a single-use sign-off is never used a second time.
- **Required.** Approval for a waiting action is tied to its expiry, its scope, the candidate and the action itself, and is spent after one use.

## 6. Dividing decisions between owner and agents

The owner's part:

- **Required.** The owner signs off on an overall budget, an expiry, the resources and side effects that are allowed, the constraints that must be protected, and the intended outcomes.
- **Required.** Authors never approve what they produced.

The agents' part:

- **Required.** Inside the approved scope, agents are free to choose an implementation plan and keep revising it, break the job into pieces and hand those to workers they are allowed to use, fix what fails, and write development tests.
- **Required.** An implementation step missing from the run authorisation may still proceed if it uses only capabilities already permitted and keeps the approved commitments.
- **Required.** Inside an existing run authorisation, the chief clerk (the coordinating agent) may shift work and unused allocations from one worker to another.
- **Required.** Such a shift leaves in force the shared total caps, host refusals, quota holds, organisation controls, minimum quality in routing, and the independent checks that are required.

What stops, and what does not:

- **Required.** An action that relies on something unresolved halts. That covers four cases: a conflict of authority nobody has settled, a change to reserved material, an outward effect missing from the list, and a capability missing from the list.
- **Required.** Work that is independently authorised keeps going while that dependent action is stopped.
- **Required.** Each of these blocks whichever action relies on it: an outward effect that needs approval, a cap, a change to reserved material, an unapproved destination, or a host refusal. Meanwhile, ordinary in-scope development, testing and review keep going.
- **Required.** Citing a requirement or a class does not let a worker enlarge its run authorisation.
- **Required.** The mechanical boundaries are enforced in code: expiry, the identity of the source, budgets, the permitted classes of action, and the paths a worker may write.
- **Required.** A passing test, a record that validates against its schema, or a model label adds no authority by itself.

Judging fit:

- **Required.** The author puts forward the engineering approach. A reviewer who is independent of the author judges whether it fits semantically and whether behaviour is preserved, before acceptance and before any dependent shared action.
- **Required.** Decisions with consequences keep the evidence behind them and receive the independent review they call for.

## 7. Who acted, who approved, and how records are corrected

Approvals:

- **Required.** The owner gives approvals only by way of the protected mechanism that was adopted, and each approval names its limits, its expiry, a revision, and either one action or a standing scope.
- **Required.** An agent may never act as the owner, whether by drafting sign-offs in the owner's name or by setting locks as if it were the owner.
- **Required.** An instruction the owner gives in the current session steers work within existing run authorisations. High-value, irreversible and shared actions still need their protected approval event, and a live instruction cannot stand in for it.
- **Required.** A lock pins exact files, with their hashes, to an owner sign-off received over an authenticated channel.
- **Required.** Nobody invents a prospective approval for work already finished; a record made after the fact is labelled truthfully as retrospective.

Identity:

- **Required.** Who someone is gets read from the authenticated CI, code-host and launch logs already kept.
- **Required.** Every run is tied to its parent task, source revision, execution session, assigned role, attempt and run.
- **Required.** For shared actions there are four more bindings: whichever approval applies, the candidate's digest, the action itself, and the authenticated principal.
- **Required.** Pull-request prose, text that looks like a signature, and git author and email fields are claims.
- **Required.** If nobody recorded which model version ran, or which identity the platform saw, the record says unknown for that value.
- **Required.** When an app logs an action, that log entry alone cannot tell you which of its child workers performed it.
- **Required.** A principal shared across CI or an app shows who executed; telling individual workers apart takes records from a trusted launcher.
- **Required.** The protected recorder is closed to workers.

Trying identity out:

- **Required.** No live action happens until a trial on the real platform has shown that the identity and approval bindings it relies on function.
- **Required.** In its first form, the stub replay may stand in for protected events with fixed, repeatable stubs, and all it can prove is that the rule logic is right.
- **Required.** The stub replay can run without setting up a scratch organisation, an identity service, a key for each agent, or any new account.
- **Required.** If keys come into use at some later point, they stay with a trusted signer, out of workers' reach for both reading and writing.

Correcting records:

- **Required.** Accepted audit records are corrected only by appending.
- **Suggested.** Any other signed record is corrected by appending as well; only operational notes may be edited in place, and their earlier versions are kept.
- **Required.** Operational notes can be fixed in place, as long as their history is kept.
- **Required.** A proposed record's content is validated from its final candidate, keeping incident history where real effects or leaked secrets make it relevant.

## 8. Changing the mandate, and recovering from failure

### Failure and recovery

- **Required.** Before a state-changing action is retried, any external outcome that is unknown is reconciled.
- **Required.** Where the run authorisation allows it, an authorised worker rolling back edits of its own that nobody else has seen may treat that as routine recovery.
- **Required.** Destroying evidence, deleting other people's output and rewriting shared history each keep their own authorisation requirements.
- **Required.** If the same failure keeps coming back, either the diagnosis changes or a different permitted approach is tried.
- **Required.** Unchanged work is never retried without limit.
- **Required.** A reviewer is never replaced in order to obtain an approval.
- **Required.** A host refusal is never bypassed.
- **Required.** A quota hold is never routed around.
- **Required.** Nothing is discarded that records a failed try or an unfavourable review.
- **Required.** Ahead of building anything, a named share of the run's overall money is set aside for checking the result.
- **Required.** Allocations, targets for review rounds and the preferred size of assignments may be adjusted, but never past the bounds that were approved.

### Amendments and the source of authority

- **Required.** A minor mandate amendment states: when it takes effect; the dependencies; the interfaces, paths and requirements it touches; why it is made; the exact clauses it changes; and the revision it amends.
- **Required.** When an amendment is switched on through an authenticated channel, that switch reaches exactly the scope the amendment names.
- **Required.** The amendment yields a new mandate revision. Unchanged documents need not be copied again because of it, and the product does not need a new version just because of it.
- **Required.** A large shift in scope can still call for planning afresh.
- **Suggested.** A scoped, authenticated amendment leaves substantial scope under the product's own versioning rules.
- **Required.** Code checks where an amendment and the work explicitly overlap.
- **Required.** Where the effect on dependencies is unclear, an authorised reviewer or chief clerk who is not the author decides it.
- **Required.** Whoever judges that effect may not rewrite reserved commitments, enlarge a run authorisation, or sign off its own affected work.
- **Required.** Work whose exposure to an amendment is not yet settled stays pending or affected; run authorisations that are independent remain usable.
- **Required.** Everyone works from the same single account of who may do what, backed by the protected source already in place.
- **Required.** A proposal still awaiting a decision, or a chat log pasted in from elsewhere, can never make itself binding.
- **Required.** What was approved is held exactly, either as a canonical snapshot or through a protected immutable reference that already exists.
- **Required.** An authenticated immutable identity cannot be replaced by a branch head that moves.
- **Required.** Nothing in this charter calls for an extra service to store artifacts.
- **Required.** Drafting a candidate change to a verifier or guard is open to agents, but the version currently enforcing stays protected.
- **Required.** Promoting a change to a verifier or guard requires its own separate authorisation, after independent review and suitable adverse tests.
- **Required.** No candidate may turn on the rule that approves it.

## 9. The five allowed change kinds

The charter recognises five permission classes, the allowed change kinds.

- **Required.** Every class depends on an existing run authorisation covering the limits, where data may go, the kind of action, the paths that may be written, the repository, and the outcome.
- **Required.** The project's required checks apply whichever class is used.

| Class | Who reviews | Evidence kept | Never touched | Allowed work | Label |
|---|---|---|---|---|---|
| Fixture repair | An independent party | The diff and the checks it affects | Reserved oracle inputs and expected results stay reserved | Repair loaders, formats or development inputs that are outside the reservation | **Required** |
| Doc-link repair | A non-author, unless the rule below allows CI alone | Confirmation that the target is the intended one | What policy means, pins on executable source, references to authority, and normative text | Point an existing link at the right page or anchor | **Required** |
| Dev-test change | Independent review | The diff of the tests, plus proof they catch the fault if that is practical | Reserved acceptance is never weakened or replaced | Add development tests, or tighten how existing ones are set up and what they assert | **Required** |
| Behaviour-preserving speed change | Independent review | Recorded comparisons and the relevant timings | Resource ceilings, security guarantees, effects visible from outside, interfaces and specified outputs | Get closer to the performance target that was approved | **Required** |
| Approved-item fix | A non-author | Evidence of the reproduction or regression, and the affected checks | Reserved acceptance and the approved public behaviour | Put the implementation right, staying within the scope it was given | **Required** |

- **Required.** A doc-link repair needs a non-author's review, except where an adopted policy accepts an independent check beyond the author's power to change, in which case CI on its own is enough.
- None of the five classes alters the run authorisation it works under.
- **Required.** Product code that the tests exercise, in the ordinary way, can still be written to under the run authorisation.
- **Required.** Reserved acceptance covers manifests, configuration, thresholds, grading helpers, expected results, fixtures and named tests.
- **Required.** Reservation is not limited to what an acceptance check names. Any input a check pulls in as an oracle is covered too, even one the run brief never listed.
- **Required.** If nobody can tell where the oracle ends and the product begins, an authorised role other than the author draws the line before any edit is made.
- **Required.** Even an action that fits none of the examples given may be allowed under section 6's broad rule on delegating.
- **Required.** Where an independent review is called for, its job is to confirm that the change fits semantically; it has no power to enlarge authority or to touch a commitment the owner kept for itself.
- **Required.** The dependent action waits while fit is unresolved.
- **Required.** A decision bigger than the authorised role is allowed to make goes up to the owner.

## 10. Team model

This section is Suggested except where a line says otherwise, and it names no vendor and no model.

- **Suggested.** The team model names no vendor and no model.

### 10.1 Records and retention

- **Suggested.** Every run ends with a record anyone can check, stating what was run, on what model, and how each check came out.
- **Suggested.** If the host can, it records its own observations of the run and authenticates them against what the worker produced.
- **Suggested.** The operator decides where run records are stored.
- **Suggested.** For each type of record, how long it is retained is stated. Bulky debugging evidence is held for 30 days unless set otherwise; a small run record stays until the work it informs is gone.
- **Required.** A worker's statements about itself never establish a pass (repeats tenet 12).
- **Required.** An unrecorded model version or platform identity is entered as unknown (repeats section 7).
- **Required.** No agent deletes evidence alone, since deletion is irreversible (repeats S2).
- **Required.** Failed attempts are kept (repeats section 8).

### 10.2 Spending and escalation

- **Required.** Every run carries a total budget, with a portion held back for verification (repeats sections 6 and 8).
- **Suggested.** Hosts able to do so keep a ledger that sets money aside ahead of any launch and any paid call; the set-aside spans every vendor, every retry and every child.
- **Suggested.** Every role names its escalation path: an ordered list of grades or people, any number of attempts (zero included) at each, a person as the last step, and every step written into the run record.
- **Suggested.** When authority is what a problem is stuck on, it is passed to the owner, or to a person already holding the authority needed to settle it.
- **Required.** Escalating gives an agent no new powers (repeats S5).
- **Required.** A host refusal is never bypassed and a quota hold is never routed around (repeats section 8).

### 10.3 Roles, purpose and the arbiter

- **Suggested.** Purpose: the locked statement of the wanted outcome and its motive, plus the reserved acceptance that decides when it is done.
- **Suggested.** Assignment: a single bounded outcome serving one purpose item, carrying a run id.
- **Suggested.** Role: it may ask for capabilities, and it gives none.
- **Suggested.** Post: an enduring identity that holds one role on one project.
- **Suggested.** Grade: a capability class whose name involves no vendor.
- **Suggested.** Model roster: maps each grade to a concrete model.
- **Suggested.** The model roster is the operator's, and it is kept outside the repository.
- **Suggested.** Every role declares which record kinds it writes.
- **Suggested.** Within one assignment, the role that writes the code never also writes the purpose used to judge that code.
- **Required.** A role's declaration never permits editing reserved material, and development tests stay in the permission class meant for them (repeats section 9).
- **Suggested.** The arbiter is named beforehand by the owner and is not an author of the work concerned. If the chief clerk is stuck and the owner stays silent beyond the waiting period the project fixed, the arbiter may decide engineering questions, but only within the run authorisation already granted.
- **Suggested.** Silence from the owner gives the arbiter nothing more than the existing run authorisation already gives.
- **Required.** Having an arbiter changes nothing here: an unsettled conflict of authority still halts the action that relies on it (repeats sections 6 and 9).
- **Required.** The owner is asked when a decision goes beyond what the authorised role may decide (repeats section 9).

### 10.4 Review

- **Suggested.** Each verdict is bound to the exact candidate it judged.
- **Suggested.** Nobody who wrote any earlier attempt may act as reviewer either.
- **Suggested.** Work that locks, plans or rules, and any change to locks or to security, is reviewed on another model whose grade is at least the author's, and on another vendor family if the roster approves one. When reviewer and author share a family, the review records that fact and gives its reasons.
- **Required.** No author signs off what they wrote (repeats section 6).
- **Required.** Negative reviews are kept (repeats section 8).

### 10.5 Model rosters, memory and messages

- **Suggested.** Every role declares a minimum grade, and no roster switch goes below it.
- **Suggested.** Each time the roster is switched, a record notes when and why.
- **Suggested.** If no eligible model is left after a switch, the assignment waits.
- **Required.** A roster switch cannot send work data to any destination lacking clearance for it, and cannot let a role do more than before (repeats S3 and S5).
- **Suggested.** Whatever is ingested or retrieved keeps its trust label, its revision and where it came from.
- **Required.** Summaries, retrieved text, messages and typed entries are unable to create approvals or privileged instructions (repeats S4).

## 11. Adopting and evaluating this charter

- **Required.** Adoption records that the owner accepts delegated engineering with one shared progress table. Three further events each happen on their own: activation by cryptography, adoption by each individual project, and qualification at runtime.
- **Required.** Explicit adoption and locking stay apart. Qualification at runtime stays apart from both.
- **Suggested.** Offering a charter revision stays distinct from those stages.
- **Required.** Whether to take up a charter revision is something each project settles for itself by its own approved process; importing a text switches on no successor charter.
- **Required.** A pin further down the chain stays put when a fresh revision is put on offer, unless someone moves it.
- **Required.** Each project checks how the charter fits, and what migrating would involve, against the contract it has today.
- **Required.** Merely receiving this charter switches on no product amendment and leaves every scoring rubric as it was.
- **Required.** Evaluations that have nothing to do with each other stay independent and keep their information walled off.
- **Required.** Later review may put forward a superseding revision, but never edits the frozen text quietly.

Evaluation:

- **Required.** Begin by evaluating five synthetic cases: a retrospective plan; an edit to a reserved specification made during work; a forged signature; a rule the owner reversed that candidate code still enforces; and lock verification that is unavailable on the local machine.
- **Required.** Live gates and credentials stay untouched while evaluating.
- **Required.** Tests of reservation boundaries include a valid edit to product code and a case in which a golden file is left out.
- **Required.** Saying how something behaves when running requires having watched it happen.
- **Required.** Any live pilot that follows must have an approved scope and be ready in its own right.

Checklist for taking up a charter revision. Work through it top to bottom; no item may start before the one above it is finished.

1. **Suggested.** Check the incoming files: confirm every file of the revision is intact and is what it claims to be.
2. **Suggested.** Name who is affected: write down every consumer that relies on the charter.
3. **Suggested.** Trace the acceptance impact: write down every acceptance mapping the revision touches.
4. **Suggested.** Get a second reader: someone who did not prepare the adoption reviews it.
5. **Suggested.** Pin what is being taken up: record the exact identity of every adopted item.
6. **Suggested.** Switch it on: the adopter's owner activates the revision. This item is never done before items 1 to 5.
7. **Suggested.** Note the result: after activation, the adopter records which conformance level it reached.

Release format:

- **Suggested.** A charter release that spans several files carries a SHA-256 manifest covering all of them.
- **Suggested.** Signatures on a charter release are checked independently through the adopter's own authenticated process.
- The machine-readable charter (`charter.yaml` or `charter.json`) follows charter schema 0.1.

### What this charter does not establish

Adopting the charter checks no runtime enforcement and supplies no outcome of a measured pilot. It does not integrate identity and approval live, does not replay any original incident, does not show that products have adopted it, and does not carry the owner's cryptographic signature.

## 12. Security annex

The annex covers eight control areas: bounded security assessment, synthetic tests of hosts, boundaries for approval and evidence, protected credentials, the broadest-effect rule, automation checks, organisation precedence, and host surveys.

Inside the bounds:

- A job sheet is produced by code, never by an agent. In it the run finds, quoted, everything that bounds it: which repository and branch, which paths it may touch, its caps, the acceptance criteria it must meet, and the digest of every locked input.
- **Required.** Workers have no write access to the acceptance in force, the evaluators, the approval records or the audit history.
- **Suggested.** New spending halts while accounting or price data is unavailable.
- **Suggested.** Input that is malformed goes into quarantine and is never acted on.
- **Suggested.** When a person stops a run, its state is preserved.
- **Suggested.** Leases ensure that the same work never has two live runs.
- **Suggested.** One gate evaluates every lane start, every tool call and every model call, and answers run, refuse or wait.

Hosts and automation:

- **Suggested.** Running a security target needs confinement, resource limits, custodial intake of results and its own authority; no process rule can stand in for these.
- **Suggested.** Before a host is used, the checks it must pass are run against synthetic data alone.
- A trusted host survey captures how the host is set up right now: isolation, credentials, hooks, routes and configuration. A survey grants nothing.
- Kept apart from the host survey, an automation register records, per project, every deployment trigger, bot, CI pipeline and notification.
- **Suggested.** The host survey and the automation register should both be fresh at entry, at each resume, and before any action that relies on them.
- **Suggested.** A changed automation prompts a fresh check. Under the broadest-effect rule an action is classed by what it now triggers, so a plain push that now starts a deployment counts as a deployment.

Enforcement modes, as conformance levels:

- Level 3 is checks on every call made on a qualified host.
- **Suggested.** Unattended work is allowed at level 3 alone.
- Level 2 is checks at merge time.
- Level 1 is an attended process.

Measures:

- **Suggested.** For the bounded mandate, track four measures: the hours between a lock and its candidate; owner actions together with how long they waited; outcomes of host checks; and refusal rates. This text shows no measured gain from the pattern.

## Open questions

- Status of charter 0.1: decision record 0002 adopts it at a fixed SHA-256, but the owner has not said whether it is locked or only agreed. The owner needs to confirm which status holds.
