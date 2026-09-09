from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

TRACKED = [
    "README.md",
    "DEVPOST.md",
    "pyproject.toml",
    "src/heimdall/api.py",
    "src/heimdall/governor.py",
    "src/heimdall/policy.py",
    "src/heimdall/nebius.py",
]


def main() -> None:
    files = {}
    for name in TRACKED:
        path = Path(name)
        if path.exists():
            files[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    payload = {
        "generated_at": datetime.now(UTC).isoformat(),
        "artifact": "HEIMDALL-Machine-Governor",
        "files": files,
    }
    target = Path("proof/BUILD-MANIFEST.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(target)


if __name__ == "__main__":
    main()
