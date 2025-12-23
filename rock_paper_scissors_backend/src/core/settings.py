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

    CORS policy:
        - Explicitly allow the React frontend on http://localhost:3000
        - Also permit common localhost variations and 127.0.0.1 to support local dev
        - Keep credentials enabled and allow all methods/headers
    """
    allowed_frontend_origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://localhost:3000",
        "https://127.0.0.1:3000",
    ]
    return CORSSettings(
        allow_origins=allowed_frontend_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
