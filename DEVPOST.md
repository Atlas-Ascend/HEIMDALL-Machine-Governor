# HEIMDALL — Devpost Submission Draft

## Tagline

The machine governor between autonomous AI agents and the computers they control.

## Track

Coding and Agentic Engineering.

## Inspiration

Autonomous coding agents are rapidly becoming capable of changing files, running tools, calling networks, and repairing software. The missing infrastructure is not another planner. It is a trustworthy authority boundary that can answer: what may this agent do, what did it actually do, and is the claimed result proven?

## What it does

HEIMDALL compiles an objective into an execution contract, evaluates each effectful action with deterministic policy and risk controls, permits only in-scope work, captures evidence, and requires verification before promotion. A failed proof routes to bounded repair. A prohibited action is denied and receipted.

## How we built it

The control plane is Python/FastAPI with Pydantic contracts. Reasoning is integrated through an NVIDIA open-source model served by Nebius Token Factory's OpenAI-compatible API. The final demo uses an isolated execution path appropriate to the Coding and Agentic Engineering track and records policy decisions, test outcomes, diffs, model calls, and verification state.

## Why Nebius + NVIDIA matters

The NVIDIA model is not decorative. It performs planning/repair reasoning inside a governed execution loop. Nebius Token Factory provides the hosted inference surface and the project is structured so the exact live model is discovered and pinned before submission.

## Challenge

The hard problem is separating intelligence from authority. Model output remains a proposal. The deterministic governor decides permission. That separation makes agent capability upgradeable without silently expanding machine access.

## Accomplishments

- typed execution contracts
- deterministic permit/deny decisions
- bounded repair state
- machine-verifiable evidence requirements
- final proof receipt
- competition-grade adversarial demo design

## What we learned

[Complete after live Token Factory and sandbox integration.]

## What's next

Extend the reference policy engine into container/cloud enforcement backends and support enterprise policy languages while preserving the same execution-contract and proof semantics.

## Significant updates during submission period

HEIMDALL as a competition product, its Nebius/NVIDIA integration, execution-contract implementation, policy/risk engine, demo scenario, proof model, tests, and operator surfaces are developed in this repository during the competition period. Broader architectural concepts around governed agent execution may predate the hackathon; the final submission will preserve that distinction explicitly.
