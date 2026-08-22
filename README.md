# F97 | Agentic Academic Integrity Checker | L3 Gold Standard | v1.0

A governed multi-agent reference system for authorship signals, citation verification, evidence review, policy mapping, and human adjudication support.

## Five-agent architecture

- Authorship Signal Agent
- Citation Verification Agent
- Evidence Review Agent
- Policy Mapping Agent
- Adjudication Support Agent

## Gold-standard academic-integrity governance

F97 is fail closed and advisory only. Release requires reviewed submission context, evidence provenance, authorship signals, citation verification, institutional policy mapping, due process, privacy, and explicit qualified human adjudicator approval.

Release is blocked for missing evidence provenance, overclaimed authorship signals, incomplete citation verification, ambiguous policy mapping, insufficient evidence, due-process gaps, student privacy risks, or unresolved conflicting evidence.

The reference system cannot autonomously make misconduct findings, recommend sanctions, impose discipline, change student records, determine appeals, or report externally. Authorship signals are treated as non-conclusive evidence and must be considered together with traceable evidence and institutional process.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out academic-integrity suite.
