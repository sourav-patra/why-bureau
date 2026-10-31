# Adapters, hosts, entry checks and qualification

Part of specification 0.1. Status: draft specification; no reference implementation yet.

An adapter links a runtime, meaning a vendor command-line tool plus a model, to the protected host. Only the host decides whether a launch goes ahead, records what happened and enforces the limits. Labels follow the README, and a line with no label describes how a conforming implementation behaves.

## Who decides

- **Suggested.** Nothing but the protected host may let a launch proceed, keep the record or enforce limits; memory, model rosters, role definitions, dispatchers and workers get to make suggestions and no more.
- **Suggested.** Until a security control has faced a hostile test, no implementation is entitled to say the control is effective.

## Adapters

- An adapter reports usage, runs role sessions in a sandbox and lists the models available.
- **Required** (repeats charter section 8). Independent review covers the evaluators, the adapters and the host.
- **Suggested.** The evaluators, the adapters and the host are pinned where workers cannot write, and identified by digest in run records.
- **Required** (repeats charter section 8). A proposed change to a host component has no means of switching itself on; promoting one needs existing protected approval.
- **Suggested.** A proposed change to a host component is qualified on its own, apart from everything else.

## The entry check, with or without a dispatcher

- **Suggested.** Running with a dispatcher and running without one share a single entry contract.
- **Suggested.** Any pick the dispatcher offers is only a suggestion until the host has examined it.
- **Required** (repeats S3, S5 and charter sections 6 and 8). Ahead of each launch, the host examines refusal bindings, quota holds, the minimum grade, the authenticated run authorisation and the role's request, and whether the destination is eligible for the data class.
- **Suggested.** Ahead of each launch, the host further examines the budget ledger and reservations, cooldowns, and task limits that can only tighten.
- **Suggested.** Without a dispatcher, the host works from the same protected state as it currently stands, and records why it ran without dispatch and the evidence for that.
- **Required** (repeats charter section 8). Quota holds and host refusals can never trigger the switch to running without a dispatcher.
- **Suggested.** Other refusals and waits can never trigger the switch to running without a dispatcher.
- **Suggested.** Missing state halts execution. The one way past that halt is an emergency route, and only if a policy authorised beforehand allows that exact route.

Sources: REFERENCES.md entries 10 and 11.

## Conditions for every launch

### Host and authority are current

- **Suggested.** A live launch may go ahead only once every control it asks for has a protected qualification record that passed, and each record matches the exact combination of backend, host, adapter and effective configuration in use.
- **Suggested.** Qualification lapses as soon as something relevant drifts. Execution then waits, as it does when a qualification record is missing, out of date or failed, and nothing is downgraded to get around the wait.
- **Required** (repeats charter section 5). Authority gets a fresh check at three moments: right before the launch, before every resume, and before each effect that goes through the broker; on top of that, expiry keeps being enforced for as long as execution lasts.
- **Required** (repeats charter section 5). If authority has been revoked or has expired, dependent effects stop; if the state of authority cannot be determined, they are held.
- **Suggested.** Revoked or expired authority also brings the affected execution to an end. Having passed an entry check earlier is not enough.

### Operations are idempotent

- **Suggested.** Nothing is started until the record of the launch has been written durably.
- **Suggested.** The authenticated caller and the idempotency key are bound, in one atomic step, to the exact digest of the request and to a single durable operation.
- **Suggested.** A repeat of an identical request returns the existing operation; reusing a key with different content is refused.
- **Suggested.** Once the system is back up, child processes and outside effects are reconciled. Where it is unclear how an operation ended, its state remains unknown, and nothing restarts it on its own.

Sources: REFERENCES.md entries 103 and 104.

### Output is collected through custodial intake

- **Suggested.** A trusted collector touches the worker's sealed scratch area only when every process in the tree has exited, and even then it takes nothing but declared regular files that fit within a size limit.
- **Suggested.** Collection accesses files relative to a descriptor and never follows links. It rejects links, path traversal, files that change while being collected and special files, and it enforces a cumulative byte limit.
- **Suggested.** Publication happens in one atomic step, from a protected staging area, and only for a manifest that has been checked. A failed collection that the run depends on means the run cannot succeed.

## The first runtime

- **Suggested.** Begin with a single runtime driven from the command line, pinned and reviewed like any dependency. The same controls should pass whether the run is attended or not.
- **Suggested.** Run limits stay enforced whenever nobody is watching, and usage estimates offered by a dispatcher, being advisory, never replace them.

## The compliance checker

- **Suggested.** A pinned compliance checker that workers cannot write to validates the grade-only rule, role schemas, minimum grades and sentinels.
- **Suggested.** The checker confirms the host validated rosters and destinations, works out from launch records whether attempts were independent, and holds run records up against bodies, artifacts and the protected records.
- **Required** (repeats charter section 6). Even with complete run records, passing sentinels and valid schemas, a candidate still needs its own independent acceptance.
- **Suggested.** The acceptance is for the exact candidate.

