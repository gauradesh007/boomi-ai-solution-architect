from typing import Literal

from pydantic import BaseModel

ReviewStatus = Literal[
    "APPROVED",
    "NEEDS_REVISION",
]


class ReviewResult(BaseModel):
    """
    Result returned by the Architecture Review Agent.
    """

    status: ReviewStatus

    score: int

    feedback: list[str]
