from orchestration.orchestrator import orchestrate

REFERENCE_CONTEXT = {
    "submission": "demo",
    "policy_context": "institutional",
    "submission_context_reviewed": True,
    "evidence_provenance_reviewed": True,
    "authorship_signal_reviewed": True,
    "citation_verification_reviewed": True,
    "policy_mapping_reviewed": True,
    "due_process_reviewed": True,
    "privacy_reviewed": True,
    "human_adjudicator_approval": True,
}

if __name__ == "__main__":
    print(orchestrate(REFERENCE_CONTEXT))
