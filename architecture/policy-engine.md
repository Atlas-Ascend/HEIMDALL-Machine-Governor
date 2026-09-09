# Policy Engine

Policy evaluation order:

1. malformed request -> DENY
2. explicit dangerous category -> DENY
3. target outside authorized scope -> DENY
4. command not allowlisted -> REVIEW/DENY
5. network destination outside allowlist -> DENY
6. action explicitly allowed by contract -> ALLOW

Deny rules dominate allow rules. Policy decisions include stable reason codes so tests and receipts can prove behavior without parsing prose.

The initial implementation is deterministic Python. Future policy backends may compile the same contract into OPA/Rego, Cedar, seccomp, container policy, or cloud IAM controls.
