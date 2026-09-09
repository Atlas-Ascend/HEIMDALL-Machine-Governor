# 11 — Security

Security posture is deny-by-default for high-impact categories.

Baseline blocked classes:

- destructive filesystem operations outside ephemeral workspace
- credential discovery or export
- privilege escalation
- arbitrary production deployment
- access to unapproved network destinations
- mutation outside contract path scope
- disabling the governor, verifier, or evidence recorder
- editing proof receipts after finalization

The MVP's Python policy layer is a reference enforcement plane, not a substitute for OS/container isolation. Real execution must combine HEIMDALL policy with sandbox-level isolation.

Secrets are supplied only through server-side environment variables. They are never committed, returned to clients, or placed into model prompts.
