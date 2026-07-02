from pathlib import Path


def read_markdown_files(
    knowledge_dir: Path,
) -> list[Path]:
    """
    Finds all markdown files inside the knowledge directory.
    """

    return sorted(knowledge_dir.rglob("*.md"))


def load_markdown_file(
    file_path: Path,
) -> str:
    """
    Reads a markdown file as text.
    """

    return file_path.read_text(encoding="utf-8")
