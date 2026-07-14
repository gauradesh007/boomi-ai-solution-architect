from src.models.ranked_knowledge_packet import RankedKnowledgePacket


class ContextOptimizer:
    """
    Selects the best ranked knowledge packets
    for the Architecture Agent context.
    """

    def optimize(
        self,
        ranked_packets: list[RankedKnowledgePacket],
        max_packets: int = 3,
    ) -> list[RankedKnowledgePacket]:
        """
        Returns the highest-priority ranked packets.

        The ranker already sorts packets by priority and score,
        so this method keeps only the best packets for the prompt.
        """

        if not ranked_packets:
            return []

        return ranked_packets[:max_packets]
