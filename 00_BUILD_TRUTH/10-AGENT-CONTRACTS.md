# 10 — Agent Contracts

The reasoning model has four bounded roles.

## Planner
Produces a proposed plan from the objective and visible repository state. It has no authority to execute.

## Executor
Translates an approved plan step into an ActionRequest. The Governor must authorize each effectful step before an adapter executes it.

## Repairer
Receives failed evidence and proposes the smallest corrective delta. It cannot enlarge its own authorization envelope.

## Verifier Assistant
May summarize evidence or suggest assertions, but deterministic proof gates decide promotion.

### Hard law

Model output is **proposal**, never permission. No model response can bypass explicit deny rules, mutate the contract, mark its own work as verified, or forge evidence.
