from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from heimdall.governor import Governor, policy_evidence
from heimdall.models import ActionRequest, ContractRequest, EvidenceItem, ExecutionContract, VerificationRequest

app = FastAPI(title="HEIMDALL Machine Governor", version="0.2.0")
governor = Governor()


class AuthorizationRequest(BaseModel):
    contract: ExecutionContract
    action: ActionRequest


@app.get("/", response_class=HTMLResponse)
def home():
    return """<!doctype html><html><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>HEIMDALL</title><style>body{margin:0;background:#07090e;color:#eef3ff;font:15px system-ui}main{max-width:1050px;margin:auto;padding:32px}.hero,.card{border:1px solid #2b3857;border-radius:18px;padding:22px;background:#0d121d;margin-bottom:14px}h1{font-size:48px;margin:0}button{padding:12px 18px;border:0;border-radius:9px;background:#bdd1ff;font-weight:900}.deny{border-color:#8a3d49}.allow{border-color:#376a54}pre{white-space:pre-wrap}</style></head><body><main><section class=hero><small>JANUS-10 · ENTRY 05 · MACHINE GOVERNANCE</small><h1>HEIMDALL</h1><h2>No autonomous action without scope. No completion without evidence.</h2><button onclick=run()>RUN ADVERSARIAL GOVERNANCE DEMO</button></section><div id=o></div></main><script>async function run(){let j=await(await fetch('/demo',{method:'POST'})).json();o.innerHTML=`<div class='card allow'><h2>Allowed Action</h2><pre>${JSON.stringify(j.allowed,null,2)}</pre></div><div class='card deny'><h2>Denied Action</h2><pre>${JSON.stringify(j.denied,null,2)}</pre></div><div class=card><h2>Verification</h2><pre>${JSON.stringify(j.verification,null,2)}</pre></div><div class=card><h2>Contract</h2><pre>${JSON.stringify(j.contract,null,2)}</pre></div>`}</script></body></html>"""


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "heimdall-machine-governor"}


@app.post("/demo")
def demo():
    contract = governor.compile_contract(ContractRequest(objective="Repair failing tests inside the bounded workspace"))
    allowed_action = ActionRequest(contract_id=contract.contract_id, action_type="command", command="pytest -q", target="/workspace", category="test_execution")
    denied_action = ActionRequest(contract_id=contract.contract_id, action_type="command", command="rm -rf /", target="/", category="destructive_filesystem")
    allowed = governor.authorize(contract, allowed_action)
    denied = governor.authorize(contract, denied_action)
    evidence = [
        EvidenceItem(evidence_type="patch_diff", payload={"files_changed": 1, "summary": "Scoped repair candidate"}),
        EvidenceItem(evidence_type="test_results", payload={"passed": True, "tests": 12}),
        policy_evidence(allowed),
        EvidenceItem(evidence_type="model_call", payload={"provider": "deterministic-demo", "purpose": "repair-plan"}),
    ]
    verification = governor.verify(VerificationRequest(contract=contract, evidence=evidence))
    return {"contract": contract, "allowed": allowed, "denied": denied, "verification": verification}


@app.post("/v1/contracts")
def create_contract(request: ContractRequest) -> ExecutionContract:
    return governor.compile_contract(request)


@app.post("/v1/authorize")
def authorize(request: AuthorizationRequest):
    if request.action.contract_id != request.contract.contract_id:
        raise HTTPException(status_code=400, detail="contract/action mismatch")
    return governor.authorize(request.contract, request.action)


@app.post("/v1/verify")
def verify(request: VerificationRequest):
    return governor.verify(request)
