# HEIMDALL — Machine Governor

**Governed autonomous execution for coding and agentic systems.**

HEIMDALL sits between an AI agent and the machine it is allowed to operate. It converts intent into bounded execution contracts, evaluates every requested action against policy and risk, captures evidence, and requires verification before promotion.

> **No autonomous action without scope. No completion without evidence. No promotion without verification.**

## Hackathon

Target: **Nebius × NVIDIA Global AI Hackathon — Coding and Agentic Engineering Track**.

HEIMDALL is designed to use an NVIDIA open-source model through Nebius Token Factory and to govern code/test/repair work performed in bounded execution environments.

## Core loop

```text
INTENT -> CONTRACT -> POLICY -> AUTHORIZE -> EXECUTE -> EVIDENCE -> VERIFY
                                            |                    |
                                            +---- DENY ----------+
                                            +---- REPAIR --------+
```

## MVP surfaces

- execution contract compiler
- deterministic policy engine
- risk classifier
- Nebius Token Factory adapter
- evidence and receipt model
- verification gate
- FastAPI control plane
- adversarial demo scenario

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
pytest
uvicorn heimdall.api:app --reload
```

Set `NEBIUS_API_KEY` and `NEBIUS_MODEL` before using live inference. `NEBIUS_MODEL` must be an NVIDIA open-source model currently available in the entrant's Token Factory account.

## API

- `GET /health`
- `POST /v1/contracts`
- `POST /v1/authorize`
- `POST /v1/verify`

## Build truth

The canonical product contract is in [`00_BUILD_TRUTH/`](00_BUILD_TRUTH/). Competition provenance, demo requirements, and promotion gates are explicit. Nothing is considered hackathon-complete until the proof checklist passes.

## License

MIT. See [`LICENSE`](LICENSE).
