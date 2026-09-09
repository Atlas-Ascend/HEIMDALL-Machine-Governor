# Execution Engine

The execution engine is an adapter boundary, not unrestricted shell access.

Inputs: authorized ActionRequest + PolicyDecision + contract.
Outputs: EvidenceItem(s) describing result, exit status, affected paths, and digest.

Rules:

- refuse any request not carrying an ALLOW decision
- set workspace root explicitly
- capture stdout/stderr with bounded size
- impose execution timeout
- record changed file list
- never expose environment secrets to model-visible logs
- return failure as evidence, not as an exception that disappears

The competition demo should use an isolated Nebius-compatible execution environment.
