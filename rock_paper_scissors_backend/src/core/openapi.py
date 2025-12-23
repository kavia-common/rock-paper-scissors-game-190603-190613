from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class OpenAPIMetadata:
    title: str
    description: str
    version: str
    contact: Dict[str, str]
    license_info: Dict[str, str]


def get_openapi_metadata() -> OpenAPIMetadata:
    """Return OpenAPI app-level metadata for the service."""
    return OpenAPIMetadata(
        title="Rock Paper Scissors Backend",
        description=(
            "Stateless API for playing Rock-Paper-Scissors. "
            "Designed with clean layering to support easy future persistence."
        ),
        version="1.0.0",
        contact={"name": "RPS Service", "email": "support@example.com"},
        license_info={"name": "MIT"},
    )


def get_openapi_tags() -> List[Dict[str, Any]]:
    """Return the tag definitions used across routes."""
    return [
        {"name": "Health", "description": "Health and readiness endpoints."},
        {
            "name": "Game",
            "description": "Endpoints for playing Rock-Paper-Scissors.",
        },
    ]
