from orchestration.orchestrator import orchestrate


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_adjudicator_approval": False}, False),
    ({**base(), "evidence_provenance_missing": True}, False),
    ({**base(), "authorship_signal_overclaimed": True}, False),
    ({**base(), "citation_verification_gap": True}, False),
    ({**base(), "policy_mapping_ambiguous": True}, False),
    ({**base(), "insufficient_evidence": True}, False),
    ({**base(), "due_process_gap": True}, False),
    ({**base(), "student_privacy_risk": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += orchestrate(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
