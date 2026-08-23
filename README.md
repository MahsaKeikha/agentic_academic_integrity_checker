# F97 Agentic Academic Integrity Checker

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed five-agent reference architecture for academic-integrity review across submission context, authorship signals, citation verification, evidence provenance, institutional policy mapping, due process, privacy, conflicting evidence, and qualified human adjudication support.

F97 is designed as a reusable advisory-only multi-agent reference for universities, colleges, schools, instructors, academic-integrity offices, and review committees that need structured support for examining potential integrity concerns without transferring misconduct, disciplinary, sanctions, appeals, or student-record authority to an automated system.

This repository supports evidence organization and human review. It does not autonomously make misconduct findings, recommend sanctions, impose discipline, modify student records, decide appeals, or report externally. Authorship signals are explicitly treated as non-conclusive evidence and must be considered together with traceable evidence, policy context, and qualified human process.

## Academic-integrity lifecycle

```text
submission + course context
          |
          v
   authorship signals
          |
          v
 citation verification
          |
          v
    evidence review
          |
          v
     policy mapping
          |
          v
 adjudication support
          |
          v
qualified human decision
```

The workflow is fail closed. Missing evidence provenance, overclaimed authorship signals, incomplete citation verification, ambiguous policy mapping, insufficient evidence, due-process gaps, student-privacy risks, unresolved conflicting evidence, missing review evidence, or missing qualified-human adjudicator approval remain blockers.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Authorship Signal Agent | Reviews non-conclusive indicators related to authorship, drafting patterns, provenance, and available contextual evidence | What signals exist, how reliable are they, and what must not be inferred from them? |
| Citation Verification Agent | Checks references, quotations, attribution, source traceability, and citation-support relationships | Are cited sources real, relevant, accurately represented, and properly attributed? |
| Evidence Review Agent | Organizes evidence, provenance, conflicts, limitations, and evidentiary sufficiency | What evidence is actually available, and what conclusions does it support or fail to support? |
| Policy Mapping Agent | Maps the case to the applicable institutional or course policy without inventing rules | Which policy provisions may apply, and where is interpretation still required by qualified humans? |
| Adjudication Support Agent | Produces a structured advisory package for qualified human review | Is the record sufficiently complete, fair, traceable, and procedurally ready for human adjudication? |

No agent independently determines guilt, intent, misconduct, discipline, sanctions, appeal outcomes, or student-record changes.

## Repository structure

