import streamlit as st

from src.models.integration_models import ArchitectureResult


def display_architecture_result(
    result: ArchitectureResult,
) -> None:
    """
    Displays current Sprint 2 architecture result.
    """

    st.success("Architecture inputs processed successfully.")

    st.subheader("Integration Request")
    st.json(result.request.model_dump())

    st.subheader("Pattern Recommendation")
    st.json(result.pattern.model_dump())

    st.subheader("Connector Recommendation")
    st.json(result.connectors.model_dump())

    st.subheader("Development Estimate")
    st.json(result.estimate.model_dump())

    st.subheader("Retrieval Query")
    st.code(result.retrieval_query)

    with st.expander(
        "Retrieved Knowledge Packets",
        expanded=False,
    ):
        for packet in result.knowledge_packets:
            st.markdown(f"### {packet.source}")
            st.write(f"Category: {packet.category}")
            st.markdown(packet.content)

    with st.expander(
        "Knowledge Context",
        expanded=False,
    ):
        st.text(result.knowledge_context)

    if result.architecture_review:
        st.subheader("Architecture Review")

    st.metric(
        label="Review Score",
        value=result.architecture_review.score,
    )

    st.write(f"Status: {result.architecture_review.status}")
    st.write(f"Revision Count: {result.revision_count}")

    if result.architecture_review.feedback:
        st.write("Feedback:")
        for item in result.architecture_review.feedback:
            st.warning(item)

    if result.architecture_report:
        st.subheader("Architecture Report")
        st.markdown(result.architecture_report)
