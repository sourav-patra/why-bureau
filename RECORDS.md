# What a run leaves behind

Part of specification 0.1. Status: draft specification; no reference implementation yet.

Every run leaves one permanent run record, in which the host's observations and the worker's claims sit side by side but never mix. This file covers what a run record holds, how review is tied to the work it judges, and how evidence is kept and eventually deleted. A **Required** control names the safeguard, tenet or charter section it repeats; a **Suggested** control is something to trial and evaluate.

## Run records

- Four things are bound by every run record: the run, the host, the authority and the candidate.
- Any change to an input the record binds invalidates the run records that depend on it.
- **Required** (repeats charter section 10.1 and tenet 12). Exit codes, outcomes and commands that a worker writes down are claims until the host observes or checks them independently.
- **Required** (repeats charter section 6). Every run must have a complete run record, but completeness alone never establishes acceptance.
- **Suggested.** The host's observations carry authentication and are tied to two things: the digests of the artifacts as finally produced, and the worker body in canonical form.
- **Suggested.** Run records are small and permanent. The copy that counts is held in protected storage, an append-only database for example, and every other copy refers to it by its digest.
- **Suggested.** A run record links the review, the session log, the purpose item, the attempt, the run and the assignment.
- **Suggested.** Anyone using a run record checks its origin, revocation and applicability, and its body and artifact bindings.
- **Suggested.** Terminal records that conflict, artifacts that were substituted, bodies that were spliced and replays are all rejected.
- **Suggested.** A run record from before a candidate changed cannot show that the changed candidate is accepted.
- **Suggested.** The fields for outcome, checks, usage, revision and identity are kept.

Sources: REFERENCES.md entries 98 to 101.

## Run record fields

Every group below is mandatory.

| Group | Answers | Fields |
|---|---|---|
| scope | Which work? | Purpose item, assignment, reserved acceptance digest, run, parent, attempt. |
| actor | Who did it, on what? | Role, post, grade, execution session, escalation step and round, provider, actual model version, roster revision. |
| launch | Under what authority, and how was it started? | Mandate revision and run authorisation; the dispatcher's pick, or the marker "local (no dispatch)" with an evidenced reason; digests identifying the checker, the adapter and the host; the qualification id and the render digest wherever they apply. |
| artifacts | What went in and came out? | Input hashes and pinned source revisions; the canonical worker body digest; digests of the manifest of artifacts and of the final output; for each piece of evidence, when it expires, whether it is still available, and its digest. |
| observed | What did the host see? | Timestamps; terminal state; the checks the host itself ran, with exit codes; what the host saw of tokens, cost, latency, usage and the status of each tool call; data for authentication and binding. |
| claimed | What does the worker say? | Everything the worker reports about itself (outcome, usage, files it changed, tool calls, checks, commands), every item treated as a claim. |
| review | Who judged it? | A reference to the verdict, the candidate and acceptance digests reviewed, and the reviewer's session and vendor family. |

- Wherever they apply, the qualification id and the render digest are mandatory.
- Usage provenance tells observations apart from estimates and from claims.
- A run record without run ids is incomplete; they are mandatory.
- Validating against the schema checks structure; verifying protected records checks origin and bindings.

The machine-readable form is `schemas/run-record.schema.json`.

## Review

- **Required** (repeats charter section 6). Even an ordinary review needs an identity other than the author's.
- **Required** (repeats charter section 6). A reviewer must not be the author of the candidate, across posts and sessions. **Suggested:** nor of any earlier attempt.
- **Required** (repeats charter section 7). Who the reviewer is gets established from authenticated records of the launch.
- **Suggested.** A reviewer reads the real diff and whatever source it touches.
- **Suggested.** A verdict is tied to the digests of the exact candidate and of the reserved acceptance, and any change to the candidate voids it.
- **Required** (repeats charter section 8). Once a verdict is voided, negative reviews still stay visible.
- **Suggested.** Changes to locks, changes to the security surface, and work at senior grade are reviewed by a model that differs from every author and is never of a lower grade.
- **Suggested.** Another approved vendor family is preferred but not required; an operator with only one vendor marks the review as same-family and records why.

## Retention

What stays, regardless of age:

- **Required** (repeats charter section 8). Failed attempts, negative reviews, and any evidence needed to make sense of a failure or to reproduce it are protected whether anything cites them or not, and they stay protected after a later success.
- **Suggested.** Keep cited material and the evidence that qualification, acceptance and audit need; for adverse records this is **Required** (repeats charter section 8).
- **Suggested.** Evidence that a decision, lock, incident or open issue cites stays available.
- **Required** (repeats S2). Audit records of shared or irreversible actions keep whatever period the adopted policy requires, and the default 30-day retention cannot cut it short.
- **Suggested.** Run records never expire. Unprocessed evidence normally lasts 30 days, unless the dry run, the retention index (after its references are resolved) or any other safeguard in this section says it must stay.

How long the rest is kept:

- **Suggested.** Scratch trees, test outputs, logs and transcripts are held under their digest for 30 days, a figure each project using this model is free to configure differently.
- **Suggested.** The default 30-day retention also covers superseded draft revisions: the final revision stays with its reviews, and older revisions go only once the safeguards for audit material, for records of failure and for anything referenced have been applied.
- **Suggested.** Memory records are classified before any deletion policy for evidence or run folders is applied.
- **Suggested.** If a recall note quotes a source that is about to be removed, then either the summary preserves the quoted words exactly, or the note is pointed at the summary after its provenance has been checked.
- **Suggested.** The protected sweep must first establish that no adverse record has gone missing, lost any of its contents or become unreadable; until it has, surplus payloads kept for debugging do not expire.

What a deletion leaves behind:

- **Suggested.** Run records keep their digests, and payloads that were deleted are clearly marked unavailable.
- **Suggested.** A digest proves identity. It proves nothing about whether deleted content is available or complete.
- **Suggested.** No summary or digest may stand in for evidence that audit, qualification or acceptance depends on.

Who may delete:

- **Required** (repeats S2). Deleting evidence is never a worker's job.
- **Required** (repeats S2). Workers have no ability to edit the retention index and no ability to delete evidence.

The records sweep, step by step:

1. **Suggested.** Once retention runs out, a protected records sweep starts by listing, as a dry run, what it would remove, and resolves the references; nothing is deleted at this stage.
2. **Suggested.** Next the sweep compiles a protected retention index out of decisions, locks, incidents and open issues, following each supported link and each typed-entry attribute (the literal keys `@file`, `@digest` and `@author`) to the evidence behind it.
3. **Suggested.** Last, the sweep writes a brief summary of the eligible raw evidence, giving the key measurements, its digests, how it ended and what ran, places that summary in a version-controlled store reserved for such summaries, and only after that deletes raw files, limited to those that are eligible.

- **Suggested.** If a reference source is ambiguous, unreadable or missing, the evidence it affects is not deleted.
- **Suggested.** The retention index records deletion eligibility, the reasons for protection, the resolved evidence digests, and the reference sources with their revisions.
