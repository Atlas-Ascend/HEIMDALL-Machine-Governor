from heimdall.models import ActionRequest, Decision, ExecutionContract
from heimdall.policy import evaluate


def test_allows_scoped_pytest():
    contract = ExecutionContract(objective="repair tests")
    action = ActionRequest(
        contract_id=contract.contract_id,
        action_type="shell",
        command="pytest -q",
    )
    assert evaluate(contract, action).decision == Decision.ALLOW


def test_denies_destructive_shell():
    contract = ExecutionContract(objective="repair tests")
    action = ActionRequest(
        contract_id=contract.contract_id,
        action_type="shell",
        command="rm -rf /",
        category="destructive_filesystem",
    )
    decision = evaluate(contract, action)
    assert decision.decision == Decision.DENY
    assert decision.reason_code == "EXPLICIT_DENY"


def test_denies_out_of_scope_write():
    contract = ExecutionContract(objective="repair tests")
    action = ActionRequest(
        contract_id=contract.contract_id,
        action_type="write",
        target="/etc/passwd",
    )
    assert evaluate(contract, action).decision == Decision.DENY
