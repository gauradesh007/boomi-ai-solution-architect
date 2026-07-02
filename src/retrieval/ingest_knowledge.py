from pathlib import Path

import chromadb

from src.retrieval.document_loader import load_markdown_file
from src.retrieval.document_loader import read_markdown_files
from src.retrieval.text_chunker import chunk_text

PROJECT_ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"
CHROMA_DIR = PROJECT_ROOT / "chromadb_data"
COLLECTION_NAME = "boomi_knowledge"


def build_document_id(
    relative_path: Path,
    index: int,
) -> str:
    """
    Builds a stable ChromaDB document ID.
    """

    return (
        str(relative_path)
        .replace(
            "/",
            "_",
        )
        .replace(
            ".md",
            f"_{index}",
        )
    )


def build_metadata(
    relative_path: Path,
) -> dict:
    """
    Builds metadata for a knowledge chunk.
    """

    return {
        "source": str(relative_path),
        "category": (
            relative_path.parts[1] if len(relative_path.parts) > 1 else "unknown"
        ),
    }


def ingest_knowledge() -> None:
    """
    Reads markdown knowledge files, chunks them,
    and stores chunks in persistent ChromaDB.
    """

    markdown_files = read_markdown_files(KNOWLEDGE_DIR)

    if not markdown_files:
        print("No markdown files found in knowledge directory.")
        return

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    documents = []
    ids = []
    metadatas = []

    for file_path in markdown_files:
        content = load_markdown_file(file_path)

        chunks = chunk_text(content)

        relative_path = file_path.relative_to(PROJECT_ROOT)

        for index, chunk in enumerate(chunks):
            documents.append(chunk)
            ids.append(
                build_document_id(
                    relative_path,
                    index,
                )
            )
            metadatas.append(build_metadata(relative_path))

    collection.upsert(
        documents=documents,
        ids=ids,
        metadatas=metadatas,
    )

    print(f"Ingested {len(documents)} chunks " f"from {len(markdown_files)} files.")


if __name__ == "__main__":
    ingest_knowledge()
