from pydantic import BaseModel

from src.models.integration_models import KnowledgePacket


class RankedKnowledgePacket(BaseModel):
    """
    Knowledge packet with ranking information.
    """

    packet: KnowledgePacket

    score: float

    priority: int

    reason: str
