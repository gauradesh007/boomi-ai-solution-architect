from src.models.architecture_recommendation import ArchitectureRecommendation
from src.models.review_result import ReviewResult
from src.models.revision_request import RevisionRequest


def build_revision_request(
    recommendation: ArchitectureRecommendation,
    review: ReviewResult,
) -> RevisionRequest:
    return RevisionRequest(
        feedback=review.feedback,
        previous_recommendation=recommendation.model_dump_json(indent=2),
        score=review.score,
    )
