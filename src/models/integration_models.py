from typing import Literal
from typing import Optional
from pydantic import BaseModel

IntegrationStyle = Literal[
    "API / Real-Time",
    "Event-Driven",
    "Batch / Scheduled",
    "Hybrid",
]

OperationType = Literal[
    "Create",
    "Update",
    "Upsert",
    "Delete",
    "Synchronize",
    "Extract",
    "Load",
    "Transform",
]

Frequency = Literal[
    "Real-Time",
    "Hourly",
    "Daily",
    "Weekly",
    "Monthly",
    "On Demand",
]

ComplexityLevel = Literal[
    "Low",
    "Medium",
    "High",
    "Very High",
]


class IntegrationRequest(BaseModel):
    """
    User-provided integration requirement.
    """

    source_system: str
    target_system: str
    integration_style: IntegrationStyle
    operation_type: OperationType
    frequency: Frequency
    expected_volume: str
    business_requirement: str

    authentication_type: Optional[str] = None
    runtime_environment: Optional[str] = None
    number_of_objects: Optional[int] = None
    mapping_complexity: Optional[ComplexityLevel] = None
    transformation_complexity: Optional[ComplexityLevel] = None
    additional_constraints: Optional[str] = None


class PatternRecommendation(BaseModel):
    """
    Deterministic integration pattern recommendation.
    """

    pattern_name: str
    reason: str


class ConnectorRecommendation(BaseModel):
    """
    Recommended source and target connectors.
    """

    source_connector: str
    target_connector: str
    notes: str


class DevelopmentEstimate(BaseModel):
    """
    Development and testing effort estimate.
    """

    complexity: ComplexityLevel
    development_estimate: str
    testing_estimate: str
    total_estimate: str
    assumptions: list[str]


class ArchitectureReport(BaseModel):
    """
    Final architecture report content.
    """

    executive_summary: str
    requirement_summary: str
    recommended_pattern: str
    source_system: str
    target_system: str
    boomi_process_flow: str
    connector_strategy: str
    mapping_strategy: str
    error_handling_strategy: str
    retry_strategy: str
    monitoring_and_logging: str
    security_considerations: str
    risks_and_assumptions: str
    scalability_considerations: str
    development_and_testing_estimate: str
    implementation_roadmap: str
    final_recommendation: str


class KnowledgePacket(BaseModel):
    """
    Retrieved knowledge chunk used by the architecture workflow.
    """

    content: str
    source: str
    category: str
    relevance_score: float | None = None
    trust_level: str = "medium"
    freshness: str = "stable"
