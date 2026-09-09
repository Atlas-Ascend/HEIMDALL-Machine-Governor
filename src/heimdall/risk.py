from heimdall.models import ActionRequest, RiskLevel

CRITICAL_CATEGORIES = {
    "credential_access",
    "destructive_filesystem",
    "privilege_escalation",
    "production_deploy",
}

HIGH_RISK_TOKENS = (
    "rm -rf",
    "sudo ",
    "chmod 777",
    "/etc/shadow",
    ".ssh/",
    "printenv",
    "env |",
)


def classify_risk(action: ActionRequest) -> RiskLevel:
    if action.category in CRITICAL_CATEGORIES:
        return RiskLevel.CRITICAL
    command = (action.command or "").lower()
    if any(token in command for token in HIGH_RISK_TOKENS):
        return RiskLevel.CRITICAL
    if action.action_type in {"shell", "network", "write"}:
        return RiskLevel.MEDIUM
    return RiskLevel.LOW
