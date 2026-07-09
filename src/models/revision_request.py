from pydantic import BaseModel


class RevisionRequest(BaseModel):
    feedback: list[str]
    previous_recommendation: str
    score: int
