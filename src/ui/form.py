import streamlit as st

from src.models.integration_models import IntegrationRequest

SOURCE_TARGET_OPTIONS = [
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

INTEGRATION_STYLE_OPTIONS = [
    "API / Real-Time",
    "Event-Driven",
    "Batch / Scheduled",
    "Hybrid",
]

FREQUENCY_OPTIONS = [
    "Real-Time",
    "Hourly",
    "Daily",
    "Weekly",
    "Monthly",
    "On Demand",
]

OPERATION_OPTIONS = [
    "Create",
    "Update",
    "Upsert",
    "Delete",
    "Synchronize",
    "Extract",
    "Load",
    "Transform",
]

AUTHENTICATION_OPTIONS = [
    "OAuth2",
    "Basic",
    "API Key",
    "Mutual TLS",
    "Certificate",
    "Not Sure",
]

RUNTIME_OPTIONS = [
    "Atom",
    "Molecule",
    "Boomi Atom Cloud",
    "Not Sure",
]

COMPLEXITY_OPTIONS = [
    "Low",
    "Medium",
    "High",
    "Very High",
]


def get_index(
    options: list[str],
    value: str | None,
    default: str,
) -> int:
    selected_value = value or default

    if selected_value in options:
        return options.index(selected_value)

    return options.index(default)


def get_default(
    defaults: dict,
    field_name: str,
    default_value: str,
) -> str:
    value = defaults.get(field_name)

    if value:
        return str(value)

    return default_value


def build_request_form(
    default_values: dict | None = None,
) -> IntegrationRequest | None:
    """
    Renders the integration request form.

    Returns IntegrationRequest when submitted.
    """

    defaults = default_values or {}

    with st.form("integration_request_form"):
        st.subheader("Integration Requirement")

        st.markdown("### 1. Source and Target Systems")

        col1, col2 = st.columns(2)

        with col1:
            source_system = st.selectbox(
                "Source System",
                SOURCE_TARGET_OPTIONS,
                index=get_index(
                    SOURCE_TARGET_OPTIONS,
                    defaults.get("source_system"),
                    "Local Database",
                ),
            )

        with col2:
            target_system = st.selectbox(
                "Target System",
                SOURCE_TARGET_OPTIONS,
                index=get_index(
                    SOURCE_TARGET_OPTIONS,
                    defaults.get("target_system"),
                    "Salesforce",
                ),
            )

        st.markdown("### 2. Integration Settings")

        col3, col4 = st.columns(2)

        with col3:
            integration_style = st.selectbox(
                "Integration Style",
                INTEGRATION_STYLE_OPTIONS,
                index=get_index(
                    INTEGRATION_STYLE_OPTIONS,
                    defaults.get("integration_style"),
                    "Batch / Scheduled",
                ),
            )

            frequency = st.selectbox(
                "Frequency",
                FREQUENCY_OPTIONS,
                index=get_index(
                    FREQUENCY_OPTIONS,
                    defaults.get("frequency"),
                    "Daily",
                ),
            )

            expected_volume = st.text_input(
                "Expected Volume",
                value=get_default(
                    defaults,
                    "expected_volume",
                    "50,000 records/day",
                ),
                help=(
                    "Example: 10,000 records/day, "
                    "500,000 records/month, low volume, high volume"
                ),
            )

        with col4:
            operation_type = st.selectbox(
                "Operation Type",
                OPERATION_OPTIONS,
                index=get_index(
                    OPERATION_OPTIONS,
                    defaults.get("operation_type"),
                    "Upsert",
                ),
            )

            authentication_type = st.selectbox(
                "Authentication Type",
                AUTHENTICATION_OPTIONS,
                index=get_index(
                    AUTHENTICATION_OPTIONS,
                    defaults.get("authentication_type"),
                    "OAuth2",
                ),
            )

            runtime_environment = st.selectbox(
                "Runtime Environment",
                RUNTIME_OPTIONS,
                index=get_index(
                    RUNTIME_OPTIONS,
                    defaults.get("runtime_environment"),
                    "Atom",
                ),
            )

        st.markdown("### 3. Complexity Inputs")

        col5, col6 = st.columns(2)

        with col5:
            mapping_complexity = st.selectbox(
                "Mapping Complexity",
                COMPLEXITY_OPTIONS,
                index=get_index(
                    COMPLEXITY_OPTIONS,
                    defaults.get("mapping_complexity"),
                    "Medium",
                ),
            )

        with col6:
            transformation_complexity = st.selectbox(
                "Transformation Complexity",
                COMPLEXITY_OPTIONS,
                index=get_index(
                    COMPLEXITY_OPTIONS,
                    defaults.get("transformation_complexity"),
                    "Medium",
                ),
            )

        st.markdown("### 4. Business Requirement")

        business_requirement = st.text_area(
            "Business Requirement (Plain English)",
            value=get_default(
                defaults,
                "business_requirement",
                (
                    "Synchronize customer master data from the on-premise "
                    "database to Salesforce every night using batch processing."
                ),
            ),
            height=140,
            help="Describe what the integration should achieve in business terms.",
        )

        additional_constraints = st.text_area(
            "Additional Constraints",
            value=get_default(
                defaults,
                "additional_constraints",
                "Must complete before business hours.",
            ),
            height=100,
            help=(
                "Examples: SLA, timing, compliance, security, "
                "or operational constraints."
            ),
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
