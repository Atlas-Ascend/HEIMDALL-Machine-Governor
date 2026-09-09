from heimdall.governor import Governor
from heimdall.models import EvidenceItem, ExecutionContract, VerificationRequest, VerificationStatus


def test_verification_requires_complete_evidence():
    governor = Governor()
    contract = ExecutionContract(objective="repair")
    result = governor.verify(
        VerificationRequest(
            contract=contract,
            evidence=[EvidenceItem(evidence_type="test_results", payload={"passed": True})],
        )
    )
    assert result.status == VerificationStatus.REPAIR
    assert "patch_diff" in result.missing_evidence


def test_verification_passes_with_required_proof():
    governor = Governor()
    contract = ExecutionContract(objective="repair")
    evidence = [
        EvidenceItem(evidence_type="patch_diff"),
        EvidenceItem(evidence_type="test_results", payload={"passed": True}),
        EvidenceItem(evidence_type="policy_log"),
        EvidenceItem(evidence_type="model_call"),
    ]
    result = governor.verify(VerificationRequest(contract=contract, evidence=evidence))
    assert result.status == VerificationStatus.PASS
    assert result.receipt_id is not None
