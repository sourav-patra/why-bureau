# The why-bureau method

Version 0.1. Current status: draft specification; no reference implementation yet. Decision record 0001 is what put this text in force.

This is the engineering method. It holds five safeguards, which exist to protect people who are not on the team; fourteen numbered tenets, grouped here by theme; and practical guidance arranged by when it applies: before, during and after a run. Labels: **Required** binds this repository; **Suggested** is advice to try and measure; an unlabelled statement is a definition, a fact or an explanation.

## 1. Standing of this method

- **Suggested.** Read most of this text as advice. It sets no deadlines, and nobody audits a team against it; what binds a team is whatever security and compliance policy its own organisation has.
- No record of departures is kept, no item in the method is pinned to a date, and adopting it comes with no deadline.
- **Suggested.** Teams with a trusted way of working, for example a harness repository they share, a skill catalogue they have vetted, or the defaults a vendor ships, can keep it, on condition that section 3's safeguards hold.
- **Suggested.** Where a team departs from the method it may note why in a single line. That note is optional, and nothing is owed without it.
- **Suggested.** If another method does better on the team's own tasks, that method takes priority over this one.
- **Required.** The safeguards are the part that does not bend, because when one fails the harm lands outside the team: on a customer, a colleague, or whoever owns the data. Restricted data falls under S3 and the audit record falls under S2.
- **Required.** Should the organisation's security or compliance rules be stricter, they win; this method never waters them down.
- Taking up the method leaves the host unbuilt and the runtime unqualified. A host is never qualified by a score given to a repository or by having a policy written down, and nothing in these pages enforces itself. Handing a method to someone else needs evidence the receiver holds; assessing a repository cannot provide that evidence.
- Citations make an idea plausible; whether it helps a particular team shows up only in that team's own measurements. Every threshold here is a design choice until it is measured on the tasks of the team using it.

## 2. Vocabulary

- Harness: the whole apparatus that turns a model into an agent: sandbox, checks, hooks, skills, instruction files, tools and loop.
- Instruction file: read into the agent afresh whenever a session opens; `AGENTS.md` is an example.
- **Suggested.** Purpose: agreed before any work begins, and made of three things: the acceptance checks that decide when the work is complete, the goal, and why the goal matters.
- Skill: a folder holding instructions, frequently with scripts, that is loaded only when a task calls for it.
- Tool: whatever an agent can execute, whether that is an API call, a tool on an MCP tool server, a shell command or a script.
- Trust zone: an area within which data may travel freely. For project data, that area is the organisation together with the providers it approved.
- Unattended: an agent that runs unobserved, whether a scheduler started it or it was left going in the background.
- Verifier: something the agent can run to learn if it is done, for instance a linter, a build, tests, or a script exercising the whole flow.

## 3. Safeguards

- **Required.** Five safeguards, numbered S1 to S5, apply everywhere. Each one exists because a failure would hurt people beyond the team that accepted the risk, and because agents are unusual software: steering text reaches them, they hold context, they act while nobody watches, they send data out, and the model underneath them can be swapped.

### S4. No text carries authority

- **Required.** However it is worded, a piece of text confers no authority, since prompt injection remains unsolved.
- **Required.** Comments, messages, tool output, retrieved passages, skills and tool-server descriptions are all data.
- **Required.** A model's label or score grants nothing.
- **Required.** An instruction that arrives from an unpinned location is ignored.
- **Required.** Doing what a message, a file or a tool result says, because it said so, is a breach of S4.
- **Required.** If one agent writes authority into a file, the agent that later reads the file sees only data.
- Protocols for tool access and for messages between agents carry traffic. They never confer approval.

### The two-of-three limit

- **Required.** A single session may combine at most two of: the power to send data out or change state; reach into sensitive data or systems; and input that is not trusted.
- **Required.** Should a task call for all three, either a person joins in or the job is divided across separate sessions.

### S1. Credentials never enter the agent

- **Required.** Neither the agent's context nor its process ever holds credentials, because text injected into a session can carry off whatever is held there.
- **Required.** A typical means: requests leave the agent bare, and a proxy or broker running separately adds the credential on the way out.
- **Required.** A typical means: the agent's shell is stripped of every variable matching `*_CREDENTIAL`, `*_KEY`, `*_PASSWORD`, `*_SECRET` or `*_TOKEN`.
- **Required.** A typical means: every credential is limited to one job and carries an expiry.
- **Required.** A token sitting in an environment variable, on the hope that the agent will leave it alone, does not satisfy S1.
- **Required.** Say so when the agent's tool holds its own login, and never label such a setup with the top isolation grade.
- **Suggested.** As a habit alongside S1, secrets are never written to logs or to memory.

### S3. Project data stays where it is allowed

- **Required.** Project data does not leave the organisation plus the providers it approved. Once data has gone out, it cannot be recalled.
- **Required.** Each type of project data, including anything from which the work could be recognised, goes only to providers and services cleared for that type.
- **Required.** Not once may project data be copied, cached, indexed, summarised, routed or used to train anything outside the organisation plus the providers it approved.
- **Required.** Agents' caches, memory, traces and context never hold restricted data, meaning whatever the organisation so classes, such as regulated health, identity or payment data within the scope set by its compliance owners.
- **Required.** Restricted data may be used only where the people who own security and compliance have put their sign-off on that one specific use in writing.
- **Required.** Swap restricted values for masked ones, tokens or test data.
- **Required.** The reason: material an agent has seen resurfaces later in caches, memory, traces and prompts, quietly multiplying the places restricted data sits, and an injected instruction can pull out whatever the context contains.
- **Required.** A session being attended does not loosen the limits on where project data may go.

