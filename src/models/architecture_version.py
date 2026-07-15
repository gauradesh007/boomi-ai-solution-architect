from datetime import datetime

from pydantic import BaseModel

from src.models.architecture_recommendation import ArchitectureRecommendation
from src.models.approval_result import ApprovalResult
from src.models.review_result import ReviewResult


class ArchitectureVersion(BaseModel):
    version: int
    created_at: datetime
    recommendation: ArchitectureRecommendation
    review: ReviewResult
    approval: ApprovalResult | None = None
