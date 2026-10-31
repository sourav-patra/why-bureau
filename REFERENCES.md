# References

Public sources behind why-bureau, grouped by topic. Each entry gives the title, the author or publisher, the year when known, the URL or a standard identifier, and one line on what the source supports here.

Status: every source below is reported, not read in full for this repository. "URL checked" means the address was confirmed to resolve. "URL not confirmed" gives the HTTP status received. "No URL to check" means no URL was given; a standard identifier is shown where one exists, and otherwise only the title and publisher.

## How sources are used

- Only your own measurements show that an idea works on your tasks; a citation lends it support and nothing more.
- Each source is listed once, with the parts of why-bureau it supports and whether it was read or only reported. This map is reference material for the tenets and practice sections, not part of the rules.
- Check date for the comparable tools: 27 October 2026. They do related things, nothing more: they may be described and compared, but they back no claim that they are secure or equivalent, and no policy rule ever names one.
- Fit and conformance of a comparable tool can only be judged by evaluating it at implementation level; comparing descriptions proves neither that it meets the combined controls nor that it falls short of them.
- The sign test used in METHOD.md section 7.2 is a standard non-parametric test; the reference values there were computed for the stated case counts.

## Prompt injection, authority and isolation

Why text is data, why capability is limited at the boundary, and how sandboxes and gateways are built.

1. Agents Rule of Two: A Practical Approach to AI Agent Security. Meta, 2025. <https://ai.meta.com/blog/practical-ai-agent-security/> Source of the two-of-three limit; treats all agent input as data and motivates injection and authority probes (METHOD.md sections 3 and 7.1). Status: Reported; URL checked.
2. New prompt injection papers. Simon Willison, 2025. <https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/> Prompt injection has no solution yet, which is why S4 and tenet 3 allow no relaxation. Status: Reported; URL checked.
3. Defeating Prompt Injections by Design (CaMeL). arXiv 2503.18813, 2025. No URL given; arXiv:2503.18813. Separating control flow from untrusted data, the design idea behind S4. Status: Reported; no URL to check.
4. The Dual LLM pattern. Simon Willison, 2023. No URL given; title and author only. Keeping the model that reads untrusted text away from privileged actions, an early form of the two-of-three limit. Status: Reported; no URL to check.
5. OWASP Top 10 for Agentic Applications for 2026. OWASP, 2025. <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/> A public list of agent risks, a source for injection and authority test cases (METHOD.md section 7.1). Status: Reported; URL checked.
6. How we contain Claude across products. Anthropic, 2026. <https://www.anthropic.com/research/how-we-contain-claude> Isolation grades, limits at the boundary instead of per-step approval, and input treated as data (tenets 3 and 4, METHOD.md section 5.4). Status: Reported; URL checked.
7. Making Claude Code safer with sandboxing. Anthropic, 2025. <https://www.anthropic.com/research/claude-code-sandboxing> An OS sandbox with both network and filesystem limits (tenet 4, isolation grades G1 to G3). Status: Reported; URL checked.
8. How we built Claude Code auto mode. Anthropic, 2026. <https://www.anthropic.com/research/claude-code-auto-mode> People who approve every step stop reading, so guardrails sit at the boundary and per action class (tenet 4, METHOD.md section 5.3). Status: Reported; URL checked.
9. Guardrails, OpenAI Agents SDK. OpenAI (documentation). <https://openai.github.io/openai-agents-python/guardrails/> Guardrails written as code at the input, output and action layers (METHOD.md section 5.3). Status: Reported; URL checked.
10. Securing MCP: a control plane for agent tool execution. Microsoft, 2026. <https://developer.microsoft.com/blog/securing-mcp-a-control-plane-for-agent-tool-execution/> One enforcement point for every tool call, like the single gate in CHARTER.md section 12. Status: Reported; URL checked.
11. Amazon Bedrock AgentCore, Policy core concepts. AWS (documentation). <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-core-concepts.html> A policy gateway that checks agent tool calls before they run (CHARTER.md section 12, the single gate). Status: Reported; URL checked.
12. Why Policy in Amazon Bedrock AgentCore chose Cedar for securing agentic workflows. AWS, 2026. <https://aws.amazon.com/blogs/security/why-policy-in-amazon-bedrock-agentcore-chose-cedar-for-securing-agentic-workflows/> Agent policy as declarative, deterministic code (tenet 2). Status: Reported; URL checked.
13. Poisoned Skills: AI Agent Marketplace Supply Chain Attacks. Cloud Security Alliance, 2026. <https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-skill-supply-chain-attacks-20260624-csa/> Marketplace skills as an attack path, supporting approved, pinned and reviewed dependencies and the safeguards (tenet 13, METHOD.md section 5.5). Status: Reported; URL checked.
14. Scaling Managed Agents with stable interfaces. Anthropic, 2026. <https://www.anthropic.com/research/managed-agents> Durable session state behind stable interfaces, with the safeguards kept around it (tenet 11, section 3 of METHOD.md). Status: Reported; URL checked.

