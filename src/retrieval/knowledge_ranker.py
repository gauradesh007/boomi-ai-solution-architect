from src.models.integration_models import (
    IntegrationRequest,
)
from src.models.integration_models import (
    KnowledgePacket,
)
from src.models.ranked_knowledge_packet import (
    RankedKnowledgePacket,
)

CATEGORY_PRIORITY = {
    "connectors": 1,
    "patterns": 2,
    "security": 3,
    "error_handling": 4,
    "monitoring": 5,
    "estimation": 6,
}


class KnowledgeRanker:
    """
    Ranks retrieved knowledge packets.
    """

    def rank(
        self,
        request: IntegrationRequest,
        packets: list[KnowledgePacket],
    ) -> list[RankedKnowledgePacket]:

        ranked = []

        for packet in packets:

            category = packet.category

            priority = CATEGORY_PRIORITY.get(
                category,
                99,
            )

            score = 100 - priority

            reason = f"Category '{category}' " f"priority {priority}"

            ranked.append(
                RankedKnowledgePacket(
                    packet=packet,
                    score=score,
                    priority=priority,
                    reason=reason,
                )
            )

        ranked.sort(
            key=lambda item: (
                item.priority,
                -item.score,
            )
        )

        return ranked
