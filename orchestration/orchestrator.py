from AGENTS.authorship_signal_agent import run as a
from AGENTS.citation_verification_agent import run as b
from AGENTS.evidence_review_agent import run as c
from AGENTS.policy_mapping_agent import run as d
from AGENTS.adjudication_support_agent import run as e
def orchestrate(context): return [a(context),b(context),c(context),d(context),e(context)]
