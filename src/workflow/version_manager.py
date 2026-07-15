from datetime import datetime

from src.models.approval_result import ApprovalResult
from src.models.architecture_recommendation import (
    ArchitectureRecommendation,
)
from src.models.architecture_version import (
    ArchitectureVersion,
)
from src.models.review_result import ReviewResult


class VersionManager:
    """
    Creates architecture versions.

    This class is intentionally stateless.
    The caller owns the version history.
    """

    def create_version(
        self,
        version_number: int,
        recommendation: ArchitectureRecommendation,
        review: ReviewResult,
        approval: ApprovalResult | None = None,
    ) -> ArchitectureVersion:

        return ArchitectureVersion(
            version=version_number,
            created_at=datetime.now(),
            recommendation=recommendation,
            review=review,
            approval=approval,
        )
