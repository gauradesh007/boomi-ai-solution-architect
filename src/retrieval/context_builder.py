from src.models.ranked_knowledge_packet import RankedKnowledgePacket


def build_knowledge_context(
    ranked_packets: list[RankedKnowledgePacket],
) -> str:
    """
    Converts optimized ranked knowledge packets into a clean context block.

    This context is passed to the Architecture Agent.
    """

    if not ranked_packets:
        return "No relevant knowledge was retrieved."

    context_sections = []

    for index, ranked_packet in enumerate(
        ranked_packets,
        start=1,
    ):
        packet = ranked_packet.packet

        section = f"""
Knowledge Source {index}

Source:
{packet.source}

Category:
{packet.category}

Rank Score:
{ranked_packet.score}

Rank Reason:
{ranked_packet.reason}

Content:
{packet.content}
""".strip()

        context_sections.append(section)

    return "\n\n---\n\n".join(context_sections)
