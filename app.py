import streamlit as st

from src.models.integration_models import IntegrationRequest

st.set_page_config(
    page_title="Boomi AI Solution Architect",
    page_icon="🧩",
    layout="wide",
)


st.title("Boomi AI Solution Architect")
st.write(
    "Generate Boomi-oriented integration architecture recommendations "
    "from structured inputs and business requirements."
)


with st.form("integration_request_form"):
    st.subheader("Integration Requirement")

    col1, col2 = st.columns(2)

    with col1:
        source_system = st.selectbox(
            "Source System",
            [
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
            ],
        )

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

    business_requirement = st.text_area(
        "Business Requirement",
        value=(
            "Create or update customer information in Salesforce "
            "from a local database every night."
        ),
        height=140,
    )

    additional_constraints = st.text_area(
        "Additional Constraints",
        value="Must complete before business hours.",
        height=100,
    )

    submitted = st.form_submit_button("Generate Architecture")


if submitted:
    request = IntegrationRequest(
        source_system=source_system,
        target_system=target_system,
        integration_style=integration_style,
        operation_type=operation_type,
        frequency=frequency,
        expected_volume=expected_volume,
        authentication_type=authentication_type,
        runtime_environment=runtime_environment,
        business_requirement=business_requirement,
        additional_constraints=additional_constraints,
    )

    st.success("Integration request captured successfully.")

    st.subheader("Captured Request")
    st.json(request.model_dump())
