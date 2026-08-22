"""Fail-closed governance for F97 Academic Integrity Checker."""

PROTECTED_ACTIONS = {
    "misconduct_finding",
    "disciplinary_action",
    "student_record_change",
    "external_reporting",
    "sanction_recommendation",
    "appeal_determination",
}

REQUIRED_REVIEWS = (
    "submission_context_reviewed",
    "evidence_provenance_reviewed",
    "authorship_signal_reviewed",
    "citation_verification_reviewed",
    "policy_mapping_reviewed",
    "due_process_reviewed",
    "privacy_reviewed",
    "human_adjudicator_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding academic adjudication is outside reference-system authority"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required academic-integrity review", "missing": missing}

    blockers = []
    if context.get("evidence_provenance_missing"):
        blockers.append("evidence provenance incomplete")
    if context.get("authorship_signal_overclaimed"):
        blockers.append("authorship signal treated as conclusive evidence")
    if context.get("citation_verification_gap"):
        blockers.append("citation verification incomplete")
    if context.get("policy_mapping_ambiguous"):
        blockers.append("institutional policy mapping ambiguous")
    if context.get("insufficient_evidence"):
        blockers.append("evidence insufficient for reliable integrity assessment")
    if context.get("due_process_gap"):
        blockers.append("notice, response, or appeal process incomplete")
    if context.get("student_privacy_risk"):
        blockers.append("student privacy risk unresolved")
    if context.get("conflicting_evidence_unresolved"):
        blockers.append("conflicting evidence unresolved")

    if blockers:
        return {"allowed": False, "reason": "academic-integrity governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "advisory integrity package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
