from __future__ import annotations

from pathlib import PurePosixPath

from heimdall.models import ActionRequest, Decision, ExecutionContract, PolicyDecision, RiskLevel
from heimdall.risk import classify_risk


def _command_name(command: str | None) -> str:
    return (command or "").strip().split(" ", 1)[0]


def _path_allowed(target: str | None, scopes: list[str]) -> bool:
    if target is None:
        return True
    target_path = PurePosixPath(target)
    for scope in scopes:
        prefix = scope.removesuffix("/**").rstrip("/")
        if str(target_path) == prefix or str(target_path).startswith(prefix + "/"):
            return True
    return False


def evaluate(contract: ExecutionContract, action: ActionRequest) -> PolicyDecision:
    risk = classify_risk(action)

    if action.contract_id != contract.contract_id:
        return PolicyDecision(
            decision=Decision.DENY,
            reason_code="CONTRACT_MISMATCH",
            rationale="Action does not belong to this execution contract.",
            risk=RiskLevel.HIGH,
            matched_rule="contract.identity",
        )

    if action.category in contract.denied_categories or risk == RiskLevel.CRITICAL:
        return PolicyDecision(
            decision=Decision.DENY,
            reason_code="EXPLICIT_DENY",
            rationale="Action matches a prohibited or critical-risk category.",
            risk=risk,
            matched_rule="policy.explicit_deny",
        )

    if action.action_type in {"write", "read"}:
        scopes = contract.filesystem_write if action.action_type == "write" else contract.filesystem_read
        if not _path_allowed(action.target, scopes):
            return PolicyDecision(
                decision=Decision.DENY,
                reason_code="PATH_OUT_OF_SCOPE",
                rationale="Filesystem target is outside the contract scope.",
                risk=RiskLevel.HIGH,
                matched_rule="filesystem.scope",
            )

    if action.action_type == "shell":
        command_name = _command_name(action.command)
        if command_name not in contract.commands:
            return PolicyDecision(
                decision=Decision.DENY,
                reason_code="COMMAND_NOT_ALLOWED",
                rationale=f"Command '{command_name}' is not in the contract allowlist.",
                risk=RiskLevel.HIGH,
                matched_rule="shell.allowlist",
            )

    return PolicyDecision(
        decision=Decision.ALLOW,
        reason_code="WITHIN_CONTRACT",
        rationale="Action is within the contract authorization envelope.",
        risk=risk,
        matched_rule="contract.allow",
    )
