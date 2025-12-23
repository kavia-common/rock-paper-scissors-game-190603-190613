from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers import health, game
from src.core.settings import get_cors_settings
from src.core.openapi import get_openapi_metadata, get_openapi_tags


# PUBLIC_INTERFACE
def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance.

    Returns:
        FastAPI: Configured FastAPI app with CORS, routes, and OpenAPI metadata.
    """
    metadata = get_openapi_metadata()
    app = FastAPI(
        title=metadata.title,
        description=metadata.description,
        version=metadata.version,
        contact=metadata.contact,
        license_info=metadata.license_info,
        openapi_tags=get_openapi_tags(),
    )

    # CORS
    cors = get_cors_settings()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors.allow_origins,
        allow_credentials=cors.allow_credentials,
        allow_methods=cors.allow_methods,
        allow_headers=cors.allow_headers,
    )

    # Routers
    app.include_router(health.router)
    app.include_router(game.router)

    return app