## Verification, evaluation and grading

How to know a change helps, and how graders themselves are checked.

15. Demystifying evals for AI agents. Anthropic, 2026. <https://www.anthropic.com/research/demystifying-evals-for-ai-agents> Verifiers before autonomy, checking depth scaled to risk, repeated runs and the all-runs-pass rate, grading the path an agent takes and not only its result, fixing the grader first, and calibrating model graders (tenet 5, METHOD.md sections 7.1, 7.2 and 7.3). Status: Reported; URL checked.
16. Evaluate agent workflows. OpenAI (documentation). <https://developers.openai.com/api/docs/guides/agent-evals> Grading both the route an agent took and its outcome, and keeping the traces (METHOD.md section 7.3). Status: Reported; URL checked.
17. Evaluation best practices. OpenAI (documentation). <https://developers.openai.com/api/docs/guides/evaluation-best-practices> Turning observed failures into regression cases, and calibrating a model grader against people (METHOD.md sections 7.3 and 7.4). Status: Reported; URL checked.
18. Eval awareness in Opus 4.6 on BrowseComp. Anthropic, 2026. <https://www.anthropic.com/research/eval-awareness-browsecomp> A strong model can notice it is under test, so evaluations can be gamed (METHOD.md section 7.3). Status: Reported; URL checked.
19. Infrastructure noise in agentic coding evals. Anthropic, 2026. <https://www.anthropic.com/research/infrastructure-noise> Environment differences move scores, so both arms keep one environment and baselines are reused only when the setup is shown unchanged (METHOD.md section 7.2). Status: Reported; URL checked.
20. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. arXiv 2306.05685, 2023. <https://arxiv.org/abs/2306.05685> Biases of model judges, behind grading by code first, then a person, then a model (tenet 10, METHOD.md section 7.3). Status: Reported; URL checked.
21. LLM Evaluators Recognize and Favor Their Own Generations. arXiv 2404.13076, 2024. <https://arxiv.org/abs/2404.13076> Models prefer text they produced themselves, the reason an author never grades what it wrote (tenet 10). Status: Reported; URL checked.
22. Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models. arXiv 2404.18796, 2024. <https://arxiv.org/abs/2404.18796> A panel of models from different families, behind different-family graders and model juries (METHOD.md section 7.3). Status: Reported; URL checked.
23. Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences. arXiv 2404.12272, 2024. <https://arxiv.org/abs/2404.12272> Grading rules are tuned on a separate practice set, never on the cases being scored, and then locked (METHOD.md section 7.3). Status: Reported; URL checked.
24. HealthBench: Evaluating Large Language Models Towards Improved Human Health. arXiv 2505.08775, 2025. <https://arxiv.org/abs/2505.08775> Before a model grader works unsupervised, its grades are compared with human ones (METHOD.md section 7.3). Status: Reported; URL checked.
25. tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains. arXiv 2406.12045, 2024. <https://arxiv.org/abs/2406.12045> For unattended work every run must pass, not just one (METHOD.md section 7.2). Status: Reported; URL checked.
26. Measuring what Matters: Construct Validity in Large Language Model Benchmarks. arXiv 2511.04703, 2025. <https://arxiv.org/abs/2511.04703> The statistical test and its cut-off are fixed ahead of time (METHOD.md section 7.2). Status: Reported; URL checked.
27. SkillOpt: Agent skills as trainable parameters. Microsoft Research (paper arXiv 2605.23904), 2026. <https://arxiv.org/abs/2605.23904> and <https://www.microsoft.com/en-us/research/blog/skillopt-agent-skills-as-trainable-parameters/> Scores that decided which change to keep count as selection scores, and held-out results are reported separately (METHOD.md section 7.1). Status: Reported; URL checked.
28. The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents. arXiv 2607.22520, 2026. <https://arxiv.org/abs/2607.22520> A change can help some cases and harm others, so count both and scale checking to risk (METHOD.md sections 7.1 and 7.2). Status: Reported; URL checked.
29. Test plugins with evals. Anthropic (Claude Code documentation). <https://code.claude.com/docs/en/plugin-evals> Comparison arms are declared before an evaluation (METHOD.md section 7.2). Status: Reported; URL checked.
30. skill-creator. Anthropic skills repository. <https://github.com/anthropics/skills/tree/main/skills/skill-creator> A vendor tool that tests skills with and without the skill, supporting declared comparison arms (METHOD.md section 7.2). Status: Reported; URL checked.
31. Improving skill-creator: test, measure and refine agent skills. Anthropic, 2026. <https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills> Skills are tested with and without, and measured, before they are trusted (METHOD.md section 5.5). Status: Reported; URL checked.

