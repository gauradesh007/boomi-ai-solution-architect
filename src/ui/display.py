import streamlit as st

from src.models.integration_models import ConnectorRecommendation
from src.models.integration_models import DevelopmentEstimate
from src.models.integration_models import IntegrationRequest
from src.models.integration_models import KnowledgePacket
from src.models.integration_models import PatternRecommendation


def display_debug_results(
    request: IntegrationRequest,
    pattern: PatternRecommendation,
    connectors: ConnectorRecommendation,
    estimate: DevelopmentEstimate,
    query: str,
    knowledge_packets: list[KnowledgePacket],
    knowledge_context: str,
) -> None:
    """
    Displays Sprint 2 debug output.
    """

    st.success("Architecture inputs processed successfully.")

    st.subheader("Integration Request")
    st.json(request.model_dump())

    st.subheader("Pattern Recommendation")
    st.json(pattern.model_dump())

    st.subheader("Connector Recommendation")
    st.json(connectors.model_dump())

    st.subheader("Development Estimate")
    st.json(estimate.model_dump())

    st.subheader("Retrieval Query")
    st.code(query)

    with st.expander("Retrieved Knowledge Packets", expanded=False):
        for packet in knowledge_packets:
            st.markdown(f"### {packet.source}")
            st.write(f"Category: {packet.category}")
            st.markdown(packet.content)

    with st.expander("Knowledge Context", expanded=False):
        st.text(knowledge_context)
