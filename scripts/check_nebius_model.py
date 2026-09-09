from heimdall.nebius import NebiusClient


def main() -> None:
    client = NebiusClient()
    matches = [
        model for model in client.list_models()
        if "nvidia" in model.lower() or "nemotron" in model.lower()
    ]
    if not matches:
        raise SystemExit("No NVIDIA/Nemotron model found in current Token Factory model list")
    print("Current NVIDIA/Nemotron candidates:")
    for model in matches:
        print(f"- {model}")
    if client.model not in matches:
        raise SystemExit(f"Configured NEBIUS_MODEL is not a current NVIDIA/Nemotron candidate: {client.model}")
    print(f"PINNED_OK={client.model}")


if __name__ == "__main__":
    main()