## Structure, harnesses and workflows

When to add agents and harness parts, and how long-running work survives.

32. Building effective agents (engineering post). Anthropic, 2024. <https://www.anthropic.com/engineering/building-effective-agents> Begin with the simplest setup, and add agents only when the gain covers the cost (tenet 7). Status: Reported; URL checked.
33. Building effective AI agents. Anthropic, 2024. <https://www.anthropic.com/research/building-effective-agents> The progression from one call to several agents, compared at the same budget (tenet 7). Status: Reported; URL checked.
34. How we built our multi-agent research system. Anthropic, 2025. <https://www.anthropic.com/research/multi-agent-research-system> Running several agents multiplies token spend, so judge them against one agent with the same budget, and by price per accepted outcome (tenet 7, METHOD.md section 6.4). Status: Reported; URL checked.
35. Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets. arXiv 2604.02460, 2026. <https://arxiv.org/abs/2604.02460> Given the same token budget, a single agent often does as well as a team of them (tenet 7, METHOD.md section 7.2). Status: Reported; URL checked.
36. Why Do Multi-Agent LLM Systems Fail?. arXiv 2503.13657, 2025. <https://arxiv.org/abs/2503.13657> Common failure modes of multi-agent systems, supporting strong verifiers before adding agents (tenets 5 and 7). Status: Reported; URL checked.
37. Don't Build Multi-Agents. Cognition, 2025. <https://cognition.com/blog/dont-build-multi-agents> Sub-agents need all prior decisions in their context plus shared durable state (tenet 11, METHOD.md section 6.2). Status: Reported; URL checked.
38. Building a C compiler with parallel Claudes. Anthropic, 2026. <https://www.anthropic.com/research/building-c-compiler> Parallel agents work when a strong test suite exists and progress lives in durable records (tenets 5 and 11). Status: Reported; URL checked.
39. Effective harnesses for long-running agents. Anthropic, 2025. <https://www.anthropic.com/research/effective-harnesses-for-long-running-agents> Progress files, runnable checks and checked outcomes for work that spans sessions (tenets 5, 11 and 12). Status: Reported; URL checked.
40. Harness design for long-running apps. Anthropic, 2026. <https://www.anthropic.com/research/harness-design-long-running-apps> Harness parts are temporary, and no author grades what it produced (tenets 9 and 10). Status: Reported; URL checked.
41. Build Better AI Agents: 5 Developer Tips from the Agent Bake-Off. Google, 2026. <https://developers.googleblog.com/build-better-ai-agents-5-developer-tips-from-the-agent-bake-off/> Decidable logic in tested code, and harness parts re-tested as models change (tenets 2 and 9). Status: Reported; URL checked.
42. Production-Ready AI Agents: 5 Lessons from Refactoring a Monolith. Google, 2026. <https://developers.googleblog.com/production-ready-ai-agents-5-lessons-from-refactoring-a-monolith/> Mechanical enforcement, simple workflows and observable records in production agents (tenet 8, METHOD.md sections 6.2 and 7.5). Status: Reported; URL checked.
43. Minions: Stripe's one-shot, end-to-end coding agents. Stripe, 2026. <https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents> Deterministic gates around agents and review-led delivery (tenet 2, METHOD.md section 7.6); design details are second-hand. Status: Reported; URL checked.
44. Stripe coding agents design report (title not given). InfoQ, 2026. <https://www.infoq.com/news/2026/03/stripe-autonomous-coding-agents/> Independent reporting on the same design, supporting the same points; second-hand. Status: Reported; URL checked.
45. Code execution with MCP for efficient agents. Anthropic, 2025. <https://www.anthropic.com/research/code-execution-with-mcp> Work moved into code the agent runs stays testable and costs fewer tokens (tenet 2). Status: Reported; URL checked.
46. 2026 Agentic Coding Trends Report. Anthropic (vendor report), 2026. <https://resources.anthropic.com/2026-agentic-coding-trends-report> A runnable verifier as the precondition for autonomy (tenet 5). Status: Reported; URL checked.

