# HEIMDALL — Machine Governor

**Governed autonomous execution for coding and agentic systems.**

HEIMDALL sits between an AI agent and the machine it is allowed to operate. It converts intent into bounded execution contracts, evaluates requested actions against policy and risk, captures evidence, and requires verification before promotion.

> **No autonomous action without scope. No completion without evidence. No promotion without verification.**

## JANUS-10 competition lane
Target: **IBM Bob 2.0 Hackathon**, September 25–27, 2026. The existing governor is a disclosed pre-event infrastructure baseline. Bob-specific judged functionality must be built during the event; see `COMPETITION/IBM_BOB_2.md`.

## Current executable demo
The hosted/local adversarial demo creates one bounded repair contract, evaluates a safe test action, denies a destructive filesystem action, supplies the required evidence classes, and permits promotion only after verification PASS.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
uvicorn heimdall.api:app --reload
```

API: `/v1/contracts`, `/v1/authorize`, `/v1/verify`. Judge demo: `POST /demo` or the browser UI at `/`.

## Product law
`INTENT → CONTRACT → POLICY → AUTHORIZE/DENY → EXECUTION → EVIDENCE → VERIFY → PROMOTE/REPAIR`

MIT licensed.
