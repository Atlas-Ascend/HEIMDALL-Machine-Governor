from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def new_receipt_id() -> str:
    return f"HG-{datetime.now(timezone.utc):%Y%m%d}-{uuid4().hex[:8]}"


def persist_receipt(receipt_id: str, payload: dict) -> Path:
    root = Path(os.getenv("HEIMDALL_RECEIPT_DIR", "proof/runtime"))
    root.mkdir(parents=True, exist_ok=True)
    target = root / f"{receipt_id}.json"
    target.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return target
