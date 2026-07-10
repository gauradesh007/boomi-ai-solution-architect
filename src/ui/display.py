import streamlit as st

from src.models.integration_models import ArchitectureResult


def display_architecture_result(
    result: ArchitectureResult,
    mode: str = "Production",
) -> None:
    """
    Displays architecture result based on selected view mode.
    """

    if mode == "Production":
        display_production_result(result)
    else:
        display_developer_result(result)


def display_production_result(
    result: ArchitectureResult,
) -> None:
    """
    Displays clean user-facing architecture result.
    """

    st.success("Architecture report generated successfully.")

    if result.architecture_review:
        st.subheader("Architecture Review")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                label="Review Score",
                value=result.architecture_review.score,
            )

        with col2:
            st.metric(
                label="Revision Count",
                value=result.revision_count,
            )

        with col3:
            st.metric(
                label="Status",
                value=result.architecture_review.status,
            )

        if result.architecture_review.feedback:
            with st.expander("Review Feedback"):
                for item in result.architecture_review.feedback:
                    st.warning(item)

    if result.architecture_report:
        st.subheader("Architecture Report")
        st.markdown(result.architecture_report)

        st.download_button(
            label="Download Markdown Report",
            data=result.architecture_report,
            file_name="boomi_architecture_report.md",
            mime="text/markdown",
        )


def display_developer_result(
    result: ArchitectureResult,
) -> None:
    """
    Displays developer/debug view of the architecture result.
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

    if result.architecture_recommendation:
        st.subheader("Architecture Recommendation")
        st.json(result.architecture_recommendation.model_dump())

    if result.architecture_review:
        st.subheader("Architecture Review")
        st.json(result.architecture_review.model_dump())
        st.write(f"Revision Count: {result.revision_count}")

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

    if result.architecture_report:
        st.subheader("Architecture Report")
        st.markdown(result.architecture_report)

        st.download_button(
            label="Download Markdown Report",
            data=result.architecture_report,
            file_name="boomi_architecture_report.md",
            mime="text/markdown",
        )
