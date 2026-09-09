# 07 — Architecture

```text
Client / Operator
      |
      v
HEIMDALL API
      |
      +--> Contract Compiler
      +--> Policy Engine
      +--> Risk Engine
      |
      v
Authorization Envelope
      |
      v
Agent Runtime ----> Nebius Token Factory ----> NVIDIA Model
      |
      v
Sandbox / Tool Adapter
      |
      v
Evidence Collector
      |
      v
Verifier ---- PASS ---> Receipt ---> Promotion Eligible
   |          |
   |          +-- FAIL ---> Repair request
   +-- DENY -------------> Receipt
```

The policy plane is deterministic and independent of the reasoning model. The model can propose actions; it cannot grant itself authority. Execution and evidence are treated as separate concerns. Verification evaluates evidence against the contract's proof requirements.

See `/architecture` for component contracts.
