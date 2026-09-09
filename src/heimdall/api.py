from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from heimdall.governor import Governor
from heimdall.models import ActionRequest, ContractRequest, ExecutionContract, VerificationRequest

app = FastAPI(title="HEIMDALL Machine Governor", version="0.1.0")
governor = Governor()


class AuthorizationRequest(BaseModel):
    contract: ExecutionContract
    action: ActionRequest


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "heimdall-machine-governor"}


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