### S5. Switching models grants nothing new

- **Required.** A different model never means wider permissions. Fallback logic and dispatchers can put a different model in place without anyone noticing.
- **Required.** Permissions attach to the role and to the sandbox; they never attach to a model.
- **Required.** A fallback model receives no tool the primary model lacks.
- **Required.** If one model declines a task, handing it to a different model needs a written policy that names exactly that move.
- When a model declines on policy grounds, that stands as a refusal; it is no excuse for shopping around for a more obliging model beyond what the adopted policy permits.
- Changing the model changes neither authority nor the minimum quality level.

### S2. Irreversible and high-value actions need a named person

- **Required.** For every action that is irreversible or of high value, a named person is recorded as accountable for it. Classifiers miss things, agents miss things, and the cost reaches beyond the team.
- **Required.** An approval that cannot be checked later is treated as if it never happened.
- **Required.** S2 is met in one of two ways: someone signs off this particular action, or it falls under a standing sign-off. A standing sign-off carries an expiry and a scope and sits in storage agents cannot write to.
- **Required.** Under S2 fall: shipping a release; deploying; deleting; merging to a protected branch; moving money; contacting a customer or a third party; and an agent changing the permissions, schedule, configuration or skills it runs with.
- **Required.** For each irreversible or shared action, a record kept beyond agents' reach, for as long as the organisation retains such records, says which run it was, which agent identity acted, who approved and what happened.
- **Suggested.** In addition to S2, approvals, grants and actions are never cached; only reads are.

## 4. Tenets

The tenets keep their numbers 1 to 14 wherever they appear, so a record citing a number always means the same idea. Here they are grouped by theme, and each ends with the sign an outsider can look for.

### Boundaries and authority

**Tenet 3. Reading is not obeying.**

- **Required.** Because nobody has solved prompt injection, all of these count as data: what tools return and how tools describe themselves, skill text, files, tickets, comments and web pages.
- **Required.** Authority has one origin, a person, reaching the agent over a channel that the host has authenticated.
- **Required.** There is no case in which this tenet is relaxed.
- Sign: authority probes are part of the evaluations, and nowhere in the code does text from a ticket, a file or a tool's output get run as a command.

**Tenet 4. Bound the reach, not each step.**

- **Required.** Restrict what is possible at the edges (credentials present, hosts reachable, files writable) rather than approving steps one by one; anyone asked to approve every single step quickly stops reading before approving.
- **Required.** When nobody is watching, the protection that works is a sandbox in which the harmful action cannot be taken.
- **Required.** When someone is watching, the host's permission settings together with the operating-system sandbox usually suffice.
- Sign: you can find in version control permissions that default to deny, the list of allowed outbound destinations, and the container definition or sandbox profile.

**Tenet 6. Smallest kit, smallest context.**

- **Required.** Hand over no more tokens, files, tools and permissions than the job truly requires.
- **Required.** Nothing is scarcer than context. As the window fills, the model remembers less, and each extra line dilutes the attention the others get. So keep data only while it is needed, use short-lived scoped credentials, enable few tools and keep instruction files short.
- Sign: a written rule on retention, scoped credentials, a handful of enabled tools, and a short instruction file.

**Tenet 13. Use maintained tools before building one.**

- **Required.** Before writing anything yourself, reach for a tool the organisation has approved, fix its version, and configure it safely.
- **Required.** Write your own only when no configuration removes the risk, as when the licence rules the use out, the telemetry cannot be turned off, or data would end up somewhere beyond the organisation plus the providers it approved.
- **Required.** Sandboxes and cryptography are never home-built. What the platform ships is more robust, and homemade versions break silently.
- Sign: each dependency appears in a list with the version it is pinned to and the safe settings it uses, and every component made in-house names the risk that justified building it.

### Proof

**Tenet 5. No autonomy without a check.**

- **Required.** An agent earns autonomy only once it has a check to run that it cannot easily cheat, for instance a script that exercises the whole flow, a build or a test suite. Only what can be verified can be delegated.
- **Required.** Without a check, the only signal is that the work appears finished, and agents claim success too early.
- **Required.** Where the outcome is hard to check (judgement, taste, design), a person stays involved and the work is never left unattended.
- Sign: CI displays the outcome of the verifier the agent runs, and the agent has no power to alter the tests used to judge it.

**Tenet 12. Results are observed, not announced.**

- **Required.** The result is whatever a record id, diff, test result or exit code establishes; an agent announcing that it has finished counts for nothing.
- **Required.** If a run produced nothing, its ending is failed or blocked; done is not available to it.
- Confidence weighs less than a result someone else can reproduce.
- Sign: alongside each result sit exit codes, test output or diff hashes, and one test exists purely to show that an empty run finishes as failed.

**Tenet 10. A second pair of eyes.**

- **Required.** Review is done by a separate checker with a fresh context: a different agent, a different person, or a test outside the author's control. Humans and agents alike overestimate what they themselves produced.
- **Required.** For code, and for anything built from code, the builder of a change is never its approver.
- Sign: every review is carried out by a test, agent or person other than the author, and is recorded.

