from typing import Literal

from pydantic import BaseModel

ReviewStatus = Literal["APPROVED", "NEEDS_REVISION"]


class ReviewResult(BaseModel):
    status: ReviewStatus
    score: int
    feedback: list[str]

    @property
    def approved(self) -> bool:
        return self.status == "APPROVED"