## Instructions, prompts, models and what to load

How much to load into context, what instruction files hold, and how models differ.

47. Effective context engineering for AI agents. Anthropic, 2025. <https://www.anthropic.com/research/effective-context-engineering-for-ai-agents> Context is a budget; load only what the agent could not locate on its own (tenet 6, METHOD.md section 5.1). Status: Reported; URL checked.
48. Writing effective tools for AI agents. Anthropic, 2025. <https://www.anthropic.com/research/writing-tools-for-agents> Tool output comes back paged, legible and brief (METHOD.md section 6.1). Status: Reported; URL checked.
49. Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?. arXiv 2602.11988, 2026. <https://arxiv.org/abs/2602.11988> Generated repository overviews add cost without raising success, so instruction files stay short (tenet 6, METHOD.md section 5.1). Status: Reported; URL checked.
50. Custom instructions with AGENTS.md. OpenAI (documentation). <https://learn.chatgpt.com/docs/agent-configuration/agents-md> Instruction files as short maps of non-obvious project facts (tenet 8, METHOD.md section 5.1). Status: Reported; URL checked.
51. Best practices for Claude Code. Anthropic (documentation). <https://code.claude.com/docs/en/best-practices> Mechanical enforcement over prose, review in a fresh context, and small context (tenets 6, 8 and 10). Status: Reported; URL checked.
52. Harness engineering: leveraging Codex in an agent-first world. OpenAI, 2026. <https://openai.com/index/harness-engineering/> Rules enforced by linters and CI with the fix in the message, and review-led delivery (tenet 8, METHOD.md section 7.6). Status: Reported; URL checked.
53. Using GPT-6. OpenAI (model guide). <https://developers.openai.com/api/docs/guides/latest-model> Guidance that changes between model generations, supporting lean context and routing by measured fit (tenet 6, METHOD.md section 5.6). Status: Reported; URL checked.
54. Rethinking skills and prompts for GPT-6 Astra. OpenAI, 2026. <https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra> Scaffolding written for an older model may hurt a newer one, so harness parts are re-tested (tenet 9). Status: Reported; URL checked.
55. An update on Claude Code quality reports. Anthropic, 2026. <https://www.anthropic.com/research/april-23-postmortem> Silent model and harness changes moved quality, so re-test on every model change and reuse baselines only with a proven-unchanged setup (tenet 9, METHOD.md sections 5.6 and 7.2). Status: Reported; URL checked.
56. Prompt engineering overview. Anthropic (documentation). <https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview> A better prompt can lift a weaker model (METHOD.md section 6.1). Status: Reported; URL checked.
57. Prompt Quality and Pull Request Outcomes. arXiv 2606.19644, 2026. <https://arxiv.org/html/2606.19644v1> Prompt quality goes with output quality; one of the context-degradation figures (METHOD.md section 6.1). Status: Reported; URL checked.
58. Context performance study summary. ZenML LLMOps database. <https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens> Model accuracy falls as input grows; one of the context-degradation figures (METHOD.md section 6.1). Status: Reported; URL checked.
59. Context rot explanation. Understanding AI. <https://www.understandingai.org/p/context-rot-the-emerging-challenge> Long contexts make relevant material harder to retrieve (METHOD.md sections 5.1 and 6.1). Status: Reported; URL checked.
60. Context growth and degradation. Morph. <https://www.morphllm.com/context-rot> Where information sits in context changes recall (METHOD.md section 5.1). Status: Reported; URL not confirmed (HTTP 429).
61. Coding model benchmarks. Morph. <https://www.morphllm.com/claude-benchmarks> Capability gaps between models widen on long agentic tasks, which is why mechanical work moves to a lower grade only when that grade's minimum quality and checks allow it (METHOD.md section 5.6; MODEL.md, "Grades"). Status: Reported; URL not confirmed (HTTP 429).
62. Model benchmark explanation. Vellum. <https://www.vellum.ai/blog/claude-sonnet-5-benchmarks-explained> Benchmarks show capability gaps between models, the reason the model sorts capability into grades and gives each role a minimum grade (MODEL.md, "Grades"). Status: Reported; URL checked.
63. Over-refusal study. arXiv 2505.08054, 2025. <https://arxiv.org/html/2505.08054v1> Refusal is diagnosed apart from instruction following (METHOD.md section 5.6). Status: Reported; URL checked.
64. Refusal and compliance audit. arXiv 2605.05427, 2026. <https://arxiv.org/html/2605.05427> A refusal is its own outcome, not a cue to try another model (S5). Status: Reported; URL checked.
65. Persona study (title not given). arXiv 2311.10054, 2023. No URL given; arXiv:2311.10054. A persona does not make answers more accurate (METHOD.md section 5.5). Status: Reported; no URL to check.
66. Persona study (title not given). arXiv 2512.05858, 2025. No URL given; arXiv:2512.05858. Further evidence that a persona adds no accuracy. Status: Reported; no URL to check.
67. Persona study (title not given). arXiv 2603.18507, 2026. No URL given; arXiv:2603.18507. Further evidence that a persona adds no accuracy. Status: Reported; no URL to check.

