# Adapters, hosts, entry checks and qualification

Part of specification 0.1. Status: draft specification; no reference implementation yet.

An adapter links a runtime, meaning a vendor command-line tool plus a model, to the protected host. Only the host decides whether a launch goes ahead, records what happened and enforces the limits. Nothing in this file carries a label; it describes how a conforming implementation behaves.

## Who decides

- Nothing but the protected host may let a launch proceed, keep the record or enforce limits; memory, model rosters, role definitions, dispatchers and workers get to make suggestions and no more.
- Until a security control has faced a hostile test, no implementation is entitled to say the control is effective.

## Adapters

- An adapter reports usage, runs role sessions in a sandbox and lists the models available.
- The evaluators, the adapters and the host are reviewed independently, pinned where workers cannot write, and identified by digest in run records.
- A proposed change to a host component is qualified on its own, apart from everything else, and has no means of switching itself on; promoting one needs existing protected approval.

## The entry check, with or without a dispatcher

- Running with a dispatcher and running without one share a single entry contract.
- Any pick the dispatcher offers is only a suggestion until the host has examined it.
- Before each launch, the host checks the budget ledger, reservations, tighten-only task limits, cooldowns, refusal bindings, quota holds, whether the destination is eligible for the data class, the minimum grade, the authenticated run authorisation and the role's request.
- Without a dispatcher, the host works from the same protected state as it currently stands, and records why it ran without dispatch and the evidence for that.
- Waits, quota holds and refusals can never trigger the switch to running without a dispatcher.
- Missing state halts execution. The one way past that halt is an emergency route, and only if a policy authorised beforehand allows that exact route.

Sources: REFERENCES.md entries 10 and 11.

## Conditions every launch must meet

### Host and authority are current

- A live launch may go ahead only once every control it asks for has a protected qualification record that passed, and each record matches the exact combination of backend, host, adapter and effective configuration in use.
- Qualification lapses as soon as something relevant drifts. Execution then waits, as it does when a qualification record is missing, out of date or failed, and nothing is downgraded to get around the wait.
- Authority gets a fresh check at three moments: right before the launch, before every resume, and before each effect that goes through the broker; on top of that, expiry keeps being enforced for as long as execution lasts.
- If authority has been revoked or has expired, dependent effects stop and the affected execution ends; if the state of authority cannot be determined, they are held. Having passed an entry check earlier is not enough.

### Operations are idempotent

- Nothing is started until the record of the launch has been written durably.
- The authenticated caller and the idempotency key are bound, in one atomic step, to the exact digest of the request and to a single durable operation.
- A repeat of an identical request returns the existing operation; reusing a key with different content is refused.
- Once the system is back up, child processes and outside effects are reconciled. Where it is unclear how an operation ended, its state remains unknown, and nothing restarts it on its own.

Sources: REFERENCES.md entries 103 and 104.

### Output is collected through custodial intake

- A trusted collector touches the worker's sealed scratch area only when every process in the tree has exited, and even then it takes nothing but declared regular files that fit within a size limit.
- Collection accesses files relative to a descriptor and never follows links. It rejects links, path traversal, files that change while being collected and special files, and it enforces a cumulative byte limit.
- Publication happens in one atomic step, from a protected staging area, and only for a manifest that has been checked. A failed required collection means the run cannot succeed.

## The first runtime

- Begin with a single runtime driven from the command line, pinned and reviewed like any dependency. The same controls must pass whether the run is attended or not.
- Run limits stay enforced whenever nobody is watching, and usage estimates offered by a dispatcher, being advisory, never replace them.

## The compliance checker

- A pinned compliance checker that workers cannot write to validates the grade-only rule, role schemas, minimum grades and sentinels.
- The checker confirms the host validated rosters and destinations, works out from launch records whether attempts were independent, and holds run records up against bodies, artifacts and the protected records.
- Even with complete run records, passing sentinels and valid schemas, the exact candidate still needs its own independent acceptance.

## Sentinels

- Each role is given at least five and at most twenty sentinel folders under `sentinels/<role>/`; every folder holds a check command whose result never varies, plus the exit code that command should return.
- Sentinels go through the real adapter and entry path; optional scoring does not replace acceptance.
- A change to a sentinel is protected just like the control it tests.
- Both the run record schema (`run-record.schema.json`) and the role schema carry versions.

## Repository interfaces

- The checks, the review and the grade-only rule are explained in `CONTRIBUTING.md`, while `AGENTS.md` directs readers to the roles and the grades.
- Building, testing and releasing require no dispatch history, no post archives and no private overlays.
- Whether a contributor uses a memory of their own, or none at all, is up to them.

## Rendering and entrenched layers

- Rendering yields, per supported runtime, a single approved team definition. To get there it takes the individual, post, project and organisation layers, folds whatever they may set into the operator's model roster, writes out the runtime's configuration, and stores a render digest computed over both the effective inputs and what was written.
- Executable configuration of every kind, the role catalogue included, comes only from pinned revisions that were signed off, never from something a candidate has proposed.
- Entrenched organisation fields are: independence, the permission class, the minimum grade, and an escalation path whose final step is a person.
- Lower layers can contribute extra roles and constraints; loosening an entrenched field is beyond them.
- An unattended launch draws on three layers only: post, project and organisation. An individual's layer appears solely in that person's own sessions, and only when they attend them.
- At entry, a render that includes an individual layer is rejected when execution is unattended.
- At each entry check and at post start, rendered files are compared with the render digest; drift calls for a hold or a fresh render.
- Rendered files are produced by the render step; no person and no worker hand-edits them.
- Rendering cleanly is not a stand-in for qualifying the host or for checking authority.

