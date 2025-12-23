from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Literal


class PlayRequest(BaseModel):
    """Schema for a play request."""
    choice: Literal["rock", "paper", "scissors"] = Field(
        ..., description="The player's choice: rock, paper, or scissors."
    )


class PlayResponse(BaseModel):
    """Schema for a play response."""
    player: Literal["rock", "paper", "scissors"] = Field(
        ..., description="Echo of the player's choice."
    )
    computer: Literal["rock", "paper", "scissors"] = Field(
        ..., description="The computer's randomly chosen move."
    )
    result: Literal["win", "lose", "draw"] = Field(
        ..., description="The outcome from the player's perspective."
    )
