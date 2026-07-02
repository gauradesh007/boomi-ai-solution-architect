from pathlib import Path
from src.models.integration_models import KnowledgePacket
import chromadb

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CHROMA_DIR = PROJECT_ROOT / "chromadb_data"

COLLECTION_NAME = "boomi_knowledge"


class KnowledgeRetriever:
    """
    Retrieves relevant knowledge
    from persistent ChromaDB.
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(path=str(CHROMA_DIR))

        self.collection = self.client.get_collection(COLLECTION_NAME)

    def retrieve(
        self,
        query: str,
        n_results: int = 5,
    ) -> list[dict]:
        """
        Retrieves the most relevant
        knowledge chunks.
        """

        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
        )

        knowledge = []

        for document, metadata in zip(
            results["documents"][0],
            results["metadatas"][0],
        ):

            knowledge.append(
                KnowledgePacket(
                    content=document,
                    source=metadata.get("source", "unknown"),
                    category=metadata.get("category", "unknown"),
                )
            )

        return knowledge
