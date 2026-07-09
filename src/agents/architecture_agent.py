import json

from langchain_ollama import ChatOllama

from src.models.architecture_recommendation import ArchitectureRecommendation
from src.models.integration_models import ConnectorRecommendation
from src.models.integration_models import DevelopmentEstimate
from src.models.integration_models import IntegrationRequest
from src.models.integration_models import PatternRecommendation
from src.models.revision_request import RevisionRequest

llm = ChatOllama(
    model="llama3.2:1b",
)


def normalize_architecture_data(
    data: dict,
    pattern: PatternRecommendation,
    connectors: ConnectorRecommendation,
    estimate: DevelopmentEstimate,
) -> dict:
    """
    Normalizes imperfect LLM JSON into the required
    ArchitectureRecommendation schema.
    """

    def as_string(value, fallback: str) -> str:
        if isinstance(value, str) and value.strip():
            return value
        if value is None:
            return fallback
        return json.dumps(value, indent=2)

    def as_list(value, fallback: list[str]) -> list[str]:
        if isinstance(value, list):
            return [str(item) for item in value]
        if isinstance(value, str) and value.strip():
            return [value]
        if isinstance(value, dict):
            return [f"{key}: {val}" for key, val in value.items()]
        return fallback

    return {
        "executive_summary": as_string(
            data.get("executive_summary"),
            "Architecture recommendation generated from structured request and retrieved knowledge.",
        ),
        "pattern_reasoning": as_string(
            data.get("pattern_reasoning"),
            pattern.reason,
        ),
        "connector_reasoning": as_string(
            data.get("connector_reasoning"),
            connectors.notes,
        ),
        "boomi_process_flow": as_string(
            data.get("boomi_process_flow"),
            "Start Shape -> Source Connector -> Data Validation -> Map Shape -> Target Connector -> Process Reporting",
        ),
        "mapping_strategy": as_string(
            data.get("mapping_strategy"),
            "Use Boomi Map shape and validate mandatory fields before target submission.",
        ),
        "error_handling_strategy": as_string(
            data.get("error_handling_strategy"),
            "Use Try/Catch and route failed records to an error path.",
        ),
        "retry_strategy": as_string(
            data.get("retry_strategy"),
            "Retry transient failures only. Do not retry validation errors.",
        ),
        "monitoring_strategy": as_string(
            data.get("monitoring_strategy"),
            "Use Boomi process reporting and alerts.",
        ),
        "security_strategy": as_string(
            data.get("security_strategy"),
            "Use secure credentials and least-privilege access.",
        ),
        "scalability_considerations": as_string(
            data.get("scalability_considerations"),
            "Use batching and pagination where required.",
        ),
        "risks": as_list(
            data.get("risks"),
            ["Manual architecture review is required."],
        ),
        "assumptions": as_list(
            data.get("assumptions"),
            estimate.assumptions,
        ),
        "implementation_roadmap": as_list(
            data.get("implementation_roadmap"),
            [
                "Confirm requirements.",
                "Configure connectors.",
                "Build process flow.",
                "Implement mapping.",
                "Test and validate.",
            ],
        ),
        "final_recommendation": as_string(
            data.get("final_recommendation"),
            "Proceed after architecture review.",
        ),
    }


def generate_architecture_recommendation(
    request: IntegrationRequest,
    pattern: PatternRecommendation,
    connectors: ConnectorRecommendation,
    estimate: DevelopmentEstimate,
    knowledge_context: str,
    revision_request: RevisionRequest | None = None,
) -> ArchitectureRecommendation:
    """
    Generates structured architecture reasoning.

    The LLM returns JSON.
    This function converts that JSON into ArchitectureRecommendation.
    """

    prompt = f"""
You are a Senior Boomi Solution Architect.

Generate a structured architecture recommendation.

Use ONLY:
- the integration request
- deterministic tool outputs
- retrieved knowledge

Return ONLY valid JSON.
Do not include markdown.
Do not include explanation outside JSON.

Integration Request:
Source System: {request.source_system}
Target System: {request.target_system}
Integration Style: {request.integration_style}
Operation Type: {request.operation_type}
Frequency: {request.frequency}
Expected Volume: {request.expected_volume}
Business Requirement: {request.business_requirement}

Tool Outputs:
Recommended Pattern: {pattern.pattern_name}
Pattern Reason: {pattern.reason}
Source Connector: {connectors.source_connector}
Target Connector: {connectors.target_connector}
Connector Notes: {connectors.notes}
Complexity: {estimate.complexity}
Development Estimate: {estimate.development_estimate}
Testing Estimate: {estimate.testing_estimate}
Total Estimate: {estimate.total_estimate}

Retrieved Knowledge:
{knowledge_context}

Required JSON schema:
{{
  "executive_summary": "string",
  "pattern_reasoning": "string",
  "connector_reasoning": "string",
  "boomi_process_flow": "string",
  "mapping_strategy": "string",
  "error_handling_strategy": "string",
  "retry_strategy": "string",
  "monitoring_strategy": "string",
  "security_strategy": "string",
  "scalability_considerations": "string",
  "risks": ["string"],
  "assumptions": ["string"],
  "implementation_roadmap": ["string"],
  "final_recommendation": "string"
}}
"""
    if revision_request:
        prompt += f"""

Revision Instructions:

The previous recommendation did not pass review.

Review Score:
{revision_request.score}

Reviewer Feedback:
{revision_request.feedback}

Previous Recommendation:
{revision_request.previous_recommendation}

Revise the architecture recommendation using the reviewer feedback.
Fix only the issues mentioned by the reviewer.
Keep the output as valid JSON only.
Do not include markdown.
Do not include explanation outside JSON.
"""
    response = llm.invoke(prompt)

    try:
        data = json.loads(response.content)
    except json.JSONDecodeError:
        data = {
            "executive_summary": "The architecture recommendation could not be parsed from the AI response.",
            "pattern_reasoning": pattern.reason,
            "connector_reasoning": connectors.notes,
            "boomi_process_flow": "Use source connector, validation, mapping, target connector, and process reporting.",
            "mapping_strategy": "Use Boomi Map shape and validate mandatory fields before target submission.",
            "error_handling_strategy": "Use Try/Catch and route failed records to an error path.",
            "retry_strategy": "Retry transient failures only. Do not retry validation errors.",
            "monitoring_strategy": "Use Boomi process reporting and alerts.",
            "security_strategy": "Use secure credentials and least-privilege access.",
            "scalability_considerations": "Use batching and pagination where required.",
            "risks": [
                "AI response was not valid JSON.",
                "Manual review is required.",
            ],
            "assumptions": estimate.assumptions,
            "implementation_roadmap": [
                "Confirm requirements.",
                "Configure connectors.",
                "Build process flow.",
                "Implement mapping.",
                "Test and validate.",
            ],
            "final_recommendation": "Proceed after manual architecture review.",
        }

    normalized_data = normalize_architecture_data(
        data=data,
        pattern=pattern,
        connectors=connectors,
        estimate=estimate,
    )

    return ArchitectureRecommendation(**normalized_data)
