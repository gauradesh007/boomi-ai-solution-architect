from src.models.review_result import ReviewResult
from src.models.revision_request import RevisionRequest
from src.models.architecture_recommendation import (
    ArchitectureRecommendation,
)


def build_revision_request(
    recommendation: ArchitectureRecommendation,
    review: ReviewResult,
) -> RevisionRequest:
    """
    Converts review feedback into
    an Architecture Agent revision request.
    """

    return RevisionRequest(
        feedback=review.feedback,
        previous_recommendation=recommendation.model_dump_json(indent=2),
        score=review.score,
    )
