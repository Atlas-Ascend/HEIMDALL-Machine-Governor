# Evidence Engine

Evidence is the bridge from autonomous action to trustworthy completion.

Each item records `execution_id`, `type`, timestamp, structured payload, and optional digest. Expected evidence classes include model_call, policy_log, command_result, patch_diff, test_results, denial, verification, and receipt.

Evidence is append-oriented. Final receipts reference evidence identifiers rather than reinterpreting the event history.

Secrets and raw credentials are never admissible evidence and must be redacted before persistence.
