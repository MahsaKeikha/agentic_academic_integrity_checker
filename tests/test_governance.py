from orchestration.orchestrator import orchestrate
from safety.policy import authorize


def valid_context():
    return {
        "submission_context_reviewed": True,
        "evidence_provenance_reviewed": True,
        "authorship_signal_reviewed": True,
        "citation_verification_reviewed": True,
        "policy_mapping_reviewed": True,
        "due_process_reviewed": True,
        "privacy_reviewed": True,
        "human_adjudicator_approval": True,
    }


def test_complete_review_can_release_advisory_package():
    result = orchestrate(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_misconduct_authority"] is False


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_adjudicator_approval"] = False
    assert orchestrate(context)["release_allowed"] is False


def test_misconduct_finding_is_never_autonomous():
    assert authorize("misconduct_finding", valid_context())["allowed"] is False


def test_missing_evidence_provenance_blocks_release():
    context = valid_context()
    context["evidence_provenance_missing"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_authorship_signal_overclaim_blocks_release():
    context = valid_context()
    context["authorship_signal_overclaimed"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_insufficient_evidence_blocks_release():
    context = valid_context()
    context["insufficient_evidence"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_due_process_gap_blocks_release():
    context = valid_context()
    context["due_process_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_student_privacy_risk_blocks_release():
    context = valid_context()
    context["student_privacy_risk"] = True
    assert orchestrate(context)["release_allowed"] is False