**Tenet 1. Trust what you measured.**

- **Required.** Let results on your own work decide which practices to adopt, and demand firmer evidence the more is at stake. No two agent runs behave quite alike, and feeling fast proves nothing.
- **Required.** Small, inexpensive changes that can be rolled back are simply tried out; watching what happens takes the place of any study.
- **Required.** If a change reaches into other teams' setups, into customer data or into production, it is trialled both with and without the change before anyone adopts it.
- Sign: each piece of the agent setup either has evaluation results or carries a note saying why it stays.

### Code over prose

**Tenet 2. Code makes the decision.**

- **Required.** Whatever a rule can settle goes into code that can be tested, because models slip on policy, bookkeeping and arithmetic.
- **Required.** Model output is only one input to the code that decides, and it is parsed against a schema before it is used.
- **Required.** Exploratory or creative work may relax this tenet, provided a person makes the call.
- Bookkeeping, deterministic policy and state transitions are code, not something left to agents.
- Sign: decisions that change state are made in tested code, and nothing a model outputs is used before a schema has parsed it.

**Tenet 8. If it must always hold, make it run.**

- **Required.** Put every rule that must hold without exception into something that runs, such as a CI step, a hook, a linter, a test, a schema or a guardrail that blocks.
- **Required.** Instruction files only advise, and the fuller the context, the weaker their pull.
- **Required.** When a lint rule fires, its message should tell the reader how to fix the problem.
- **Required.** If a check could catch what an instruction-file line describes, the line moves out of the file and into the check.
- Sign: rules that would otherwise sit in the instruction file live in CI jobs, linters or hooks, and their messages include the fix.

**Tenet 11. Write state down durably.**

- **Required.** Put state that must outlast a crash or carry into a fresh session somewhere durable, be that git, a task ledger, a progress file or an event log. Each session starts with nothing, and a container that is lost takes its contents with it.
- **Required.** Every retried piece of work is tagged with an idempotency key, so that after a restart it is neither dropped nor done again.
- Sign: the repository's history contains an event log, ledger or progress file, and idempotency keys travel with work that gets retried.

### Staying lean

**Tenet 7. Grow structure only when it repays its cost.**

- **Required.** Structure grows in this order: a single call, a fixed workflow, one agent, several agents. Each step up must repay what it costs.
- **Required.** Move up a step only when a measurement at an equal token budget shows the step beneath falling short. Adding agents burns extra tokens, and frequently it is those tokens, not the extra agents, that made the difference.
- **Required.** Multiple agents are worth it for pieces that really are independent and that a strong verifier can judge; most day-to-day work is not like that.
- Sign: whenever a design uses several agents, a one-agent baseline exists for comparison, run with an identical number of tokens.

**Tenet 9. Scaffolding expires.**

- **Required.** Every harness part, whether an extra review step, a hook, a skill or an instruction line, is a bet on some gap in what the model is able to do by itself.
- **Required.** When a new model arrives, retest the harness and throw out whatever has stopped paying off. Props built around a weaker model waste tokens and may hamper a stronger one, and a better model arrives every few months.
- **Required.** The safeguards are exempt and stay in place, because they protect people instead of compensating for the model.
- Sign: each skill, hook and instruction line is marked with the model and the date it was last tested against, and some of them get removed as models change.

**Tenet 14. Count what was accepted and stayed.**

- **Required.** Measure outcomes that were accepted and remained stable, not the amount produced. Agents increase output, and the cost surfaces as review time, instability and defects.
- **Required.** Throughput alone is not enough: also follow how long each change takes to review, how often changes fail, how many defects escaped, and how many changes were accepted.
- **Required.** Build delivery on the assumption that review is the bottleneck.
- Sign: next to the number of merges, reports show how often changes failed and how long review took per change.

### Ideas without a number

Some ideas have no tenet number and live in the guidance: measuring every axis, admitting changes strictly and reporting what went unmeasured (sections 7.1 and 7.2); local, open tools as the default (section 5.5, within the limits of S3); memory (sections 5.2 and 6.1); keeping cached data fresh (section 6.4); turning feedback into tests (section 7.4); and the same authority for every model (S5 and section 5.6).

## 5. Before a run: shaping the setup

### 5.1 Instruction files and context

- **Suggested.** Treat context as money: spend it only on what the agent could not work out on its own.
- Research on context degradation (reported, not reproduced here) found that information placed in the middle of a long context lost more than 30% in accuracy, so where a line sits matters as well as whether it is there.
- **Suggested.** Keep the always-loaded instruction file brief. It points to documents, like a map, and is not a manual.
- **Suggested.** Put in the instruction file only project facts that are not obvious. Auto-writing an overview of the entire repository raises cost and does nothing for success.
- **Suggested.** The instruction file settles conflicts by naming whose guidance wins, for instance that a person's instruction outranks a skill's.
- **Suggested.** Track a short instruction file, free of private paths, in the repository as you would code. Keep private notes and handoffs out of it.
- **Suggested.** Cut the instruction file back regularly, as you would code.
- **Suggested.** Test the instruction file the way any change is tested: compare a handful of real tasks with a section present and with it removed, and drop sections whose absence changes nothing.

### 5.2 Memory

