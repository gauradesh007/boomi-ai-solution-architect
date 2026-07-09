from src.models.architecture_recommendation import ArchitectureRecommendation
from src.models.integration_models import ArchitectureResult


def generate_architecture_markdown_report(
    result: ArchitectureResult,
) -> str:
    """
    Converts ArchitectureRecommendation into a Markdown report.
    """

    if not result.architecture_recommendation:
        return "# Architecture Report\n\nNo architecture recommendation is available."

    recommendation: ArchitectureRecommendation = result.architecture_recommendation

    risks = "\n".join(f"- {risk}" for risk in recommendation.risks)

    assumptions = "\n".join(
        f"- {assumption}" for assumption in recommendation.assumptions
    )

    roadmap = "\n".join(
        f"{index}. {step}"
        for index, step in enumerate(
            recommendation.implementation_roadmap,
            start=1,
        )
    )

    return f"""
# Boomi Integration Architecture Report

## 1. Executive Summary

{recommendation.executive_summary}

## 2. Requirement Summary

- Source System: {result.request.source_system}
- Target System: {result.request.target_system}
- Integration Style: {result.request.integration_style}
- Operation Type: {result.request.operation_type}
- Frequency: {result.request.frequency}
- Expected Volume: {result.request.expected_volume}

Business Requirement:

{result.request.business_requirement}

## 3. Recommended Integration Pattern

{result.pattern.pattern_name}

{recommendation.pattern_reasoning}

## 4. Connector Strategy

- Source Connector: {result.connectors.source_connector}
- Target Connector: {result.connectors.target_connector}

{recommendation.connector_reasoning}

## 5. Boomi Process Flow

{recommendation.boomi_process_flow}

## 6. Mapping Strategy

{recommendation.mapping_strategy}

## 7. Error Handling Strategy

{recommendation.error_handling_strategy}

## 8. Retry Strategy

{recommendation.retry_strategy}

## 9. Monitoring and Logging

{recommendation.monitoring_strategy}

## 10. Security Considerations

{recommendation.security_strategy}

## 11. Scalability Considerations

{recommendation.scalability_considerations}

## 12. Risks

{risks}

## 13. Assumptions

{assumptions}

## 14. Development and Testing Estimate

- Complexity: {result.estimate.complexity}
- Development Estimate: {result.estimate.development_estimate}
- Testing Estimate: {result.estimate.testing_estimate}
- Total Estimate: {result.estimate.total_estimate}

## 15. Implementation Roadmap

{roadmap}

## 16. Final Recommendation

{recommendation.final_recommendation}
""".strip()
