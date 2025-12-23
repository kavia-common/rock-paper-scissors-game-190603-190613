from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CORSSettings:
    allow_origins: List[str]
    allow_credentials: bool
    allow_methods: List[str]
    allow_headers: List[str]


def get_cors_settings() -> CORSSettings:
    """Return CORS settings.

    Note:
        No env vars used per project note; centralized for easy future changes.
    """
    return CORSSettings(
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