```text
AGENTS/
├── authorship_signal_agent.py
├── citation_verification_agent.py
├── evidence_review_agent.py
├── policy_mapping_agent.py
└── adjudication_support_agent.py

SKILLS/
├── authorship_analysis.py
├── citation_verification.py
├── evidence_assessment.py
├── policy_mapping.py
└── adjudication_briefing.py

TOOLS/
├── case_log_tool.py
├── citation_check_tool.py
├── comparison_tool.py
├── policy_matrix_tool.py
└── source_trace_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The structure separates analytical assistance from deterministic case logging, citation checking, comparison, policy mapping, and source tracing while keeping governance, evaluation, observability, and human authority explicit.

## Submission context

A useful review record can include:

```text
case_id
course_or_program
assignment_type
submission_date
student_or_author_identifier
assessment_rules
permitted_assistance
permitted_ai_use
citation_requirements
collaboration_rules
submission_artifacts
source_materials
version_history
instructor_observations
student_explanation
applicable_policy
review_owner
```

Implementations should minimize personally identifying information and only retain information necessary for the legitimate academic-integrity process.

## Context before inference

A potential integrity concern cannot be interpreted reliably without understanding the assignment and the rules that applied when the work was produced.

Relevant context can include:

- whether collaboration was permitted
- whether generative AI was allowed
- whether tutoring or editing assistance was permitted
- whether source use was restricted
- whether drafts were required
- whether citation style was specified
- whether reuse of prior work was permitted
- whether the work was individual or group-based

A system should not infer misconduct merely because a work product appears unusual.

## Authorship signals

`SKILLS/authorship_analysis.py` supports structured analysis of authorship-related signals.

Potential signals can include:

- drafting history
- version history
- metadata
- writing-pattern changes
- unusual phrase overlap
- source-use anomalies
- inconsistent reasoning across artifacts
- unexplained shifts in terminology
- discrepancies between oral explanation and submitted work

These signals are contextual clues, not proof.

## Authorship signals are not conclusive

F97 explicitly prevents authorship signals from being treated as dispositive evidence.

The governance blocker `authorship_signal_overclaimed` applies when an indicator is being treated as if it conclusively proves who authored a work or whether misconduct occurred.

Writing style, fluency, vocabulary, formatting, or sudden improvement can have many explanations. They should not be converted into certainty without corroborating evidence.

## AI-detection boundary

Model-generated-text detectors, stylometric tools, perplexity estimates, or similar automated scores should not be treated as conclusive proof of AI use or misconduct.

A detector score may be one input to a broader inquiry, but F97 should preserve uncertainty and require corroborating evidence, applicable policy, and human review.

The system should never state that a student used AI solely because an automated detector reports a probability or label.

## Comparison analysis

`TOOLS/comparison_tool.py` supports structured comparison of artifacts.

Comparisons can examine:

- versions of the same document
- student work and suspected source material
- citation text and original source text
- drafts and final submissions
- assignment requirements and submitted content

Comparison should make overlap and differences visible without silently converting similarity into a misconduct finding.

## Citation verification

`SKILLS/citation_verification.py` and `TOOLS/citation_check_tool.py` support structured citation review.

Citation verification can examine whether:

- the source exists
- the citation resolves to the claimed source
- quotations match the source
- paraphrases remain faithful
- page or section references are plausible
- the cited source supports the associated claim
- references are fabricated or unverifiable
- attribution is missing where required

A citation error is not automatically equivalent to intentional misconduct.

## Source tracing

`TOOLS/source_trace_tool.py` supports provenance tracking for source-based evidence.

A useful source record can include:

```text
source_id
source_type
title_or_description
author_or_owner
location
version_or_date
retrieval_date
relevant_excerpt_or_claim
verification_status
limitations
```

The system should distinguish verified source content from inferred source relationships.

## Evidence provenance

Every material integrity claim should be traceable to evidence.

Evidence provenance can include:

- submission artifact
- draft history
- institutional system record
- source material
- citation record
- instructor observation
- student explanation
- witness information where applicable
- technical log where authorized

F97 should not fabricate evidence, timestamps, metadata, sources, communications, or institutional records.

`evidence_provenance_missing` is an explicit fail-closed blocker.

## Evidence sufficiency

Evidence can exist without being sufficient for a reliable conclusion.

The system should ask:

- Is the evidence relevant?
- Is it authentic?
- Is it complete?
- Is it corroborated?
- Is there an alternative explanation?
- Is the evidence consistent with the applicable policy?
- Is contradictory evidence unresolved?

`insufficient_evidence` blocks advisory-package release when the record does not support reliable review.

## Conflicting evidence

Academic-integrity cases can contain conflicting evidence.

Examples include:

- a detector score suggesting AI use while version history shows gradual drafting
- suspicious phrase overlap with a source but proper citation elsewhere
- inconsistent metadata with a plausible device or software explanation
- an instructor concern contradicted by contemporaneous drafts

`conflicting_evidence_unresolved` remains a blocker rather than being resolved automatically in favor of suspicion.

## Policy mapping

`SKILLS/policy_mapping.py` and `TOOLS/policy_matrix_tool.py` support structured mapping between evidence and applicable rules.

A policy map can preserve:

```text
policy_source
policy_version
applicable_course_or_program
provision
required_elements
available_evidence
missing_evidence
interpretation_question
review_owner
```

The system should not invent an institutional policy or apply a policy from another term, course, program, or institution without justification.

## Policy ambiguity

Policies can be incomplete, conflicting, outdated, or unclear.

When the applicable rule is ambiguous, the system should flag `policy_mapping_ambiguous` rather than choose the interpretation most favorable to a misconduct conclusion.

Qualified institutional interpretation remains authoritative.

## Academic integrity and intent

A policy violation and a conclusion about intent are not necessarily the same question.

Potential issues can include:

- plagiarism
- unauthorized collaboration
- unauthorized tool use
- fabricated citations
- falsified data
- contract cheating
- reuse of prior work
- prohibited external assistance
- exam misconduct

Whether a specific situation meets an institutional definition requires the actual policy, evidence, and qualified human process.

## Due process

Academic-integrity review can have serious consequences for students and researchers.

`due_process_reviewed` is a required governance condition.

A fair process may require, depending on institutional policy:

- notice of the concern
- access to relevant evidence
- opportunity to respond
- opportunity to provide context or evidence
- impartial review
- documentation of the decision basis
- appeal or review rights
- appropriate timelines

F97 does not define one universal institutional process, but it must not bypass the process that applies.

## Student or author response

A student's or author's explanation is evidence that should be recorded and reviewed rather than ignored.

Relevant explanations can include:

- drafting process
- source use
- collaboration
- authorized assistance
- software or tool use
- citation mistakes
- accessibility-related workflows
- language-support tools
- prior versions
- technical anomalies

The system should not presume that an explanation is false merely because an automated signal conflicts with it.

## Privacy

Academic-integrity cases can contain highly sensitive educational information.

Potentially sensitive data include:

- student identity
- grades
- disability or accommodation information
- disciplinary history
- communications
- device or account records
- learning-management records
- drafts
- private notes

`privacy_reviewed` is required, and `student_privacy_risk` blocks release.

Implementations should use data minimization, access controls, appropriate retention, and authorized institutional processes.

## Accessibility and language considerations

Writing variation can result from many legitimate factors, including language development, accessibility tools, dictation, editing support, translation support, or assistive technology.

The system should not infer disability, language background, or unauthorized assistance from style alone.

Formal accommodation information should only be used when appropriate and authorized.

## Bias and fairness

Academic-integrity systems can amplify bias if they rely on proxies unrelated to actual evidence.

Review should avoid unsupported conclusions based on:

- accent or language style
- grammar quality
- educational background
- nationality
- age
- disability
- writing sophistication
- sudden improvement
- perceived technical ability

The focus should remain on traceable evidence and applicable policy.

## Case logging

`TOOLS/case_log_tool.py` supports structured case tracking.

A case log can preserve:

```text
case_id
issue_reported
evidence_received
source_provenance
review_actions
student_or_author_response
policy_mapping
open_questions
conflicting_evidence
human_review_state
final_institutional_outcome
```

A case log should distinguish system-generated observations from institutional findings.

## Adjudication support

`SKILLS/adjudication_briefing.py` supports preparation of an advisory package for qualified human review.

A briefing can include:

- case context
- applicable policy
- verified evidence
- authorship signals with limitations
- citation findings
- conflicting evidence
- student or author response
- unresolved questions
- due-process status
- privacy considerations
- required human decisions

The briefing should not contain an automated declaration of guilt.

## Required reviews

The safety policy requires:

```text
submission_context_reviewed
evidence_provenance_reviewed
authorship_signal_reviewed
citation_verification_reviewed
policy_mapping_reviewed
due_process_reviewed
privacy_reviewed
human_adjudicator_approval
```

Missing any required review causes the workflow to fail closed.

## Fail-closed governance

Reference blockers include:

- evidence provenance incomplete
- authorship signal treated as conclusive evidence
- citation verification incomplete
- institutional policy mapping ambiguous
- evidence insufficient for reliable integrity assessment
- notice, response, or appeal process incomplete
- student privacy risk unresolved
- conflicting evidence unresolved
- required review missing
- qualified human adjudicator approval missing

The workflow should surface the blocker rather than manufacture a definitive integrity judgment.

## Protected actions

The reference policy prohibits autonomous execution of:

```text
misconduct_finding
disciplinary_action
student_record_change
external_reporting
sanction_recommendation
appeal_determination
```

These actions remain outside system authority even when all review flags are true.

## Human authority boundaries

F97 must not autonomously:

- determine that misconduct occurred
- determine intent
- recommend sanctions
- impose discipline
- modify grades or student records
- make progression or graduation decisions
- decide an appeal
- report a student externally
- disclose protected case information without authorization
- fabricate evidence or policy
- treat AI-detection output as proof
- claim institutional approval

Final authority remains with qualified faculty, academic-integrity officers, committees, administrators, and authorized institutional processes.

## Appeals boundary

An appeal is a separate institutional process with its own authority and evidentiary standards.

F97 can organize evidence or prior findings for authorized reviewers, but `appeal_determination` is explicitly protected and cannot be automated.

## Sanctions boundary

Even when a qualified human determines that a policy violation occurred, the appropriate consequence can depend on policy, severity, prior history, educational context, proportionality, and institutional procedure.

F97 does not autonomously recommend sanctions or disciplinary outcomes.

## External reporting boundary

Academic-integrity information should not be reported to external organizations, credentialing bodies, employers, sponsors, or other institutions merely because the system identifies a concern.

`external_reporting` is a protected action requiring authorized institutional handling.

## End-to-end reference workflow

A typical F97 workflow follows this sequence:

1. Capture the submission, assignment, course, and institutional context.
2. Record the rules governing collaboration, citations, tools, and AI use.
3. Register available evidence with provenance.
4. Review authorship-related signals while preserving uncertainty.
5. Verify citations, quotations, references, and source support.
6. Compare relevant artifacts where authorized.
7. Review evidence sufficiency and alternative explanations.
8. Identify and preserve conflicting evidence.
9. Map evidence to the correct version of applicable policy.
10. Confirm that privacy requirements are addressed.
11. Confirm notice, response, and other due-process requirements.
12. Record the student or author's response and supporting evidence.
13. Prepare an adjudication-support briefing.
14. Apply fail-closed governance gates.
15. Require explicit qualified-human adjudicator approval.
16. Keep misconduct findings, sanctions, appeals, discipline, record changes, and external reporting outside autonomous authority.

## Evaluation and held-out governance suite

The repository includes evaluation logic under `evals/` and benchmark material under `benchmarks/`.

Evaluation should test both analytical usefulness and governance behavior.

Useful dimensions include:

- evidence provenance discipline
- citation-verification accuracy
- unsupported-authorship-inference prevention
- AI-detector overclaim prevention
- policy-mapping correctness
- conflicting-evidence handling
- evidence-sufficiency calibration
- privacy enforcement
- due-process enforcement
- protected-action enforcement
- human-adjudicator approval enforcement

Held-out scenarios should include cases where surface-level signals appear suspicious but corroborating evidence is weak, contradictory, or exculpatory.

## Direct governance tests

The behavioral verification layer should confirm at minimum that:

- a fully reviewed advisory package can be released
- missing human adjudicator approval fails closed
- misconduct findings are never autonomous
- missing evidence provenance blocks release
- overclaimed authorship signals block release
- incomplete citation verification blocks release
- ambiguous policy mapping blocks release
- insufficient evidence, privacy gaps, due-process gaps, or unresolved conflicting evidence remain blockers as represented in the governance suite

Production deployments require institution-specific validation beyond the reference tests.

## Explicit failure states

Useful explicit states include:

```text
SUBMISSION CONTEXT INCOMPLETE
EVIDENCE PROVENANCE MISSING
AUTHORSHIP SIGNAL NONCONCLUSIVE
AUTHORSHIP SIGNAL OVERCLAIMED
CITATION VERIFICATION INCOMPLETE
POLICY MAPPING AMBIGUOUS
INSUFFICIENT EVIDENCE
CONFLICTING EVIDENCE UNRESOLVED
DUE PROCESS INCOMPLETE
PRIVACY REVIEW REQUIRED
HUMAN ADJUDICATOR APPROVAL REQUIRED
MISCONDUCT FINDING AUTHORITY PROHIBITED
SANCTION RECOMMENDATION PROHIBITED
DISCIPLINARY ACTION PROHIBITED
STUDENT RECORD CHANGE PROHIBITED
APPEAL DETERMINATION PROHIBITED
EXTERNAL REPORTING PROHIBITED
```

The system should never fabricate authorship certainty, intent, evidence, sources, policy language, institutional decisions, disciplinary history, or human approval.

## Observability

The `observability/` layer supports traceability of the multi-agent workflow.

Useful telemetry can include:

- case identifier
- evidence sources
- citation checks
- source traces
- comparison operations
- authorship-signal limitations
- policy mappings
- unresolved evidence conflicts
- privacy flags
- due-process state
- human-review state
- governance blockers

Observability supports auditability. It does not create adjudicative authority.

## Memory and state

The `memory/` and `state/` layers can retain structured workflow context across review stages.

State should distinguish:

- raw evidence
- verified evidence
- system observations
- hypotheses
- unresolved questions
- student or author statements
- institutional policy
- qualified human findings

Implementations should avoid retaining unnecessary case information and should follow applicable institutional retention and access rules.

## Provenance and uncertainty

Material claims should preserve source and confidence where practical.

The system should distinguish among:

```text
verified fact
authorship signal
comparison observation
policy provision
student or author statement
system inference
qualified human finding
```

Uncertainty is a feature of responsible review and should not be hidden behind confident language.

## Reproducibility

For a case intended to be reviewed or audited, preserve at minimum:

- submission version
- assignment instructions
- applicable policy version
- evidence sources
- source verification state
- citation findings
- comparison inputs
- authorship-signal limitations
- student or author response
- unresolved conflicts
- governance state
- human-review state

Reproducibility should not justify unnecessary retention of sensitive student data.

## Reproduce the reference implementation

Install the project:

```bash
python -m pip install -e .
```

Run static verification:

```bash
ruff check . --select E9,F63,F7,F82
```

Run direct governance tests:

```bash
python -m pytest -q
```

Run the held-out governance suite:

```bash
python evals/held_out.py
```

Run the governed reference workflow:

```bash
python run.py
```

CI validates the reference implementation on Python 3.10, 3.11, and 3.12.

## Extension points

Potential institution-specific extensions include:

- learning-management-system evidence import
- version-history systems
- institutional policy repositories
- citation databases
- authorized document-comparison services
- case-management systems
- role-based reviewer workflows
- appeal-routing systems
- secure evidence stores

New integrations should preserve privacy, provenance, uncertainty, due process, and human adjudicative authority.

## Example applications

F97 can serve as a reference architecture for:

- citation and source-verification review
- suspected plagiarism case preparation
- AI-use policy review
- authorship-evidence organization
- academic-integrity case intake
- policy mapping
- evidence-conflict analysis
- adjudication briefing
- academic-integrity training

It should not be deployed as an automated misconduct detector or disciplinary decision maker.

## Design principles

1. Treat authorship signals as non-conclusive evidence.
2. Require provenance for material evidence.
3. Verify citations and source relationships directly when possible.
4. Separate similarity from misconduct.
5. Separate policy mapping from adjudication.
6. Preserve contradictory and exculpatory evidence.
7. Protect student privacy and procedural fairness.
8. Fail closed when evidence or policy is insufficient.
9. Keep findings, sanctions, discipline, appeals, and record changes under qualified human authority.
10. Evaluate refusal and escalation behavior as seriously as analytical quality.

## Scope statement

F97 is an advisory academic-integrity reference architecture for governed multi-agent evidence review. It demonstrates how specialized agents, deterministic tools, explicit state, observability, evaluation, and fail-closed controls can support academic-integrity workflows without giving an AI system autonomous authority to determine misconduct or impose consequences.

It is not an academic-integrity officer, disciplinary committee, appeals body, or substitute for qualified institutional process.