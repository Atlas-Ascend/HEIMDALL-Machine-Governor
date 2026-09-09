from __future__ import annotations

import os

from openai import OpenAI

DEFAULT_BASE_URL = "https://api.tokenfactory.nebius.com/v1/"


class NebiusClient:
    def __init__(self) -> None:
        api_key = os.getenv("NEBIUS_API_KEY")
        if not api_key:
            raise RuntimeError("NEBIUS_API_KEY is required for live inference")
        self.model = os.getenv("NEBIUS_MODEL", "").strip()
        if not self.model:
            raise RuntimeError("NEBIUS_MODEL must be set to a current NVIDIA open-source model ID")
        self.client = OpenAI(
            base_url=os.getenv("NEBIUS_BASE_URL", DEFAULT_BASE_URL),
            api_key=api_key,
        )

    def list_models(self) -> list[str]:
        return [model.id for model in self.client.models.list().data]

    def reason(self, system: str, user: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content or ""