## Vetting skills and plugins

Skills, plugins and catalogues treated as dependencies.

68. Equipping agents with Agent Skills. Anthropic, 2025. <https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills> What a skill is, and why it is code plus prompt (METHOD.md sections 2 and 5.5). Status: Reported; URL checked.
69. Agent Skills specification. Agent Skills project. <https://agentskills.io/specification> The public specification of the skill folder (term defined in METHOD.md section 2). Status: Reported; URL checked.
70. Skill authoring best practices. Anthropic (documentation). <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices> Short, focused skills with clear descriptions, tested against named comparison arms (METHOD.md sections 5.5 and 7.2). Status: Reported; URL checked.
71. Behind the scenes: How we build, test, and scale Google Agent Skills. Google Cloud, 2026. <https://cloud.google.com/blog/topics/developers-practitioners/behind-the-scenes-how-we-build-test-and-scale-google-agent-skills> Skills built, tested and versioned like dependencies (METHOD.md section 5.5). Status: Reported; URL checked.
72. SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks. arXiv 2602.12670, 2026. <https://arxiv.org/abs/2602.12670> Skills help some tasks and hurt others, so measure with paired comparisons (METHOD.md sections 5.5 and 7.2). Status: Reported; URL checked.
73. SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?. arXiv 2603.15401, 2026. <https://arxiv.org/abs/2603.15401> Many skills show no gain on real engineering tasks, so test with and without (METHOD.md section 5.5). Status: Reported; URL checked.
74. anthropics/skills. Anthropic (GitHub). <https://github.com/anthropics/skills> A public skill catalogue: a fine starting point that still needs checking (METHOD.md section 5.5). Status: Reported; URL checked.
75. agent-skills. addyosmani (GitHub). <https://github.com/addyosmani/agent-skills> A public skill collection, an example of a shared catalogue to vet. Status: Reported; URL checked.
76. ECC. affaan-m (GitHub). <https://github.com/affaan-m/ECC> A large workflow pack, an example of something to read and vet before installing. Status: Reported; URL checked.
77. ponytail. DietrichGebert (GitHub). <https://github.com/DietrichGebert/ponytail> A minimal-change coding skill, an example of a single-purpose skill. Status: Reported; URL checked.
78. ponytail-benchmark. KuldeepB19 (GitHub). <https://github.com/KuldeepB19/ponytail-benchmark> A benchmark for that skill, an example of measuring a skill with and without it. Status: Reported; URL checked.
79. llm-council. karpathy (GitHub). <https://github.com/karpathy/llm-council> Several models answering together, related to model juries (METHOD.md section 7.3). Status: Reported; URL checked.

