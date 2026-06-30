from src.models.integration_models import IntegrationRequest
from src.models.integration_models import PatternRecommendation


def select_integration_pattern(
    request: IntegrationRequest,
) -> PatternRecommendation:
    """
    Selects an integration pattern using deterministic rules.
    """

    style = request.integration_style
    frequency = request.frequency
    volume = request.expected_volume.lower()
    operation = request.operation_type

    if style == "API / Real-Time" or frequency == "Real-Time":
        return PatternRecommendation(
            pattern_name="API-Led Real-Time Integration",
            reason=(
                "The integration requires real-time or request-response "
                "communication, so an API-led pattern is recommended."
            ),
        )

    if style == "Event-Driven":
        return PatternRecommendation(
            pattern_name="Event-Driven Integration",
            reason=(
                "The integration is event-based, so an asynchronous "
                "event-driven pattern is recommended."
            ),
        )

    if style == "Batch / Scheduled":
        return PatternRecommendation(
            pattern_name="Batch / Scheduled Integration",
            reason=(
                "The integration runs on a schedule, so a batch-oriented "
                "processing pattern is recommended."
            ),
        )

    if "500,000" in volume or "million" in volume or "large" in volume:
        return PatternRecommendation(
            pattern_name="High-Volume Batch Integration",
            reason=(
                "The expected volume appears high, so a scalable batch "
                "processing pattern is recommended."
            ),
        )

    if operation == "Synchronize":
        return PatternRecommendation(
            pattern_name="System Synchronization Pattern",
            reason=(
                "The operation requires keeping systems aligned, so a "
                "synchronization pattern is recommended."
            ),
        )

    return PatternRecommendation(
        pattern_name="Hybrid Integration Pattern",
        reason=(
            "The requirements suggest a combination of integration approaches, "
            "so a hybrid pattern is recommended."
        ),
    )
