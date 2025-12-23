from __future__ import annotations

from enum import Enum
from typing import Literal, Tuple


class Choice(str, Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


Result = Literal["win", "lose", "draw"]


# PUBLIC_INTERFACE
def evaluate_round(player: Choice, computer: Choice) -> Result:
    """Evaluate a single Rock-Paper-Scissors round.

    Args:
        player: The player's choice.
        computer: The computer's choice.

    Returns:
        Result: 'win', 'lose', or 'draw' for the player perspective.
    """
    if player == computer:
        return "draw"

    wins_over = {
        Choice.ROCK: Choice.SCISSORS,
        Choice.PAPER: Choice.ROCK,
        Choice.SCISSORS: Choice.PAPER,
    }
    return "win" if wins_over[player] == computer else "lose"


# PUBLIC_INTERFACE
def valid_choices() -> Tuple[Choice, Choice, Choice]:
    """Return the tuple of valid choices."""
    return (Choice.ROCK, Choice.PAPER, Choice.SCISSORS)
