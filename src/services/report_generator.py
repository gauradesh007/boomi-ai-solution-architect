from src.models.integration_models import ConnectorRecommendation
from src.models.integration_models import DevelopmentEstimate
from src.models.integration_models import IntegrationRequest
from src.models.integration_models import PatternRecommendation


def generate_markdown_report(
    request: IntegrationRequest,
    pattern: PatternRecommendation,
    connectors: ConnectorRecommendation,
    estimate: DevelopmentEstimate,
) -> str:
    """
    Generates a Markdown architecture report.
    """

    assumptions = "\n".join(f"- {item}" for item in estimate.assumptions)

    report = f"""
# Boomi Integration Architecture Report

## Executive Summary

This report provides a Boomi-oriented integration architecture recommendation.

---

## Requirement Summary

**Source System:** {request.source_system}

**Target System:** {request.target_system}

**Integration Style:** {request.integration_style}

**Operation Type:** {request.operation_type}

**Frequency:** {request.frequency}

**Expected Volume:** {request.expected_volume}

---

## Business Requirement

{request.business_requirement}

---

## Recommended Integration Pattern

**{pattern.pattern_name}**

{pattern.reason}

---

## Connector Strategy

Source Connector:
{connectors.source_connector}

Target Connector:
{connectors.target_connector}

Notes:

{connectors.notes}

---

## Boomi Process Flow

Start Shape
    ↓
Source Connector
    ↓
Data Validation
    ↓
Map Shape
    ↓
Target Connector
    ↓
Process Reporting

---

## Mapping Strategy

- Validate mandatory fields
- Standardize formats
- Use Map Shape
- Document mappings

---

## Error Handling

- Try/Catch
- Exception Route
- Process Reporting
- Log failed records

---

## Retry Strategy

Retry:

- Timeout
- Temporary API failures

Do NOT Retry:

- Validation errors
- Authentication errors

---

## Monitoring

- Process Reporting
- Alerts
- Execution Time
- Success Count
- Failure Count

---

## Security

- Secure Properties
- HTTPS
- OAuth
- Least Privilege

---

## Risks and Assumptions

{assumptions}

---

## Development Estimate

Complexity:
{estimate.complexity}

Development:
{estimate.development_estimate}

Testing:
{estimate.testing_estimate}

Total:
{estimate.total_estimate}

---

## Implementation Roadmap

1. Confirm requirements
2. Configure connectors
3. Build process
4. Build mappings
5. Implement error handling
6. Test
7. Deploy

---

## Final Recommendation

Proceed using the **{pattern.pattern_name}**.
"""

    return report.strip()
