# 09 — Data Contracts

Canonical objects are defined in `src/heimdall/models.py`.

## ExecutionContract

Contains contract ID, objective, filesystem allowlist, command allowlist, network allowlist, explicit deny categories, and required proof types.

## ActionRequest

Represents one proposed effectful operation: action type, target, command, metadata, and contract ID.

## PolicyDecision

Contains decision (`ALLOW`, `DENY`, `REVIEW`), reason code, human-readable rationale, risk level, and matched rule.

## EvidenceItem

Contains evidence type, timestamp, digest/reference, and structured payload.

## VerificationResult

Contains status (`PASS`, `REPAIR`, `DENY`), missing evidence, assertions evaluated, and receipt ID when finalized.

Contracts are versioned. Receipts must retain the contract version used for authorization.
