# 13 — Verification

Verification is a separate state transition after execution.

Default code-repair proof requirements:

- `patch_diff`
- `test_results`
- `policy_log`
- `model_call`

A run passes only when all required evidence types are present and test evidence reports success. Missing evidence produces `REPAIR`; prohibited behavior produces `DENY`.

The verifier does not trust an agent statement such as "tests pass." It evaluates machine-produced evidence. The demo must show the proof inventory and the final decision.

Promotion eligibility is derived exclusively from verification state `PASS` plus a persisted receipt.
