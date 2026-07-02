from pathlib import Path

import chromadb

PROJECT_ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"
CHROMA_DIR = PROJECT_ROOT / "chromadb_data"
COLLECTION_NAME = "boomi_knowledge"


def read_markdown_files() -> list[Path]:
    """
    Finds all markdown files inside the knowledge directory.
    """

    return sorted(KNOWLEDGE_DIR.rglob("*.md"))


def chunk_text(
    text: str,
    chunk_size: int = 1200,
    overlap: int = 150,
) -> list[str]:
    """
    Splits text into simple overlapping chunks.
    """

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - overlap

    return chunks


def ingest_knowledge() -> None:
    """
    Reads markdown knowledge files and stores them
    in persistent ChromaDB.
    """

    markdown_files = read_markdown_files()

    if not markdown_files:
        print("No markdown files found in knowledge directory.")
        return

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    documents = []
    ids = []
    metadatas = []

    for file_path in markdown_files:
        content = file_path.read_text(encoding="utf-8")

        chunks = chunk_text(content)

        relative_path = file_path.relative_to(PROJECT_ROOT)

        for index, chunk in enumerate(chunks):
            doc_id = (
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

            documents.append(chunk)
            ids.append(doc_id)
            metadatas.append(
                {
                    "source": str(relative_path),
                    "category": (
                        relative_path.parts[1]
                        if len(relative_path.parts) > 1
                        else "unknown"
                    ),
                }
            )

    collection.upsert(
        documents=documents,
        ids=ids,
        metadatas=metadatas,
    )

    print(f"Ingested {len(documents)} chunks " f"from {len(markdown_files)} files.")


if __name__ == "__main__":
    ingest_knowledge()