## Security model

Each line names a control, the attack it answers, and the boundary concerned.

### Authority, identity and review

- Approved immutable definitions plus authenticated run authorisations, revalidated at launch, at resume and at every brokered effect with expiry enforced during execution. Answers: a candidate's rules approving themselves, and queued effects relying on revoked or expired run authorisations. Boundary: authority, including long-running authority.
- An arbiter named beforehand who did not write the work, who holds just the run authorisation already in place, and who gains nothing from silence. Answers: a manufactured block, or time passing, creating authority. Boundary: the arbiter.
- A scoped problem statement, the same run authorisation, a budget for each round and the protected escalation path, with authority questions going to a person. Answers: someone faking failures to push the escalation path into handing out more capability, a bigger run authorisation or wider data access. Boundary: escalation.
- Each attempt's identity is derived from the way it was launched, and every review is tied to the candidate digest and the acceptance digest it examined. Answers: an author posing as someone else, or approving stale work. Boundary: review.
- Separate development tests, verdicts bound to digests, locked acceptance and write scope by record kind. Answers: a builder weakening the criteria that grade it. Boundary: acceptance writes.
- The host validates expiry, issuer, order digest, assignment, attempt, branch, paths and effects, turns replays away, and brokers a push only for a verified digest and branch; whatever the app's identity is, it carries no human authority. Answers: a counterfeit or recycled dispatch that tries to borrow the app permissions belonging to a human user. Boundary: the app proxy.

### Hosts, execution and money

- Components are qualified in isolation, their digests are recorded, and they are pinned and reviewed somewhere workers cannot write; each qualification is tied to one specific combination of backend, host, adapter and configuration, so any change to these holds every launch. Answers: a tampered component that forges records or switches controls off, and live configuration quietly undoing controls that once passed qualification. Boundary: host and adapters, including host drift.
- The runtime, loader, tokenizer, weights and dependencies are all pinned; provenance and digests are verified ahead of any installation; remote code and hooks that nobody reviewed are banned; a maintained sandbox restricts network and mounts; telemetry is verified; and any change means qualifying again. Answers: malicious runtime or model components running code or exporting data. Boundary: local execution.
- Failure states never merge, children and side effects get reconciled, preconditions are confirmed, idempotency is tied to the caller, and the durable record is written before anything spawns, with ambiguous cases left unknown. Answers: retrying something still running or something that was refused, building on dependencies that failed, and a race or crash that starts a second state-changing operation. Boundary: failure handling and duplicate execution.
- Dispatch on or off, a single entry contract applies and the host works from one protected state. Answers: turning dispatch off to drop holds or reservations. Boundary: dispatcher-free mode.
- Hard caps, money set aside for verification, and atomic, hierarchy-wide reservations. Answers: failures provoked on purpose to burn through money or reviewers' time. Boundary: budget.
- A broker performs a fixed set of operations, only on artifacts that were verified, and no publishing job contains candidate code; and an atomic manifest, bounded no-follow access to regular files, sealed scratch and a trusted collector. Answers: jobs holding credentials running candidate code, and collection tricked by links, traversal, changing files or special files. Boundary: publication and artifact collection.

### Data, memory and credentials

- Tests confirm that reading and disclosure attempts fail; a narrowly scoped broker outside the agent's environment supplies what the agent needs; sockets and credentials sit beyond the agent's reach; and that environment holds only allowlisted variables and has its own isolated home folder and mounts. Answers: injected text or code reading secrets, sockets, home-folder settings or sign-in files. Boundary: credentials.
- Checking the real provider, account, endpoint and data class for artifacts, prompts, caches, retrieval, telemetry and traces; intersecting the restrictions of operator, project and organisation; and blocking the transfer when anything is unknown. Answers: account, endpoint, telemetry or proxy settings exporting data. Boundary: providers and data.
- Partitioning by project and trust zone with authorised destination reads and explicit exports; and authenticated provenance with protected authority, tested with stale sources, supersession, forged authors and poisoned records. Answers: observation or retrieval leaking across projects or review destinations, and typed entries, messages or forged authors turning into instructions. Boundary: cross-project memory and memory authority.
- Enforced entrenchment and render-digest checks, individual layers kept out of unattended launches, and holds on drift. Answers: layers further down loosening entrenched fields or hand-altering configuration that the render produced. Boundary: rendering and layers.

### Records and evidence

- Bindings of body and artifacts that are authenticated and then checked for revocation, applicability and origin. Answers: replays, substituted artifacts or spliced bodies. Boundary: run records.
- The protected dry run plus the retention index, which protects uncited adverse records and required evidence. Answers: a clean-up that buries failures or strips away the evidence a decision rested on. Boundary: evidence expiry.
