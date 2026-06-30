from src.models.integration_models import DevelopmentEstimate
from src.models.integration_models import IntegrationRequest


def estimate_complexity(
    request: IntegrationRequest,
) -> DevelopmentEstimate:
    """
    Estimates integration complexity and rough effort
    using deterministic rules.
    """

    score = 0
    assumptions = []

    # Integration style
    if request.integration_style == "API / Real-Time":
        score += 2
        assumptions.append(
            "Real-time integrations require lower latency and stronger error handling."
        )

    elif request.integration_style == "Event-Driven":
        score += 3
        assumptions.append(
            "Event-driven integrations require asynchronous design and event handling."
        )

    elif request.integration_style == "Batch / Scheduled":
        score += 1
        assumptions.append(
            "Batch integrations are usually simpler when scheduling and volume are clear."
        )

    elif request.integration_style == "Hybrid":
        score += 4
        assumptions.append(
            "Hybrid integrations usually require multiple design patterns."
        )

    # Operation type
    if request.operation_type == "Upsert":
        score += 2
        assumptions.append(
            "Upsert requires matching logic such as external ID or unique key handling."
        )

    elif request.operation_type in ["Synchronize", "Delete"]:
        score += 3
        assumptions.append(
            "Synchronization or delete operations require stronger data governance."
        )

    else:
        score += 1

    # Volume
    volume = request.expected_volume.lower()

    if "million" in volume or "500,000" in volume or "large" in volume:
        score += 4
        assumptions.append(
            "High data volume may require batching, pagination, and performance tuning."
        )

    elif "100,000" in volume or "50,000" in volume:
        score += 2
        assumptions.append(
            "Moderate data volume may require batching and process monitoring."
        )

    else:
        score += 1

    # Mapping complexity
    if request.mapping_complexity == "High":
        score += 3
        assumptions.append(
            "High mapping complexity increases development and testing effort."
        )

    elif request.mapping_complexity == "Medium":
        score += 2
        assumptions.append(
            "Medium mapping complexity requires careful field mapping validation."
        )

    elif request.mapping_complexity == "Low":
        score += 1

    # Transformation complexity
    if request.transformation_complexity == "High":
        score += 3
        assumptions.append(
            "High transformation complexity may require custom logic or multiple maps."
        )

    elif request.transformation_complexity == "Medium":
        score += 2
        assumptions.append(
            "Medium transformation complexity requires additional validation."
        )

    elif request.transformation_complexity == "Low":
        score += 1

    # Determine complexity and estimate
    if score <= 5:
        complexity = "Low"
        development_estimate = "2-4 business days"
        testing_estimate = "1-2 business days"
        total_estimate = "3-6 business days"

    elif score <= 10:
        complexity = "Medium"
        development_estimate = "5-8 business days"
        testing_estimate = "3-5 business days"
        total_estimate = "8-13 business days"

    elif score <= 15:
        complexity = "High"
        development_estimate = "9-15 business days"
        testing_estimate = "5-8 business days"
        total_estimate = "14-23 business days"

    else:
        complexity = "Very High"
        development_estimate = "Requires detailed estimation"
        testing_estimate = "Requires detailed estimation"
        total_estimate = "Requires solution review"

    if not assumptions:
        assumptions.append("Estimate is based on available structured inputs.")

    return DevelopmentEstimate(
        complexity=complexity,
        development_estimate=development_estimate,
        testing_estimate=testing_estimate,
        total_estimate=total_estimate,
        assumptions=assumptions,
    )
