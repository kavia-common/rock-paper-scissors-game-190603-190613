from fastapi import APIRouter

from src.api.schemas import PlayRequest, PlayResponse
from src.domain.game import Choice
from src.services.game_service import GameService

router = APIRouter(prefix="", tags=["Game"])

_service = GameService()


@router.post(
    "/play",
    response_model=PlayResponse,
    summary="Play Rock-Paper-Scissors",
    operation_id="play_rps",
    responses={
        200: {
            "description": "The result of the game round.",
        }
    },
)
# PUBLIC_INTERFACE
def play(req: PlayRequest) -> PlayResponse:
    """Play a round of Rock-Paper-Scissors.

    Parameters:
        req (PlayRequest): Body containing the player's choice string in {'rock'|'paper'|'scissors'}.

    Returns:
        PlayResponse: JSON with fields:
            - player: str, echo of player's choice
            - computer: str, randomly chosen move
            - result: str, one of {'win','lose','draw'} from player's perspective
    """
    outcome = _service.play(Choice(req.choice))
    return PlayResponse(**_service.to_dict(outcome))
