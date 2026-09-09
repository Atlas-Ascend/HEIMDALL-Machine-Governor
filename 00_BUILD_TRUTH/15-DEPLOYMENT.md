# 15 — Deployment

The API is a standard ASGI service and can run locally or on a supported cloud runtime.

Competition architecture should ensure the working project satisfies the official runtime condition: real Token Factory inference or execution/deployment on Nebius AI Cloud.

Environment contract:

- `NEBIUS_API_KEY` — secret, server side only
- `NEBIUS_BASE_URL` — default Token Factory `/v1/` endpoint
- `NEBIUS_MODEL` — current NVIDIA open-source model ID selected from the live account
- `HEIMDALL_RECEIPT_DIR` — writable receipt path

Production/demo deployment must expose `/health` and preserve evidence between the start and end of a judged demo session. No API key may appear in browser-delivered code.
