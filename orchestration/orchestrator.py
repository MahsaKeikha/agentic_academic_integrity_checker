from AGENTS.adjudication_support_agent import run as adjudication
from AGENTS.authorship_signal_agent import run as authorship
from AGENTS.citation_verification_agent import run as citations
from AGENTS.evidence_review_agent import run as evidence
from AGENTS.policy_mapping_agent import run as policy
from safety.policy import authorize


def orchestrate(context: dict) -> dict:
    """Run integrity specialists and apply fail-closed advisory governance."""
    results = [
        authorship(context),
        citations(context),
        evidence(context),
        policy(context),
        adjudication(context),
    ]
    governance = authorize("integrity_advisory_release", context)
    return {
        "system": "F97",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_review_required": True,
        "autonomous_misconduct_authority": False,
        "autonomous_disciplinary_authority": False,
    }
