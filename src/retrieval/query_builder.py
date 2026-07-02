from src.models.integration_models import IntegrationRequest


def build_retrieval_query(
    request: IntegrationRequest,
) -> str:
    """
    Builds a focused search query for the knowledge retriever.

    The query combines structured inputs and business intent
    so ChromaDB can retrieve the most relevant architecture knowledge.
    """

    query_parts = [
        request.source_system,
        request.target_system,
        request.integration_style,
        request.operation_type,
        request.frequency,
        request.expected_volume,
        request.business_requirement,
    ]

    if request.authentication_type:
        query_parts.append(request.authentication_type)

    if request.runtime_environment:
        query_parts.append(request.runtime_environment)

    if request.mapping_complexity:
        query_parts.append(f"{request.mapping_complexity} mapping complexity")

    if request.transformation_complexity:
        query_parts.append(
            f"{request.transformation_complexity} transformation complexity"
        )

    if request.additional_constraints:
        query_parts.append(request.additional_constraints)

    return " ".join(part.strip() for part in query_parts if part and part.strip())
