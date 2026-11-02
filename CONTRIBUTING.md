# Contributing

## Proposing a change

1. Open an issue that says what you want to change and why.
2. Send a pull request that makes the change. Keep it small.
3. Run `python schemas/check.py` and make sure it exits with status 0.
4. The pull request is reviewed by a person other than its author before it is merged.

## Changing METHOD.md or CHARTER.md

METHOD.md and CHARTER.md are adopted texts. For each, a record in `decisions/` pins the exact SHA-256 at which it was adopted.

- Every adopted file has a SHA-256 sidecar file next to it, named after the file with `.sha256` added, in `sha256sum` format (`METHOD.md.sha256`, `CHARTER.md.sha256`). Check both with `sha256sum -c METHOD.md.sha256 CHARTER.md.sha256`.
- Changing an adopted file means writing a new decision record naming the file's new SHA-256 and its refreshed sidecar. Until that record exists, the changed file does not count as adopted.
- A copy is the adopted text only when its hash equals the one its sidecar holds.
- When the repository holds a copy of a text locked elsewhere, the copy is identified in two ways: the source digest identifies the original it came from, and the copy's own sidecar identifies the copy. The copy's lock is distinct from the original's lock, and the copy establishes no enforcement at runtime.
- Adopting a text records no owner signature and no runtime check. It changes only the adopted description and the digest.
- The text adopted by the latest decision record is the one in force. Superseded versions stay only in version control history.
- Adopting a text gives it no new signature and qualifies no runtime.
- Adopted texts, their sidecars and any adoption index live either in `docs/texts/` or at a path named in `.gitattributes`. Every file under `docs/texts/`, and every file `.gitattributes` names, is stored byte-exact with no line-ending conversion. Do not let an editor or a tool rewrite their line endings.

## Labels and the grade-only rule

- Every control in the method, the charter and the specification carries a label: **Required** or **Suggested**. In the specification, a Required control names the safeguard, tenet or charter section it repeats. A Suggested control is never written as a rule.
- Rules name grades (build, build-lite, fast, review, senior, top) and never a vendor or a specific model. Specific models are named only in private model rosters and in factual run records.

## What belongs in this repository

- General rules, public ideas and normative controls.
- Not private records, censuses of projects, local measurements, machine paths, people, or framing specific to one organisation.
- Building, testing and releasing need no dispatch history, no post archives and no private overlays. A contributor is free to use a memory of their own, or to work without one.

## Writing docs

The README is the front door: a stranger decides in a minute whether to try the project.

- Order: the project name and a one-line promise, status badges from GitHub, and a figure of the project working, all before the first section. Then the headings "Why", "Features", "Quick start" and "Docs". Under "Why", state the reader's problem with one line of evidence. Number the quick-start steps; run each one and end it on a check the reader can run. Put reference detail behind links.
- Keep paragraphs to at most 60 words, most under 25. Put detail in lists, tables or linked pages.
- Each sentence states one thing a reader can check. Name who does what, and state errors as cause and fix. No filler words, no "etc.", no dashes joining clauses, no "not X but Y", no sales adjectives.
- Explain a technical term the first time it appears, or link to where it is explained. Keep each fact in one place and link to it elsewhere.
- Every number is measured, or marked "not measured" with the command that would measure it. Name the source of each claim, and keep observed, reported and planned behaviour apart.
- Use at least two distinct rendered figures that answer different questions, in one style. Badges, logos and repeated images do not count. Give each figure labels, alt text and a caption stating its conclusion and limits; colour never carries meaning alone. Use animation when motion explains the task. Keep each diagram as one plain-text SVG in the repository, edited directly, with system fonts and no external resources; update any derived image when its SVG changes. Never paste diagram source or ASCII boxes into the README.
- Check what each figure shows against the source revision, and look at it at reading size. Record both checks; keep unperformed checks pending.
- Keep the status, the key evidence and the main limits next to the claims they qualify. Never include secrets, tokens, personal data or paths outside the project.

Before opening a pull request, run `python scripts/readme_lint.py README.md`; CI runs it on every pull request. Passing the lint does not mean the README follows every rule above. A reviewer checks every rule above and that links open without signing in. Then someone unfamiliar with the project, without help, says its audience, problem and status within a minute, and after reading, its input, output, the decision it supports, the first action, the evidence and the main limits, and explains the figures. Record their answers and what they misread, fix it and ask again. Keep the GitHub sidebar current: description, a working website or docs link, 5 to 10 relevant topics, a social preview image, and a release for each published version. If the lint rejects correct text, open an issue about the lint; do not rewrite correct text to pass it.
