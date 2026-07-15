import streamlit as st

from src.models.integration_models import IntegrationRequest


def get_index(
    options: list[str],
    value: str | None,
    default: str,
) -> int:
    """
    Returns safe index for Streamlit selectbox.
    """

    selected_value = value or default

    if selected_value in options:
        return options.index(selected_value)

    return options.index(default)


def build_request_form(
    default_values: dict | None = None,
) -> IntegrationRequest | None:
    """
    Renders the integration request form.

    Returns IntegrationRequest when submitted.
    """
    defaults = default_values or {}

    source_options = [
        "Local Database",
        "Salesforce",
        "SAP",
        "REST API",
        "SFTP",
        "Workday",
        "Snowflake",
        "Oracle",
        "SQL Server",
        "PostgreSQL",
        "Custom",
    ]

    with st.form("integration_request_form"):
        st.subheader("Integration Requirement")

        st.markdown("### 1. Source and Target Systems")

        col1, col2 = st.columns(2)

        with col1:
            source_system = st.selectbox(
                "Source System",
                source_options,
                index=get_index(
                    source_options,
                    defaults.get("source_system"),
                    "Local Database",
                ),
            )

        with col2:
            target_system = st.selectbox(
                "Target System",
                [
                    "Salesforce",
                    "SAP",
                    "Local Database",
                    "REST API",
                    "SFTP",
                    "Workday",
                    "Snowflake",
                    "Oracle",
                    "SQL Server",
                    "PostgreSQL",
                    "Custom",
                ],
            )

        st.markdown("### 2. Integration Settings")

        col3, col4 = st.columns(2)

        with col3:
            integration_style = st.selectbox(
                "Integration Style",
                [
                    "API / Real-Time",
                    "Event-Driven",
                    "Batch / Scheduled",
                    "Hybrid",
                ],
            )

            frequency = st.selectbox(
                "Frequency",
                [
                    "Real-Time",
                    "Hourly",
                    "Daily",
                    "Weekly",
                    "Monthly",
                    "On Demand",
                ],
            )

            expected_volume = st.text_input(
                "Expected Volume",
                value="50,000 records/day",
                help="Example: 10,000 records/day, 500,000 records/month, low volume, high volume",
            )

        with col4:
            operation_type = st.selectbox(
                "Operation Type",
                [
                    "Create",
                    "Update",
                    "Upsert",
                    "Delete",
                    "Synchronize",
                    "Extract",
                    "Load",
                    "Transform",
                ],
            )

            authentication_type = st.selectbox(
                "Authentication Type",
                [
                    "OAuth2",
                    "Basic",
                    "API Key",
                    "Mutual TLS",
                    "Certificate",
                    "Not Sure",
                ],
            )

            runtime_environment = st.selectbox(
                "Runtime Environment",
                [
                    "Atom",
                    "Molecule",
                    "Boomi Atom Cloud",
                    "Not Sure",
                ],
            )

        st.markdown("### 3. Complexity Inputs")

        col5, col6 = st.columns(2)

        with col5:
            mapping_complexity = st.selectbox(
                "Mapping Complexity",
                [
                    "Low",
                    "Medium",
                    "High",
                    "Very High",
                ],
                index=1,
            )

        with col6:
            transformation_complexity = st.selectbox(
                "Transformation Complexity",
                [
                    "Low",
                    "Medium",
                    "High",
                    "Very High",
                ],
                index=1,
            )

        st.markdown("### 4. Business Requirement")

        business_requirement = st.text_area(
            "Business Requirement (Plain English)",
            value=(
                "Synchronize customer master data from the on-premise "
                "database to Salesforce every night using batch processing."
            ),
            height=140,
            help="Describe what the integration should achieve in business terms.",
        )

        additional_constraints = st.text_area(
            "Additional Constraints",
            value="Must complete before business hours.",
            height=100,
            help="Examples: SLA, timing, compliance, security, or operational constraints.",
        )

        submitted = st.form_submit_button(
            "Generate Architecture Recommendation",
            use_container_width=True,
        )

    if not submitted:
        return None

    return IntegrationRequest(
        source_system=source_system,
        target_system=target_system,
        integration_style=integration_style,
        operation_type=operation_type,
        frequency=frequency,
        expected_volume=expected_volume,
        authentication_type=authentication_type,
        runtime_environment=runtime_environment,
        mapping_complexity=mapping_complexity,
        transformation_complexity=transformation_complexity,
        business_requirement=business_requirement,
        additional_constraints=additional_constraints,
    )
