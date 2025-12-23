from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/", summary="Health Check", operation_id="health_check")
def health_check() -> dict:
    """Health check endpoint.

    Returns:
        dict: Simple message indicating the service is healthy.
    """
    return {"message": "Healthy"}