## Outcomes, productivity and cost

Why accepted, stable outcomes are measured instead of raw output, and what agent work costs.

80. Announcing the 2025 DORA Report. Google Cloud (DORA), 2025. <https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report> Delivery stability measured next to throughput (tenet 14). Status: Reported; URL checked.
81. DORA's software delivery performance metrics. DORA, 2026. <https://dora.dev/guides/dora-metrics-four-keys> Change failure rate and related delivery measures (tenet 14, METHOD.md section 7.6). Status: Reported; URL checked.
82. AI Engineering Report Q3 2026, The Speed Trap. Faros AI (vendor report), 2026. <https://faros.ai/research/speed-trap> More output can raise review time and defects (tenet 14). Status: Reported; URL checked.
83. AI Impact on Engineering Productivity: 2026 Report Data. Faros AI (vendor report), 2026. <https://www.faros.ai/research/ai-acceleration-whiplash> Companion data on output against review load and stability (tenet 14). Status: Reported; URL checked.
84. AI vs Human Code Generation Report. CodeRabbit (vendor report), 2025. <https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report> Defect rates in agent-written code, supporting measurement of accepted outcomes (tenet 14). Status: Reported; URL checked.
85. Many SWE-bench-Passing PRs Would Not Be Merged into Main. METR, 2026. <https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/> Passing a benchmark is not acceptance (tenet 14). Status: Reported; URL checked.
86. Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity. METR (arXiv 2507.09089), 2025. <https://arxiv.org/abs/2507.09089> Felt speed and measured speed can differ, so adopt practices on your own evidence (tenet 1). Status: Reported; URL checked.
87. Measuring the Self-Reported Impact of Early-2026 AI on Technical Worker Productivity. METR, 2026. <https://metr.org/blog/2026-05-11-ai-usage-survey/> Self-reported gains are a different measure from observed ones (tenet 1). Status: Reported; URL checked.
88. We are Changing our Developer Productivity Experiment Design. METR, 2026. <https://metr.org/blog/2026-02-24-uplift-update/> Evidence from your own work, and saying what was not measured (tenet 1, METHOD.md section 7.2). Status: Reported; URL checked.
89. State of the Coding Agent Market, October 2026. Amplifying, 2026. <https://amplifying.ai/research/state-of-coding-agents> Market data on agent use and routing (tenet 14, METHOD.md section 5.6). Status: Reported; URL checked.
90. AI coding agents could soon cost more than the developers using them. The Register (reporting a Gartner forecast), 2026. <https://www.theregister.com/ai-and-ml/2026/06/24/ai-coding-agents-could-soon-cost-more-than-the-developers-using-them/5260864> A reported forecast that agent spend may exceed developer cost, supporting the measure of spend for each accepted outcome (METHOD.md section 6.4); the forecast itself was not read first-hand. Status: Reported; URL checked.
91. State of AI: An Empirical 100 Trillion Token Study with OpenRouter. arXiv 2601.10088, 2026. <https://arxiv.org/abs/2601.10088> How work is spread across many models, supporting tests on every model a task is routed to (METHOD.md sections 5.6 and 7.1). Status: Reported; URL checked.

## Protocols, durable execution and records

Message protocols, traces, append-only records and recovery.

