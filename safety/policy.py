def review_required(action: str) -> bool:
    protected = {"misconduct_finding", "disciplinary_action", "student_record_change", "external_reporting"}
    return action in protected

def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
