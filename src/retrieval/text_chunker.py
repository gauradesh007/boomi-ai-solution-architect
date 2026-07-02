def chunk_text(
    text: str,
    chunk_size: int = 1200,
    overlap: int = 150,
) -> list[str]:
    """
    Returns one clean chunk per knowledge file.

    For the MVP, knowledge files are intentionally small,
    so keeping each file together improves retrieval quality.
    """

    cleaned_text = text.strip()

    if not cleaned_text:
        return []

    return [cleaned_text]