92. Model Context Protocol specification. Model Context Protocol. <https://modelcontextprotocol.io/specification/> The tool-server protocol named in the definition of "tool"; a protocol defines transport and grants no approval (METHOD.md sections 2 and 3). Status: Reported; URL checked.
93. The 2026-07-28 Specification. Model Context Protocol, 2026. <https://blog.modelcontextprotocol.io/posts/2026-07-28/> A revision of the same protocol, cited for routing practice (METHOD.md section 5.6). Status: Reported; URL checked.
94. Agent2Agent (A2A) Protocol Specification v1.0. A2A project. <https://a2a-protocol.org/latest/specification/> Explicit task states for agents that talk across boundaries; transport is not approval (METHOD.md sections 3 and 6.2). Status: Reported; URL checked.
95. A2A, Streaming and Asynchronous Operations. A2A project. <https://a2a-protocol.org/latest/topics/streaming-and-async/> Long-running agent tasks report their state asynchronously, which fits the rule that agents talking across vendor or team boundaries speak an open protocol whose task states are explicit (METHOD.md section 6.2). Status: Reported; URL checked.
96. A2A. a2aproject (GitHub). <https://github.com/a2aproject/A2A> Reference implementation of the agent-to-agent protocol. Status: Reported; URL checked.
97. A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year. Linux Foundation, 2026. <https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year> Wide use of an open agent protocol, supporting open protocols across vendor boundaries (METHOD.md section 6.2). Status: Reported; URL checked.
98. OpenTelemetry semantic conventions for generative AI. OpenTelemetry, 2026. <https://github.com/open-telemetry/semantic-conventions-genai> Standard fields for observability and audit records of model calls (METHOD.md section 7.5). Status: Reported; URL checked.
99. OpenTelemetry semantic conventions for generative AI spans. OpenTelemetry. <https://github.com/open-telemetry/semantic-conventions/blob/main/docs/gen-ai/gen-ai-spans.md> Trace span fields for model calls (METHOD.md section 7.5, RECORDS.md). Status: Reported; URL checked.
100. W3C Trace Context. W3C. No URL given; W3C Recommendation; title and publisher only. One identifier carries a trace across services, like the single run id (METHOD.md section 7.5). Status: Reported; no URL to check.
101. RFC 6962, Certificate Transparency. IETF. No URL given; IETF RFC 6962. Hash-chained append-only logs make records tamper-evident (RECORDS.md, "Run records"). Status: Reported; no URL to check.
102. Transactional outbox for agent coordination (title not given). Zylos, 2026. <https://zylos.ai/research/2026-06-02-transactional-outbox-pattern-ai-agent-coordination/> State changes and outgoing events committed together (MODEL.md, "Messages between agents"). Status: Reported; URL checked.
103. Durable execution write-up on DBOS, Inngest, Restate and Temporal (title not given). Reactify Solutions, 2026. <https://www.reactify-solutions.com/articles/durable-ai-agents-2026> Durable execution lets agents resume after a crash without losing or repeating work (tenet 11). Status: Reported; URL checked.
104. Crash-Only Software. HotOS IX, 2003. No URL given; USENIX HotOS IX (2003); no standard identifier given. Systems designed to recover by restarting (tenet 11, ADAPTERS.md, "Operations are idempotent"). Status: Reported; no URL to check.
105. Site Reliability Engineering. O'Reilly, 2016. No URL given; title and publisher only. Reliability practice for production services, behind bounded retries and run limits (METHOD.md section 6.3). Status: Reported; no URL to check.
106. The Site Reliability Workbook. O'Reilly, 2018. No URL given; title and publisher only. Applied reliability practice, as for the entry above. Status: Reported; no URL to check.
107. QuickCheck. ICFP 2000, 2000. No URL given; Koen Claessen and John Hughes, ICFP 2000, DOI 10.1145/351240.351266. Property-based testing with generated inputs, one way to probe bad and boundary input (METHOD.md section 7.1). Status: Reported; no URL to check.
108. Documenting Architecture Decisions. 2011. No URL given; Michael Nygard, Cognitect blog (2011); title and publisher only. Short decision records, the form used in decisions/. Status: Reported; no URL to check.

