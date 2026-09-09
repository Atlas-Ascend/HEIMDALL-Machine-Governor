from __future__ import annotations

from heimdall.models import (
    ActionRequest,
    ContractRequest,
    EvidenceItem,
    ExecutionContract,
    PolicyDecision,
    VerificationRequest,
    VerificationResult,
    VerificationStatus,
)
from heimdall.policy import evaluate
from heimdall.receipts import new_receipt_id


class Governor:
    def compile_contract(self, request: ContractRequest) -> ExecutionContract:
        data = {"objective": request.objective}
        for field in ("filesystem_read", "filesystem_write", "commands", "network_hosts"):
            value = getattr(request, field)
            if value is not None:
                data[field] = value
        return ExecutionContract(**data)

    def authorize(self, contract: ExecutionContract, action: ActionRequest) -> PolicyDecision:
        return evaluate(contract, action)

    def verify(self, request: VerificationRequest) -> VerificationResult:
        present = {item.evidence_type for item in request.evidence}
        required = set(request.contract.proof_required)
        missing = sorted(required - present)
        tests = [item for item in request.evidence if item.evidence_type == "test_results"]
        tests_pass = bool(tests) and all(bool(item.payload.get("passed")) for item in tests)
        assertions = {
            "required_evidence_present": not missing,
            "tests_pass": tests_pass,
        }
        if missing or not tests_pass:
            return VerificationResult(
                status=VerificationStatus.REPAIR,
                missing_evidence=missing,
                assertions=assertions,
            )
        return VerificationResult(
            status=VerificationStatus.PASS,
            missing_evidence=[],
            assertions=assertions,
            receipt_id=new_receipt_id(),
        )


def policy_evidence(decision: PolicyDecision) -> EvidenceItem:
    return EvidenceItem(evidence_type="policy_log", payload=decision.model_dump(mode="json"))
