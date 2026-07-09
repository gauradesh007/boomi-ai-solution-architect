from pydantic import BaseModel


class ArchitectureRecommendation(BaseModel):
    """
    AI-generated architecture reasoning.

    This model separates AI reasoning from final report formatting.
    The Architecture Agent should produce this structure.
    The Report Generator should convert it into Markdown, PDF, or other outputs.
    """

    executive_summary: str
    pattern_reasoning: str
    connector_reasoning: str
    boomi_process_flow: str
    mapping_strategy: str
    error_handling_strategy: str
    retry_strategy: str
    monitoring_strategy: str
    security_strategy: str
    scalability_considerations: str
    risks: list[str]
    assumptions: list[str]
    implementation_roadmap: list[str]
    final_recommendation: str