- **Suggested.** For short work, rely on whatever memory the host provides, or on none. A memory of your own is warranted only when the work demands it.
- **Suggested.** A home-grown memory lives inside the trust zone, and one interface handles all its reads and writes.
- **Suggested.** Every stored memory keeps its source's exact wording. On each read, code confirms the quote is still in the source, and the memory goes once the source is altered or gone.
- **Suggested.** Memory holds no restricted data, credentials or secrets.
- **Suggested.** Stored text counts as data; even a passage that sounds like an order is never handed to an agent as part of its briefing.
- **Suggested.** A removed memory can be restored. Only a person makes a deletion permanent.

### 5.3 Checks around actions

- **Suggested.** Guardrails live in code: the model suggests, and the application decides.
- **Suggested.** Let a classifier raise flags if that is useful, but make sure a second control that is not a classifier also guards each request before it turns into an action.
- **Suggested.** Before a classifier gates anything, measure how often it misses and how often it raises false alarms.
- **Suggested.** Check at every tool boundary, not only where a multi-agent flow begins and ends.

Where checks sit, from the action backward:

| Check point | What it requires | Label |
|---|---|---|
| Action, any class | A result that can be checked, an approval when the class calls for one, the policy, and the action class. | **Suggested** |
| Irreversible or high-value action, such as a release, a deploy, a delete, a merge to a branch under protection, moving money, contacting a customer, or the agent altering its configuration, permissions, schedule or skills | A named person signs off on it (S2). | **Required** |
| Write that others can see or that leaves the agent's own branch, for instance a posted comment, a new pull request or a pushed branch | A record, a policy check, and review by a non-author before merge or publication. | **Suggested** |
| Reversible internal write: an edit on a branch the agent owns | A checked result, a sandbox and a policy check. | **Suggested** |
| Read, such as a file read or a service query | A policy check and a log entry. | **Suggested** |
| Output | Harm wherever people will read the output, policy, sensitive data, and schema validity. | **Suggested** |
| What enters the prompt | Restricted data only on the terms S3 sets; secrets never; and nothing sensitive at all when the prompt is headed for a provider without approval. | **Suggested** |
| Input | Whether the input shows signs of injection, what trust labels its origins carry, whether it fits its schema, and whether the requester is known; personal and restricted data are redacted before anything else happens. | **Suggested** |

- **Suggested.** An action stopped by a rule is a state to report, not a fault to try again. Instead the task pauses, says which rule got in the way, and stays paused until a person answers over a host-authenticated channel.
- **Required.** Text inside a message or a file that says something is approved is not an approval.
- **Suggested.** Turn away any tool built to answer, suppress or pre-approve the permission prompts the host itself raises.
- **Suggested.** Keep purpose and acceptance checks where the agent they assess cannot reach them.
- **Suggested.** The agent under assessment may write additional tests of its own.
- **Suggested.** If agreed checks are to change, the change must return to the people or agents who agreed them.
- **Suggested.** Proof that guardrails work: for every action class a test shows its path holding, and a fixture containing a planted instruction provokes nothing.

### 5.4 Choosing a box

- **Suggested.** Give each agent the tightest enclosure it can still work in, and be honest about which enclosure is actually in use.
- **Suggested.** Choose an isolation grade from two questions: is there an agent, and is anyone watching it; and how far can it reach? The four grades, from least to most exposed:
  1. G0, plain automation. What runs is a script or tool touching only its own files, with no agent involved. Network use is either absent or limited to a single declared host that is only read from. The test suite proves this, and one of its tests must fail the moment anything calls a different host.
  2. G1, supervised. Someone is at the screen. Whatever the host's permission settings do not explicitly allow is refused, and the agent may change files only inside the folder it is working in.
  3. G2, alone and nearly offline. Nobody is at the screen, and the only things within reach are the model and source control that can be read but not written. Isolation comes from four separate measures. Each run is given a private copy of the repository on a branch nobody else uses. The operating system or a container makes it impossible to change files outside that private copy. Environment variables that hold credentials are removed before the agent starts. When the run finishes, the private copy is thrown away.
  4. G3, alone with reach. Nobody is at the screen, and the agent may open connections to other machines, push commits, or hold a credential. Everything required at G2 still applies. On top of that: outbound traffic is allowed only to destinations on an approved list or through an approved gateway; a broker, not the agent, supplies credentials; the platform, not the agent, says who the agent is; any token lives briefly and works only for that run; and changing what the agent can reach triggers a policy check.
