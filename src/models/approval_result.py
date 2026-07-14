from typing import Literal

from pydantic import BaseModel

ApprovalDecision = Literal[
    "APPROVED",
    "REQUEST_CHANGES",
    "REJECTED",
]


class ApprovalResult(BaseModel):
    decision: ApprovalDecision
    comments: str = ""
