from src.models.architecture_recommendation import ArchitectureRecommendation
from src.models.review_result import ReviewResult


def review_architecture(
    recommendation: ArchitectureRecommendation,
) -> ReviewResult:
    score = 100
    feedback = []

    required_fields = {
        "Executive summary": recommendation.executive_summary,
        "Pattern reasoning": recommendation.pattern_reasoning,
        "Connector reasoning": recommendation.connector_reasoning,
        "Boomi process flow": recommendation.boomi_process_flow,
        "Mapping strategy": recommendation.mapping_strategy,
        "Error handling strategy": recommendation.error_handling_strategy,
        "Retry strategy": recommendation.retry_strategy,
        "Monitoring strategy": recommendation.monitoring_strategy,
        "Security strategy": recommendation.security_strategy,
        "Final recommendation": recommendation.final_recommendation,
    }

    for name, value in required_fields.items():
        if not value or not value.strip():
            score -= 10
            feedback.append(f"{name} is missing.")

    retry_text = recommendation.retry_strategy.lower()
    error_text = recommendation.error_handling_strategy.lower()

    if "retry validation" in retry_text or "retry validation" in error_text:
        score -= 20
        feedback.append("Validation errors should not be retried.")

    if "validation errors" in retry_text and "do not retry" not in retry_text:
        score -= 15
        feedback.append(
            "Retry strategy must clearly say not to retry validation errors."
        )

    if not recommendation.risks:
        score -= 10
        feedback.append("No risks were identified.")

    if not recommendation.assumptions:
        score -= 5
        feedback.append("No assumptions were identified.")

    if not recommendation.implementation_roadmap:
        score -= 10
        feedback.append("Implementation roadmap is missing.")

    status = "APPROVED" if score >= 80 else "NEEDS_REVISION"

    return ReviewResult(
        status=status,
        score=max(score, 0),
        feedback=feedback,
    )
