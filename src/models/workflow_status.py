from typing import Literal

from pydantic import BaseModel

WorkflowStatusValue = Literal[
    "NEW",
    "PROCESSING",
    "RETRIEVING_KNOWLEDGE",
    "GENERATING_RECOMMENDATION",
    "REVIEWING",
    "REVISING",
    "WAITING_FOR_HUMAN_APPROVAL",
    "APPROVED",
    "REQUEST_CHANGES",
    "REJECTED",
    "COMPLETED",
]


class WorkflowStatus(BaseModel):
    current_status: WorkflowStatusValue = "NEW"
    status_history: list[str] = ["NEW"]

    def move_to(
        self,
        status: WorkflowStatusValue,
    ) -> None:
        self.current_status = status
        self.status_history.append(status)