## Sentinels

- **Suggested.** Each role is given at least five and at most twenty sentinel folders under `sentinels/<role>/`; every folder holds a check command whose result never varies, plus the exit code that command should return.
- **Suggested.** Sentinels go through the real adapter and entry path; optional scoring does not replace acceptance.
- **Suggested.** A change to a sentinel is protected just like the control it tests.
- **Suggested.** Both the run record schema (`run-record.schema.json`) and the role schema carry versions.

## Repository interfaces

- **Suggested.** The checks, the review and the grade-only rule are explained in `CONTRIBUTING.md`, while `AGENTS.md` directs readers to the roles and the grades.
- **Suggested.** Building, testing and releasing require no dispatch history, no post archives and no private overlays.
- **Suggested.** Whether a contributor uses a memory of their own, or none at all, is up to them.

## Rendering and entrenched layers

- Rendering yields, per supported runtime, a single approved team definition. To get there it takes the individual, post, project and organisation layers, folds whatever they may set into the operator's model roster, writes out the runtime's configuration, and stores a render digest computed over both the effective inputs and what was written.
- **Required** (repeats charter section 8). Executable configuration of every kind, the role catalogue included, comes only from pinned revisions that were signed off, never from something a candidate has proposed.
- **Suggested.** Entrenched organisation fields are: independence, the permission class, the minimum grade, and an escalation path whose final step is a person.
- **Required** (repeats charter section 2). Loosening an entrenched field is beyond the lower layers.
- **Suggested.** Lower layers can contribute extra roles and constraints.
- **Suggested.** An unattended launch draws on three layers only: post, project and organisation. An individual's layer appears solely in that person's own sessions, and only when they attend them.
- **Suggested.** At entry, a render that includes an individual layer is rejected when execution is unattended.
- **Suggested.** At each entry check and at post start, rendered files are compared with the render digest; drift calls for a hold or a fresh render.
- **Suggested.** Rendered files are produced by the render step; no person and no worker hand-edits them.
- **Required** (repeats charter section 1). Rendering cleanly is not a stand-in for checking authority.
- **Suggested.** Rendering cleanly is not a stand-in for qualifying the host.

## Security model

Each line names a control, the attack it answers, and the boundary concerned.

### Authority, identity and review

- **Required** (repeats charter sections 5, 6 and 8). Approved immutable definitions plus authenticated run authorisations, revalidated at launch, at resume and at every brokered effect with expiry enforced during execution. Answers: a candidate's rules approving themselves, and queued effects relying on revoked or expired run authorisations. Boundary: authority, including long-running authority.
- **Required** (repeats charter sections 6 and 9). An arbiter who holds just the run authorisation already in place. Answers: a manufactured block, or time passing, creating authority. Boundary: the arbiter.
- **Suggested.** An arbiter named beforehand who did not write the work, and who gains nothing from silence. Answers: a manufactured block, or time passing, creating authority. Boundary: the arbiter.
- **Required** (repeats S5). The same run authorisation. Answers: someone faking failures to push the escalation path into handing out more capability, a bigger run authorisation or wider data access. Boundary: escalation.
- **Suggested.** A scoped problem statement, a budget for each round and the protected escalation path, with authority questions going to a person. Answers: someone faking failures to push the escalation path into handing out more capability, a bigger run authorisation or wider data access. Boundary: escalation.
- **Required** (repeats charter sections 6 and 7). Each attempt's identity is derived from the way it was launched, and reviewers are not authors of the work they review. Answers: an author posing as someone else, or approving stale work. Boundary: review.
- **Suggested.** Every review is tied to the candidate digest and the acceptance digest it examined. Answers: an author posing as someone else, or approving stale work. Boundary: review.
- **Required** (repeats charter sections 8 and 9). Locked acceptance, and development tests that stay separate from the criteria that grade the builder. Answers: a builder weakening the criteria that grade it. Boundary: acceptance writes.
- **Suggested.** Verdicts bound to digests and write scope by record kind. Answers: a builder weakening the criteria that grade it. Boundary: acceptance writes.
- **Required** (repeats S2 and charter sections 5, 6 and 7). The host validates expiry, issuer, order digest, assignment, attempt, branch, paths and effects; whatever the app's identity is, it carries no human authority. Answers: a counterfeit or recycled dispatch that tries to borrow the app permissions belonging to a human user. Boundary: the app proxy.
- **Suggested.** Replayed dispatches are turned away, and a push is handed to the broker only when its digest and branch have been verified. Answers: a counterfeit or recycled dispatch that tries to borrow the app permissions belonging to a human user. Boundary: the app proxy.

### Hosts, execution and money

