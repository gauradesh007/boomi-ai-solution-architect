from langchain_ollama import ChatOllama

from src.models.integration_models import ConnectorRecommendation
from src.models.integration_models import DevelopmentEstimate
from src.models.integration_models import IntegrationRequest
from src.models.integration_models import PatternRecommendation

llm = ChatOllama(
    model="llama3.2:1b",
)


def generate_architecture_report(
    request: IntegrationRequest,
    pattern: PatternRecommendation,
    connectors: ConnectorRecommendation,
    estimate: DevelopmentEstimate,
    knowledge_context: str,
) -> str:
    """
    Generates a Boomi architecture report using:
    - structured user request
    - deterministic tool outputs
    - retrieved knowledge context
    """

    prompt = f"""
You are a Senior Boomi Solution Architect.

Create a professional Boomi integration architecture report.

Use the following information.

Integration Request:
Source System: {request.source_system}
Target System: {request.target_system}
Integration Style: {request.integration_style}
Operation Type: {request.operation_type}
Frequency: {request.frequency}
Expected Volume: {request.expected_volume}
Authentication Type: {request.authentication_type}
Runtime Environment: {request.runtime_environment}

Business Requirement:
{request.business_requirement}

Additional Constraints:
{request.additional_constraints}

Recommended Pattern:
{pattern.pattern_name}

Pattern Reason:
{pattern.reason}

Connector Recommendation:
Source Connector: {connectors.source_connector}
Target Connector: {connectors.target_connector}
Connector Notes: {connectors.notes}

Development Estimate:
Complexity: {estimate.complexity}
Development Estimate: {estimate.development_estimate}
Testing Estimate: {estimate.testing_estimate}
Total Estimate: {estimate.total_estimate}
Assumptions: {estimate.assumptions}

Retrieved Knowledge:
{knowledge_context}

Instructions:
- Use the retrieved knowledge where relevant.
- Do not invent unsupported connector capabilities.
- Keep the architecture implementation-oriented.
- Use Boomi terminology.
- Include practical guidance for development and testing.
- Return Markdown only.

Return exactly these sections:

1. Executive Summary
2. Requirement Summary
3. Recommended Integration Pattern
4. Source System
5. Target System
6. Boomi Process Flow
7. Connector Strategy
8. Mapping Strategy
9. Error Handling Strategy
10. Retry Strategy
11. Monitoring and Logging
12. Security Considerations
13. Risks and Assumptions
14. Scalability Considerations
15. Development and Testing Estimate
16. Implementation Roadmap
17. Final Recommendation
"""

    response = llm.invoke(prompt)

    return response.content
