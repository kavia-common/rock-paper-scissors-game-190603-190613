from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Dict

from src.domain.game import Choice, evaluate_round, valid_choices


@dataclass(frozen=True)
class PlayOutcome:
    """Value object representing the outcome of a single play."""
    player: Choice
    computer: Choice
    result: str


class GameService:
    """Application service for Rock-Paper-Scissors logic.

    Stateless by design. Future persistence (e.g., game history) can be added
    behind this service without changing the API.
    """

    # PUBLIC_INTERFACE
    def play(self, player_choice: Choice) -> PlayOutcome:
        """Play a single round, generating the computer's move.

        Args:
            player_choice: The player's chosen move.

        Returns:
            PlayOutcome: Outcome value object.
        """
        computer_choice = random.choice(list(valid_choices()))
        result = evaluate_round(player_choice, computer_choice)
        return PlayOutcome(player=player_choice, computer=computer_choice, result=result)

    # PUBLIC_INTERFACE
    def to_dict(self, outcome: PlayOutcome) -> Dict[str, str]:
        """Serialize a PlayOutcome to a simple dict for API responses."""
        return {
            "player": outcome.player.value,
            "computer": outcome.computer.value,
            "result": outcome.result,
        }
