from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class Decision(StrEnum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    REVIEW = "REVIEW"


class RiskLevel(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class VerificationStatus(StrEnum):
    PASS = "PASS"
    REPAIR = "REPAIR"
    DENY = "DENY"


class ExecutionContract(BaseModel):
    contract_id: str = Field(default_factory=lambda: f"HC-{uuid4().hex[:12]}")
    version: str = "1"
    objective: str
    filesystem_read: list[str] = Field(default_factory=lambda: ["/workspace/**"])
    filesystem_write: list[str] = Field(default_factory=lambda: ["/workspace/**"])
    commands: list[str] = Field(default_factory=lambda: ["git", "pytest", "python", "ruff"])
    network_hosts: list[str] = Field(default_factory=list)
    denied_categories: list[str] = Field(
        default_factory=lambda: [
            "credential_access",
            "destructive_filesystem",
            "privilege_escalation",
            "production_deploy",
        ]
    )
    proof_required: list[str] = Field(
        default_factory=lambda: ["patch_diff", "test_results", "policy_log", "model_call"]
    )


class ContractRequest(BaseModel):
    objective: str
    filesystem_read: list[str] | None = None
    filesystem_write: list[str] | None = None
    commands: list[str] | None = None
    network_hosts: list[str] | None = None


class ActionRequest(BaseModel):
    contract_id: str
    action_type: str
    target: str | None = None
    command: str | None = None
    category: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class PolicyDecision(BaseModel):
    decision: Decision
    reason_code: str
    rationale: str
    risk: RiskLevel
    matched_rule: str


class EvidenceItem(BaseModel):
    evidence_id: str = Field(default_factory=lambda: f"EV-{uuid4().hex[:12]}")
    evidence_type: str
    payload: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class VerificationRequest(BaseModel):
    contract: ExecutionContract
    evidence: list[EvidenceItem]


class VerificationResult(BaseModel):
    status: VerificationStatus
    missing_evidence: list[str] = Field(default_factory=list)
    assertions: dict[str, bool] = Field(default_factory=dict)
    receipt_id: str | None = None
