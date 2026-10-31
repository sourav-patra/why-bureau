# Security

## Reporting a problem

Report security problems through GitHub private vulnerability reporting: on the repository page, open the Security tab and choose "Report a vulnerability". Do not open a public issue for a security problem.

The maintainer aims to reply within 7 days.

## Scope

This repository holds a draft specification, JSON Schemas and a check script. Useful reports include:

- a rule in METHOD.md, CHARTER.md or the specification that, if followed, would let an agent gain authority, leak data or skip review;
- a schema that accepts a document breaking a Required control;
- a flaw in `schemas/check.py`.

There is no reference implementation yet, so there is no running service to test.