- **Suggested.** Both kinds of limit are needed: without a filesystem limit the agent leaves its folder, and without a network limit keys leak.
- **Suggested.** Rely on a sandbox the platform supplies (an OS sandbox, a container, a VM or a vendor's cloud sandbox). Never write one.
- **Suggested.** No agent keeps production credentials on hand. If a task truly cannot proceed without production access, that access leaves a log, is narrowed to what the task needs, expires, and is handed out for that one task.
- **Suggested.** Telemetry in any tool used for organisation work stays off, and someone verifies that, unless the organisation has approved the place it reports to.
- **Suggested.** Maintain a register of all the places code, traces and prompts are sent to.
- **Suggested.** Every so often, attack your own sandbox: hide an instruction somewhere, try getting a permission change through review unnoticed, impersonate another identity, connect to a host nobody approved, or try reading a secret. Write down what was stopped.

### 5.5 What to build, and vetting what you install

- **Suggested.** Plugins, skills and tool servers are prompt and code, and their descriptions and text act like code that runs. Treat them as you treat dependencies.
- **Suggested.** When choosing a plugin, skill, tool server, script or gateway to install, start from one that runs inside the organisation and whose source the team can read. Reach for a hosted or closed one only when nothing of that kind does the job, and then only from a provider S3 allows.
- **Suggested.** Prefer the lowest rung that does the job over building anything higher. Seven rungs, cheapest first, each with the reason to add it and the sign that it can go:
  1. Bare model. Add: start here, because the model may manage unaided. Retire: never; there is nothing to take away.
  2. A line of instruction. Add: for a project fact nobody would guess. Retire: once runs with and without the line come out the same.
  3. An automated guard, such as a schema, hook, linter or test. Add: for something that has to be true on every run. Retire: once the thing it guards has gone.
  4. A helper script. Add: for mechanical work the model gets wrong or does slowly. Retire: once it sits unused through a model change.
  5. A skill. Add: for know-how about a procedure or a domain that the model lacks and needs only now and then. Retire: once it brings no gain, or hurts tasks the model managed without it.
  6. An agent role of its own. Add: for work that keeps coming back and needs its own permissions, context and tools. Retire: once one general agent matches it.
  7. Several agents in a workflow. Add: for pieces that are worth the tokens, have a strong verifier and are truly independent. Retire: once some lower rung matches it.
- A dedicated agent is worth scoping as soon as recurring work needs one of these: its own permissions, its own tools or its own context. Rung 6 above asks for all three together.
- Fine-tuning comes only after the three cheaper means (retrieval, skills and instructions, in any order) have hit a limit that was measured.

Writing skills:

- **Suggested.** Keep a skill short and on one subject, limited to knowledge or behaviour the model would not show unprompted. Generic advice stays out.
- Each skill is about a single procedure or a single domain.
- **Suggested.** A skill's description explains its purpose and the moment to reach for it; where skills cover neighbouring subjects, each also spells out when to leave it alone.
- **Suggested.** Before anyone else relies on a skill, a person reads all of it. Skills an agent writes for its own use and nobody checks usually do not help.
- A skill drafted by a model has no standing until it passes its checks.
- The persona a skill gives the model is no evidence of accuracy or of authority.
- **Suggested.** Run a handful of real tasks twice, once with the skill and once without, and tally the tasks it hurt alongside the ones it helped.
- **Suggested.** Note the model a skill was tested with; test again after a model change, and retire the skill once it no longer helps.

Scripts inside skills:

- **Suggested.** Skill scripts run inside the sandbox.
- **Suggested.** Bad input must make a script fail loudly; it never exits as a success after doing the wrong thing.
- **Suggested.** Skill scripts never take credentials from environment variables.
- **Suggested.** No skill script changes an agent's hooks or configuration.
- **Suggested.** Skill scripts never pull instructions from a location that is not pinned.
- **Suggested.** No skill script downloads code and executes it.
- **Suggested.** For each script, say whether its effect can be undone, which environment variables it expects, which hosts it calls, and what it reads and writes.

Installing from outside:

- **Suggested.** Dry-run or read an installer first. Trust anchors, agent configuration and agent hooks are never added, edited or written by anything that has not shown that first.
- **Suggested.** Accept a hook only if uninstalling it leaves nothing behind, and it never calls a model, opens a network connection or pipes into a shell.
- **Suggested.** Pin every external server, plugin or skill to a version, and review it again on every change, because behaviour can shift after approval.
- **Suggested.** Before installing anything external, read its licence and also the terms of every service it calls on.
- **Suggested.** Starting from a shared catalogue is fine, but vet whatever you pull in; an item being widely used tells you little about whether it is safe or right for you.
- **Suggested.** Keep an inventory of what is installed (owner, item, version, last review) and use traces to watch how each item really behaves.
- **Suggested.** Load only the skills a task needs, since many skills compete for attention.

Layered configuration:

- **Suggested.** In layered agent configuration (organisation, team, project, individual), the safeguard settings that the organisation sets are entrenched: lower layers can add rules and can never relax the safeguards.
- **Suggested.** Ahead of each run the host takes checksums, stored out of the agent's reach, and compares them with the agent files it generated and with the approved inputs it generated them from.
- **Suggested.** If any checksum disagrees, the run halts, and it stays halted until the approved inputs and the regenerated files pass the comparison.
- **Suggested.** An individual's configuration layer has no effect on an unattended run.

### 5.6 Models and providers

- **Required.** Send work only to providers the organisation has approved, and to each only the data classes its approval names.
- **Required.** Anything sitting in the prompt path, whether gateway, dispatcher or proxy, is approved the same way a provider is; the organisation must run it itself, or else an approved provider must, with a contract that settles how training and retention are handled.
- **Suggested.** Unless configured otherwise, a routing table in code picks the model: a model can put forward labels, but the choice rests with the table.
- **Required.** Routing never shifts authority.
- **Suggested.** Routing never sends work below the minimum quality the role sets.
- **Suggested.** Fallbacks are listed in advance. If a model cannot be reached, whichever model is listed after it steps in; if none is, the work is put on hold.
- **Suggested.** For every role keep a few real tasks as sentinels. Put them through every model family the role relies on, and put them through again whenever a harness setting, the model's version or the model itself changes, because vendors update models quietly.
- Assess refusals separately from instruction following; a refusal tells you nothing about which instructions were understood.
- Pass mechanical jobs to a cheaper grade only where the minimum quality expected of that grade, together with the checks around the work, make the move safe; the stronger models are better spent on planning and on diagnosing hard problems.

## 6. During a run

### 6.1 Sessions and handoffs

- **Suggested.** Give each session a single task.
- Open a new session for each bounded task, naming at the outset its acceptance check and its files.
- **Suggested.** If two corrections have failed, begin again in a fresh session.
- Sessions that run long feel more productive even as retrieval gets worse. Reluctance to pay for a restart pushes a session past its useful context, until it loses track mid-task or leans on its own unverified claim of completion. In the reported research every model tested, 18 of 18, did worse as its input grew, and the decline began near 50K tokens in a 200K window.
- **Suggested.** Hand off references, never contents. What passes between sessions is a brief note saying where things were left, paths and ids; a transcript is never pasted in.
- Keep independent review apart from implementation, and keep restarts cheap with a short handoff that durable evidence backs up.
- **Suggested.** When a job would flood the context, for instance by fetching pages, searching widely or reading long logs, delegate it to a sub-agent whose only output is a brief summary.
- **Suggested.** Tools give back output that is paginated, readable and short.
- **Suggested.** Any project fact an agent asserts comes with its source; lacking one, the agent admits ignorance instead of plugging the hole with whatever its training suggests.
- Before adding instructions to a run that is getting worse, look at what the task asks for, at the context that has built up and at the model grade.
- The weaker the model, the more its result can depend on how good the prompt is. Reported research linked about 53% of quality variance to prompt quality; on the weakest models strategy had roughly four times the effect, while on top models it explained at most 2% of variance.
- Whatever a skill says is carried out by a runtime, so a skill is only as good as the model behind it: a well-built workflow keeps avoidable errors out, yet the ceiling on what the task can achieve is still set by the model's capability.

### 6.2 Coordinating agents

- **Suggested.** Begin from a single agent with a strong verifier. Extra agents come in only for broad research, for a clean review context, or for pieces that are independent.
- **Suggested.** Agents never coordinate by talking to one another; whatever they share goes through durable records.
- An agent learns what to do by following pointers it finds in shared state.
- Agents hand back typed results, never free-form ones.
- State transitions belong to the runtime, not to the agents.
- **Suggested.** A sub-agent whose work rests on earlier decisions receives the complete context.
- **Suggested.** The parent carries on only once all of its sub-agents are done, and it picks up just once.
- **Suggested.** When agents cooperate across a vendor or team boundary, they do so over an open protocol whose task states are explicit, and they never merge the label saying who wrote something with the label saying how far it can be trusted.
- **Suggested.** Background agents on vendor infrastructure get no secrets, submit work as pull requests using their own identity, and are reviewed by someone else.

How a run ends:

- **Suggested.** blocked: always with a reason.
- **Suggested.** unknown: after a crash.
- **Suggested.** done: only when a result can be checked.
- **Required.** An agent's say-so never makes a run done.

### 6.3 Escalation, limits and stopping

- **Suggested.** Agree beforehand the climb a run takes when it keeps failing; for example, further rounds, then a more capable model, then a person.
- **Suggested.** Every escalation step opens with a written account of the problem.
- **Required.** Climbing the escalation path never brings permissions wider than the task started with.
- **Suggested.** If a task is waiting on a decision, a permission or a credential, it is handed to a person, since a model cannot hand itself authority.
- **Suggested.** Code enforces a spending cap and a liveness heartbeat on every unattended run that costs money.
- **Suggested.** Retries are limited in number and back off.
- **Suggested.** Any run can be stopped immediately by a person.
- **Suggested.** A workflow is shown to be durable when a run that is killed halfway and restarted neither loses nor repeats anything.

### 6.4 Cost

- **Suggested.** Compared with chat, a single agent uses several times the tokens and a multi-agent setup many times more; work that cost out before choosing either.
- **Suggested.** Judge spending by what each accepted outcome cost, not by tokens burned in a session, because more tokens do not mean more value.
- **Suggested.** Reach first for the inexpensive levers: a run budget for every unattended job, noisy work given to sub-agents, a single task in each session, tools loaded only when needed, lean instruction files, and a prompt prefix that stays the same from call to call so it can be cached.
- **Suggested.** A cache key covers everything that could alter the answer, and no cache is shared between trust zones, teams or people.

## 7. After a run: checking, learning and delivering

### 7.1 How deeply to check

- **Suggested.** Match the depth of checking to the risk of the change. Brief depth suits an individual's reversible changes, regular depth suits shared setups, and thorough depth suits work that runs without supervision against live systems.
- **Suggested.** At brief depth: judge a handful of real tasks by eye, one run is enough, and simply note the cost. Held-out cases, robustness probes and other models are skipped, and so are safety probes, except when the work takes in text from outside.
- **Suggested.** Regular depth asks for more. Every arm gets five runs or more. A gain counts only on paired cases in which the change helps more cases than it harms, and only if a test such as the sign test says that such a split would be unlikely were the change doing nothing. Results on cases never used for tuning appear in a report of their own. The probes include input sitting on a boundary, input too large, broken input, and no input at all. The work is attacked with probes aimed at injection and at authority. Money and tokens are measured for every task. And the model mainly used is the one put to the test.
- **Suggested.** At thorough depth everything from regular depth applies, plus the following. Every model the work can be routed to is tested. Cost is measured against a ceiling declared in advance. Safety may not regress at all. Robustness is probed exhaustively, and bad input that slips through without an error is scored as a failure. A score that steered which change was picked is called a selection score, and it is not presented as the outcome. Where each arm has had five runs or more, the share of trials in which all runs pass is reported. Finally, measure the spread of the baseline as one standard deviation: a gain counts only when its mean is strictly greater than that figure, so a mean that merely equals it, or falls below it, does not count.
- The following are judgement, and remain judgement calls until data from the tasks of teams using them shows they predict outcomes: the split into brief, regular and thorough depth; the pass thresholds for gain; the count of five runs; the rule on bad input; treating vendor figures as claims; and counting empty answers as failures.

### 7.2 Comparing with and without a change

- **Suggested.** Decide the statistical test and its threshold before running anything.
- **Suggested.** Fix the comparison in advance. A change is measured against whatever it replaces; something new is measured against the identical setup lacking it.
- **Suggested.** Hold the environment constant across both arms.
- **Suggested.** Attribute an improvement to a new design only after comparing at equal token budgets.
- **Suggested.** No arm of a comparison runs with the safeguards turned off.
- **Suggested.** Pit any style rule against a single-line instruction requesting the same behaviour.
- **Suggested.** Run skill tests with and without the skill after every revision and every model change, so that beating an older skill cannot conceal harm compared with the bare model.
- **Suggested.** Count, for each change, the cases that did not move, the cases that got worse and the cases that got better.
- **Suggested.** When nobody is watching, one success is not the bar; all of the runs have to succeed. For example, a task that passes 90% of the time passes ten times running only about one time in three (0.9 to the tenth power is 0.349).
- **Suggested.** An illustration, using the exact two-sided sign test over 15 independent pairs without ties: a 9 to 6 split gives p = 0.607, 11 to 4 gives p = 0.118, and 12 to 3 gives p = 0.035. So with 15 pairs, 12 improvements are the fewest that get under a 5% threshold.
- **Suggested.** A later revision may borrow results from the no-skill arm, or from the one-line arm used for a style rule, provided it can be shown, for example through a model version fixed by its date, that nothing among the following has moved: the model version, instructions, harness settings, cases, tools, grading rules and token budget.
- **Suggested.** Before reusing arm results, write down the numeric limits that force a full rerun, what is measured, how many runs, which cases will run again next to the new arms, and how those cases are picked. A partial check can still overlook changes elsewhere.
- **Suggested.** Old arm results stop counting in three situations, and then every recorded arm runs again in full next to the new ones: nobody can demonstrate that the setup stayed the same; a check has gone past its limit; or the model or harness has changed.
- **Suggested.** New or edited cases get their own runs in each arm.
- **Suggested.** When you publish a result, list what went unmeasured, and do not throw away measurements that failed.
- A good average, or a single demo that worked, is weak support for running work unattended.
- Prefer to copy a method someone has already measured, and then test how well it fits.
- Shortening instructions can help, but stripping out error handling or validation can make the shorter version fail.
- The research numbers given in sections 5.1 and 6.1 are as their authors reported them, not limits that hold everywhere, and none of them proves a gain on your own work.
- The calibration count of 20 for graders is a judgement call, the 5% threshold is a convention, and the one-line-instruction arm and the rule for reusing baseline arms are judgement calls as well.

### 7.3 Grading

- **Suggested.** An evaluation can mislead or be gamed. A strong model can spot that it is under test, and a buggy grader can mask real ability or report ability that is not there.
- **Suggested.** The grading order is fixed: code first, then a person, and a model last, used only for what neither can grade.
- **Suggested.** A model used as a grader sits at a grade no lower than the model whose work it grades, and ideally belongs to another vendor family.
- **Suggested.** No model grades unsupervised until its marks have been set beside at least 20 marks a person gave, with the rate of agreement published.
- In the entry model, models from another vendor family may sit as a jury, but solely on criteria that code cannot judge and a person cannot judge either, and solely after calibration against no fewer than 20 human labels.
- **Suggested.** Sample some transcripts before you believe a score, and if something is off, mend the grader before you touch the agent.
- **Suggested.** A score covers two things, how the agent got there and where it ended up; retain whatever traces record the route.
- **Suggested.** An empty answer fails.
- **Suggested.** To tune grading rules, read what the practice cases produced, keeping those cases outside the scored set, and lock the rules before scoring begins. Those practice cases do not count as held-out cases.
- Freeze the grader before any skill evaluation run.
- Certify the evaluation fixtures as clean before they are used.
- Keep regression evaluations and capability evaluations apart.
- Every change is assigned an entry profile that rates it on seven axes: cost, held-out cases, how well it carries over to every declared model, gain, safety, variation, and robustness.
- Scoring stays at arm's length from the tool that admits changes; whoever scores does not look at that tool's repository at all.
- Scoring runs start without any memory briefing.
- Nor can a scoring run recall anything from memory while it works.
- Admitting a method change and scoring a release are separate decisions.
- Candidates turned down during selection are kept as evidence, including those that passed their checks, and failed runs are kept too.
- **Suggested.** Treat any figure a vendor or a paper reports as a claim, and only as a result once your own tasks reproduce it.

### 7.4 Learning from use

- **Suggested.** Real use is the teacher; whatever it teaches should end up as a test.
- **Suggested.** Watch three kinds of feedback signal: verdicts (approvals, rejections and overrides), repairs (corrections, retries and reverted changes), and abandonment and lessons (runs abandoned and lessons recorded).
- **Suggested.** Feedback can mislead. A rejection may really be caused by a stale source, missing data, wrong retrieval, a poor interface or a tool that failed, so the records are consulted for the cause before anything else.
- **Suggested.** A confirmed defect is captured as a test case before any fix. The case must be seen failing; then the fix goes in; then the case stays in the suite.
- **Suggested.** The first evaluation set is built from 20 to 50 failures that actually occurred, never from made-up ones.
- **Suggested.** Finding a fault, writing its case and drafting the fix may all be done by an agent, but someone else gives the approval.
- **Required.** A fix never widens a permission.
- **Suggested.** The loop is working when every confirmed defect enlarges the regression suite and fewer defects reach production.

### 7.5 Records

- **Suggested.** Everything belonging to a run, from logs and traces to checks, cost, memory reads and approvals, hangs off one run id.
- **Suggested.** Each model call is recorded with these fields:

| Concern | Fields |
|---|---|
| Identity | model and its version |
| Inputs | prompt hash; hashes of the skills and instruction files in use; context size |
| Spend | latency; cost; tokens |
| Behaviour | each tool call and whether it succeeded; errors |

- Every accepted outcome is logged with three facts: the session's age, the tool, and the model. Logging them is required. For the age, four buckets are offered as a suggestion, not a mandate: brand new; past its first task; past several tasks; open for days.
- **Suggested.** Sensitive payloads never appear raw in records; a record holds only their hashes and pointers to them.
- **Suggested.** A run record stays lean: which checks ran and what they returned, what was run and on what model, and hashes covering both inputs and outputs.
- **Suggested.** If quality falls, the records should (this is a recommendation) let you tell whether cost or context size jumped, a tool failed, data went stale, retrieval changed, a prompt or skill changed, or the model changed.
- **Suggested.** Deciding where traces live is a data decision governed by S3, so they are held inside the organisation and the providers approved for that data.
- **Required.** Shared and irreversible actions have an audit trail that is separate from any debugging log, sits where agents cannot reach it, and lasts as long as the organisation requires.
- **Suggested.** Every record type has a set retention period; bulky debugging material, for instance, goes after 30 days.
- **Suggested.** While the work they bear on is still live, failed attempts and negative reviews are retained.
- **Required.** Deleting evidence is treated as irreversible, so an agent never deletes evidence by itself.
- Keep track of later corrective changes, of rework, and of defects found in review.
- Keep what workers say separate from what was observed independently.
- Before any claim about routing or subscriptions, compare review effort and accepted outcomes per task class and per session age. No controlled result backs such a claim yet.

### 7.6 Review and delivery

- **Suggested.** Every change serves a purpose that was agreed and fixed before work began, and review evaluates whether the change fulfils that purpose.
- **Suggested.** If the purpose changes, the change goes back to those, people or agents, who agreed the original.
- **Suggested.** By the time a person reviews a change, linters, static analysis, tests and CI have all already run.
- **Suggested.** The action class decides how deep the review goes.
- **Suggested.** Three kinds of work get a reviewer running a model other than the author's, at the author's grade or above: security changes, plans, and decisions that approve and freeze something; for these that is a must.
- **Suggested.** In those reviews a model from a second vendor family is the better choice where one has approval for the data; where none has, the review notes that author and reviewer come from one family, and gives the reason.
- **Suggested.** Keep changes small, because small ones are quicker to review and easier to revert.
- **Suggested.** Agents imitate the patterns they find, so drift builds on itself; set aside time for regular clean-up.
- **Suggested.** Skills, instruction files, tool-server lists and agent configuration count as code: they live in version control, get reviewed, and change only by the usual process.
- **Suggested.** Delivery is healthy when review time per change and change failure rate stay flat or fall while merged changes grow.
- A release decision keeps three things apart: the owner's approval, the independent review and the checks.
- The release decision stays with the owner.

## 8. Open questions

Signals that would reopen this method, any one of which is enough:

| Signal | Why it matters |
|---|---|
| Someone breaks out of a platform sandbox that was set up the recommended way. | The advice to rely on platform sandboxes would no longer hold. |
| The organisation revises its policies on data, security or compliance. | Those policies always take precedence over the method. |
| A host appears that can verify instructions carried inside text. | Authority could then come from more places than it does now. |
| On the organisation's own tasks, some model generation clearly does better with longer instruction files or extra structure than with a lean setup. | The case for keeping things lean would weaken. |
| On everyday coding, at the same budget, several agents are shown to outperform one. | The case for starting with a single agent would weaken. |

Taking the method to another organisation (proposed, not adopted):

- Decide the cost of each accepted outcome, how rollback works and who owns incidents, and make promotion criteria explicit.
- Get the checks and the recovery reproduced by somebody who did not write them; test that crossings between trust zones are clean; keep local configuration out of the reusable method; and write down the authority and operating assumptions.
- A receiver of the method needs answers to four questions. Can the dependencies actually be obtained? Who authorises work, and which data boundary holds? How is configuration kept apart from the method? What does the receiver need to reproduce acceptance, run the method and recover?
