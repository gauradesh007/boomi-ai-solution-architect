from src.models.integration_models import ConnectorRecommendation
from src.models.integration_models import IntegrationRequest

CONNECTOR_MAP = {
    "Salesforce": "Salesforce Connector",
    "SAP": "SAP Connector / SAP OData / IDoc / BAPI",
    "Local Database": "Database Connector",
    "REST API": "HTTP Client Connector / REST Connector",
    "SFTP": "SFTP Connector",
    "Workday": "Workday Connector",
    "Snowflake": "Snowflake Connector",
    "Oracle": "Database Connector",
    "SQL Server": "Database Connector",
    "PostgreSQL": "Database Connector",
    "Custom": "Custom Connector / HTTP Client Connector",
}


def recommend_connector(system_name: str) -> str:
    """
    Returns the recommended Boomi connector
    for a given enterprise system.
    """

    return CONNECTOR_MAP.get(
        system_name,
        "HTTP Client Connector / Custom Connector",
    )


def recommend_connectors(
    request: IntegrationRequest,
) -> ConnectorRecommendation:
    """
    Recommends source and target connectors
    based on source and target systems.
    """

    source_connector = recommend_connector(request.source_system)

    target_connector = recommend_connector(request.target_system)

    notes = (
        f"Use {source_connector} to connect with "
        f"{request.source_system}. Use {target_connector} "
        f"to connect with {request.target_system}."
    )

    if request.operation_type == "Upsert":
        notes += (
            " Since the operation is Upsert, confirm that the "
            "target system supports external ID or equivalent matching logic."
        )

    if request.integration_style == "Batch / Scheduled":
        notes += (
            " Since the integration is batch-oriented, consider batching, "
            "pagination, and process-level monitoring."
        )

    return ConnectorRecommendation(
        source_connector=source_connector,
        target_connector=target_connector,
        notes=notes,
    )
