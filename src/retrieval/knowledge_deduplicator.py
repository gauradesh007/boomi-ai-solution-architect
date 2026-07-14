from src.models.integration_models import KnowledgePacket


class KnowledgeDeduplicator:
    """
    Removes duplicate knowledge packets before ranking.

    Duplicate detection is based on the knowledge source.
    If multiple chunks originate from the same source,
    the longest chunk is retained.
    """

    def deduplicate(
        self,
        packets: list[KnowledgePacket],
    ) -> list[KnowledgePacket]:

        unique_packets: dict[str, KnowledgePacket] = {}

        for packet in packets:

            existing = unique_packets.get(packet.source)

            if existing is None:
                unique_packets[packet.source] = packet

            elif len(packet.content) > len(existing.content):
                unique_packets[packet.source] = packet

        return list(unique_packets.values())