- **Required** (repeats charter section 8). Components are independently reviewed somewhere workers cannot write. Answers: a tampered component that forges records or switches controls off, and live configuration quietly undoing controls that once passed qualification. Boundary: host and adapters, including host drift.
- **Suggested.** Components are qualified in isolation and their digests are recorded, and they are pinned somewhere workers cannot write. Qualified status is tied to one specific combination of backend, host, adapter and configuration, so any change to these holds every launch. Answers: a tampered component that forges records or switches controls off, and live configuration quietly undoing controls that once passed qualification. Boundary: host and adapters, including host drift.
- **Suggested.** The runtime, loader, tokenizer, weights and dependencies are all pinned; provenance and digests are verified ahead of any installation; remote code and hooks that nobody reviewed are banned; a maintained sandbox restricts network and mounts; telemetry is verified; and any change means qualifying again. Answers: malicious runtime or model components running code or exporting data. Boundary: local execution.
- **Required** (repeats charter sections 5 and 8). Unknown outcomes are reconciled, and dependent work waits until its prerequisites are verified. Answers: retrying something still running or something that was refused, building on dependencies that failed, and a race or crash that starts a second state-changing operation. Boundary: failure handling and duplicate execution.
- **Suggested.** Children and side effects get reconciled, and ambiguous outcomes remain unknown. Failure states never merge, idempotency is tied to the caller, and the durable record is written before anything spawns.
- **Suggested.** Dispatch on or off, a single entry contract applies and the host works from one protected state. Answers: turning dispatch off to drop holds or reservations. Boundary: dispatcher-free mode.
- **Required** (repeats charter sections 6 and 8). Hard caps and money set aside for verification. Answers: failures provoked on purpose to burn through money or reviewers' time. Boundary: budget.
- **Suggested.** Atomic, hierarchy-wide reservations. Answers: failures provoked on purpose to burn through money or reviewers' time. Boundary: budget.
- **Suggested.** A broker performs a fixed set of operations, only on artifacts that were verified, and no publishing job contains candidate code; and an atomic manifest, bounded no-follow access to regular files, sealed scratch and a trusted collector. Answers: jobs holding credentials running candidate code, and collection tricked by links, traversal, changing files or special files. Boundary: publication and artifact collection.

### Data, memory and credentials

- **Required** (repeats S1). Credentials sit beyond the agent's reach. Answers: injected text or code reading secrets, sockets, home-folder settings or sign-in files. Boundary: credentials.
- **Suggested.** Sockets sit beyond the agent's reach. Probes confirm that reading and disclosure attempts fail; a narrowly scoped broker outside the agent's environment supplies what the agent needs; and that environment holds only allowlisted variables and has its own isolated home folder and mounts. Answers: injected text or code reading secrets, sockets, home-folder settings or sign-in files. Boundary: credentials.
- **Required** (repeats S3). Inspecting the real provider, account, endpoint and data class for artifact, prompt, cache, retrieval, telemetry and trace data, and stopping the transfer when anything is unknown. Answers: account, endpoint, telemetry or proxy settings exporting data. Boundary: providers and data.
- **Suggested.** Restrictions from operator, project and organisation are combined by intersection. Answers: account, endpoint, telemetry or proxy settings exporting data. Boundary: providers and data.
- **Required** (repeats S4 and charter section 7). Authority stays protected, and an author attribute is only a claim. Answers: observation or retrieval leaking across projects or review destinations, and typed entries, messages or forged authors turning into instructions. Boundary: cross-project memory and memory authority.
- **Suggested.** Provenance carries authentication. Projects and trust zones are kept apart, destination reads are authorised and exports are explicit; authentication and protection are tested with stale sources, supersession, forged authors and poisoned records. Answers: observation or retrieval leaking across projects or review destinations, and typed entries, messages or forged authors turning into instructions. Boundary: cross-project memory and memory authority.
- **Required** (repeats charter section 2). Enforced entrenchment. Answers: layers further down loosening entrenched fields or hand-altering configuration that the render produced. Boundary: rendering and layers.
- **Suggested.** Render-digest checks, individual layers kept out of unattended launches, and holds on drift. Answers: layers further down loosening entrenched fields or hand-altering configuration that the render produced. Boundary: rendering and layers.

### Records and evidence

- **Suggested.** Bindings of body and artifacts that are authenticated and then checked for revocation, applicability and origin. Answers: replays, substituted artifacts or spliced bodies. Boundary: run records.
- **Required** (repeats charter section 8). Adverse records that nothing cites are never discarded. Answers: a clean-up that buries failures or strips away the evidence a decision rested on. Boundary: evidence expiry.
- **Suggested.** Required evidence stays out of deletion. Adverse records that nothing cites stay out as well, because the dry run and the retention index are protected. Answers: a clean-up that buries failures or strips away the evidence a decision rested on. Boundary: evidence expiry.
