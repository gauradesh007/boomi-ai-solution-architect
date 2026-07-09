from src.models.architecture_recommendation import (
    ArchitectureRecommendation,
)

from src.models.review_result import (
    ReviewResult,
)


def review_architecture(
    recommendation: ArchitectureRecommendation,
) -> ReviewResult:
    """
    Performs deterministic review before
    asking AI for deeper validation.
    """

    score = 100

    feedback = []

    if not recommendation.executive_summary.strip():

        score -= 10

        feedback.append("Executive Summary is missing.")

    if not recommendation.pattern_reasoning.strip():

        score -= 10

        feedback.append("Pattern reasoning is missing.")

    if not recommendation.connector_reasoning.strip():

        score -= 10

        feedback.append("Connector reasoning is missing.")

    if not recommendation.monitoring_strategy.strip():

        score -= 10

        feedback.append("Monitoring strategy is missing.")

    if not recommendation.security_strategy.strip():

        score -= 10

        feedback.append("Security strategy is missing.")

    if not recommendation.retry_strategy.strip():

        score -= 10

        feedback.append("Retry strategy is missing.")

    if recommendation.retry_strategy.lower().find("validation") != -1:

        score -= 20

        feedback.append("Validation errors should not be retried.")

    if len(recommendation.risks) == 0:

        score -= 10

        feedback.append("No risks identified.")

    status = "APPROVED" if score >= 80 else "NEEDS_REVISION"

    return ReviewResult(
        status=status,
        score=score,
        feedback=feedback,
    )
