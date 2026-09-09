# Nebius + NVIDIA Integration

HEIMDALL uses Nebius Token Factory through its OpenAI-compatible API. The default base URL is `https://api.tokenfactory.nebius.com/v1/`.

The hackathon requires at least one NVIDIA open-source model. Because hosted model catalogs can change, the repository does not invent or freeze an unverified model ID. `scripts/check_nebius_model.py` lists currently available models and filters IDs containing `nvidia` or `nemotron`. The final demo pins the selected ID in `NEBIUS_MODEL` and records it in proof.

The reasoning model is used for planning/repair generation. Authorization remains deterministic in HEIMDALL.

Official references:
- https://docs.tokenfactory.nebius.com/api-reference/introduction
- https://docs.tokenfactory.nebius.com/api-reference/models/list-models
- https://nebiusglobalaihackathon.devpost.com/rules
