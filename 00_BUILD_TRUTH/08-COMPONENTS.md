# 08 — Components

- **Governor API**: typed external interface for contracts, authorization, and verification.
- **Contract Compiler**: converts objective plus requested scope into an execution contract.
- **Policy Engine**: deterministic rule evaluator. Explicit denies override allows.
- **Risk Engine**: classifies requested actions by consequence and blast radius.
- **Nebius Adapter**: model inference client using the Token Factory OpenAI-compatible API.
- **Agent Adapter**: requests plans or repair hypotheses from the configured NVIDIA model.
- **Sandbox Adapter**: bounded execution interface; implementation target is Token Factory Sandboxes or an equivalent Nebius-hosted isolated path allowed by the track.
- **Evidence Collector**: normalizes diffs, command results, tests, denials, and model calls.
- **Verifier**: checks proof requirements and determines PASS/REPAIR/DENY.
- **Receipt Writer**: persists a final audit record for each governed run.