## Standards, compliance and licensing

Standards that the safeguards and repository practice map onto.

109. ISO/IEC 27001:2022. ISO/IEC, 2022. No URL given; ISO/IEC 27001:2022. Information security controls that an organisation's own policies, which take precedence, may draw on. Status: Reported; no URL to check.
110. ISO/IEC 42001:2023. ISO/IEC, 2023. No URL given; ISO/IEC 42001:2023. A management system for AI, a frame for the organisation policies the method defers to. Status: Reported; no URL to check.
111. NIST AI RMF 1.0. NIST, 2023. No URL given; NIST AI 100-1, DOI 10.6028/NIST.AI.100-1. Risk management for AI systems, the same role as above. Status: Reported; no URL to check.
112. NIST SP 800-218 (SSDF) and SP 800-218A. NIST. <https://csrc.nist.gov/pubs/sp/800/218/a/final> Secure development practice extended to AI systems (METHOD.md section 5.5). Status: Reported; URL checked.
113. GDPR Article 5. European Union. No URL given; Regulation (EU) 2016/679, Article 5. Data minimisation and limited retention, behind S3 and retention periods (METHOD.md section 7.5). Status: Reported; no URL to check.
114. SLSA. SLSA project. <https://slsa.dev> Build provenance for the supply chain, related to pinned and reviewed host components (ADAPTERS.md). Status: Reported; URL checked.
115. OpenSSF Scorecard. OpenSSF. <https://securityscorecards.dev> Automated checks of a repository's security practice; such a score never qualifies a host (METHOD.md section 1). Status: Reported; URL checked.
116. SPDX. SPDX project. <https://spdx.dev> Machine-readable licence identifiers. Status: Reported; URL checked.
117. REUSE specification. REUSE (FSFE). <https://reuse.software> Every file states its licence and copyright. Status: Reported; URL checked.
118. Semantic Versioning 2.0.0. semver.org. <https://semver.org> Version numbers that signal compatibility, as for schema versions (ADAPTERS.md, "Sentinels"). Status: Reported; URL checked.

## Comparable tools

Listed alphabetically. Each does something related to part of why-bureau; see "How sources are used" for what such a listing can and cannot show.

119. Bernstein. Bernstein project. <https://bernstein.run/> Runs CLI agents on a deterministic schedule, each in an isolated workspace, and keeps verification logs; the project states Apache-2.0. Status: Reported; URL checked.
120. claude-code-router. musistudio (GitHub). <https://github.com/musistudio/claude-code-router> A router run on your own machine that sends requests to models and switches over when one fails; MIT. Status: Reported; URL checked.
121. CrewAI. crewAIInc (GitHub). <https://github.com/crewAIInc/crewAI> Teams of agents with assigned roles, and orchestrated workflows; the project states MIT. Status: Reported; URL checked.
122. oh-my-subagents. ringlochid (GitHub). <https://github.com/ringlochid/oh-my-subagents> Runs on one machine, coordinates agent teams that can be reused, keeps task progress durable, and resumes after an interruption; MIT core. Status: Reported; URL checked.
123. OpenHands. OpenHands (GitHub). <https://github.com/OpenHands/OpenHands> Agents that write code, deployed inside a sandbox; that repository states MIT. Status: Reported; URL checked.

## Specifications used by the repository's own files

| Source | Used for | Where | Status |
|---|---|---|---|
| JSON Schema, draft 2020-12, <https://json-schema.org/draft/2020-12> | The schema language of `schemas/`. | schemas/README.md | Reported; URL checked |
| TOML 1.0.0, <https://toml.io/en/v1.0.0> | The format of the `roles.toml` team file. | MODEL.md, "Roles" | Reported; URL checked |
| Apache License 2.0, <https://www.apache.org/licenses/LICENSE-2.0> | The licence of this repository. | LICENSE | Reported; URL checked |
| Git attributes, <https://git-scm.com/docs/gitattributes> | Storing adopted texts byte-exact. | .gitattributes | Reported; URL checked |
| GitHub private vulnerability reporting, <https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability> | How to report a security problem. | SECURITY.md | Reported; URL checked |
