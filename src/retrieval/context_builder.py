from src.models.integration_models import KnowledgePacket


def build_knowledge_context(
    knowledge_packets: list[KnowledgePacket],
) -> str:
    """
    Converts retrieved knowledge packets into a clean context block.

    This context will later be passed to the Architecture Agent.
    """

    if not knowledge_packets:
        return "No relevant knowledge was retrieved."

    context_sections = []

    for index, packet in enumerate(
        knowledge_packets,
        start=1,
    ):
        section = f"""
Knowledge Source {index}

Source:
{packet.source}

Category:
{packet.category}

Content:
{packet.content}
""".strip()

        context_sections.append(section)

    return "\n\n---\n\n".join(context_sections)
