import streamlit as st

from src.models.integration_models import ArchitectureResult


def display_architecture_result(
    result: ArchitectureResult,
    mode: str = "Production",
) -> None:
    if "Production" in mode:
        display_production_result(result)
    else:
        display_developer_result(result)


def display_production_result(
    result: ArchitectureResult,
) -> None:
    st.success("Architecture recommendation successfully generated and reviewed.")

    st.subheader("Architecture Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Source", result.request.source_system)

    with col2:
        st.metric("Target", result.request.target_system)

    with col3:
        st.metric("Pattern", result.pattern.pattern_name)

    with col4:
        st.metric("Complexity", result.estimate.complexity)

    st.divider()

    if result.architecture_review:
        st.subheader("Review Dashboard")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Review Score",
                f"{result.architecture_review.score}/100",
            )

        with col2:
            st.metric(
                "Status",
                result.architecture_review.status,
            )

        with col3:
            st.metric(
                "Revisions",
                result.revision_count,
            )

        if result.architecture_review.feedback:
            with st.expander("Review Feedback"):
                for item in result.architecture_review.feedback:
                    st.warning(item)

    st.divider()

    if result.architecture_report:
        st.subheader("Architecture Report")
        st.markdown(result.architecture_report)

        st.download_button(
            label="Download Markdown Report",
            data=result.architecture_report,
            file_name="boomi_architecture_report.md",
            mime="text/markdown",
        )
    st.divider()
    display_human_approval(result)


def display_developer_result(
    result: ArchitectureResult,
) -> None:
    st.success("Developer view generated successfully.")

    st.subheader("Architecture Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Source", result.request.source_system)

    with col2:
        st.metric("Target", result.request.target_system)

    with col3:
        st.metric("Pattern", result.pattern.pattern_name)

    with col4:
        st.metric("Complexity", result.estimate.complexity)

    st.divider()

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

    with st.expander("Retrieved Knowledge Packets", expanded=False):
        for packet in result.knowledge_packets:
            st.markdown(f"### {packet.source}")
            st.write(f"Category: {packet.category}")
            st.markdown(packet.content)

    with st.expander("Knowledge Context", expanded=False):
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
    st.divider()
    display_human_approval(result)


def display_human_approval(
    result: ArchitectureResult,
) -> None:
    st.subheader("Human Approval")

    decision = st.radio(
        "Decision",
        [
            "APPROVED",
            "REQUEST_CHANGES",
            "REJECTED",
        ],
        horizontal=True,
    )

    comments = st.text_area(
        "Approval Comments",
        placeholder="Add comments or requested changes here.",
    )

    if st.button(
        "Submit Human Decision",
        use_container_width=True,
    ):
        st.session_state["human_approval"] = {
            "decision": decision,
            "comments": comments,
        }

        if decision == "APPROVED":
            st.success("Architecture approved by human reviewer.")
        elif decision == "REQUEST_CHANGES":
            st.warning("Changes requested by human reviewer.")
        else:
            st.error("Architecture rejected by human reviewer.")
