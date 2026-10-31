# why-bureau

why-bureau is a method, a charter and a specification for how people and AI agents work together, so that every piece of work can answer five questions: why it was done, how, where, what was done, and by whom.

Version 0.1. Current status: draft specification; no reference implementation yet.

## The problem

Coding agents now write, test and ship real changes. Text can steer them, they keep working when nobody is looking, they pass data to outside services, and the model underneath can change without notice. Teams that hand them work need to know, after the fact, who authorised a change, what it was meant to achieve, which checks judged it, and what actually ran. Chat transcripts and an agent's own report of success cannot answer those questions.

Swapping the model behind an agent should not quietly change what the agent is allowed to do. why-bureau prevents that by treating five things as separate: the lasting post that answers for the result, the role doing the work, the purpose of that work, the capability grade the role needs, and the private model roster that fills that grade. Authority stays with the role and the run authorisation, never with the model, so a model change leaves it as it was.

Acceptance has three independent legs. The host, not the worker, writes the authenticated run record that says what ran. Checks the author cannot edit, the reserved acceptance, must pass. And a reviewer who is not the author judges the change.

## Who it is for

Engineers who run coding agents, alone or in a team, and who want agent work they can trust, audit and hand over.

## How to read this repository

| File | What it holds |
|---|---|
| [METHOD.md](METHOD.md) | The method: safeguards S1 to S5, tenets 1 to 14, and practice guidance. Adopted by decision 0001. |
| [CHARTER.md](CHARTER.md) | The charter: who decides what, allowed change kinds, approvals, escalation and stops, and the security annex. Adopted by decision 0002. |
| [MODEL.md](MODEL.md) | The operating model: elements, layers, roles, grades, failure states, the escalation path, memory. |
| [RECORDS.md](RECORDS.md) | What a run record holds, how evidence is kept and deleted, and how reviews are bound to the work. |
| [POLICY.md](POLICY.md) | Policy rules: role requests, record kinds, the arbiter, roster switches, budgets. |
| [ADAPTERS.md](ADAPTERS.md) | Adapters, hosts, entry checks, qualification, rendering and the security model. |
| [ROADMAP.md](ROADMAP.md) | Prototype steps, their acceptance items, and open questions. |
| [schemas/](schemas/) | JSON Schemas for the role, the run record and the escalation path, with examples and a check script. |
| [decisions/](decisions/) | Decision records that adopt METHOD.md and CHARTER.md, each pinned by its SHA-256. |
| [examples/](examples/) | One worked example on a small made-up command-line tool. |
| [REFERENCES.md](REFERENCES.md) | Public sources. |

Start with METHOD.md for the reasoning, then CHARTER.md for authority. The specification is MODEL.md, RECORDS.md, POLICY.md, ADAPTERS.md and ROADMAP.md together.

### Labels

Every control in the method, the charter and the specification carries a label.

- **Required**: a requirement. In the specification, a Required control names the safeguard, tenet or charter section it repeats.
- **Suggested**: something to trial and evaluate. Only a later revision can turn it into a rule, and no Suggested control is worded as one.
- No label: a definition, a fact, an explanation or an open question.

Adopting these texts does not enforce any of their controls, Required or Suggested. Nothing in this repository enforces them yet.

## Status

- The repository holds design documents, JSON Schemas with a check script, decision records and one example. Adapters, a host and reference code are planned and do not exist yet.
- Not verified: whether any source was signed, adoption in live use, qualification of any runtime, and any present claim about external products.

## Checking the schemas

```
python schemas/check.py
```

The script uses only the Python standard library. Details are in [schemas/README.md](schemas/README.md).

## Licence

- **Required.** This repository is licensed under the Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
