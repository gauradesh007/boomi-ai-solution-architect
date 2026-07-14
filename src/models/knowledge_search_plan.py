from pydantic import BaseModel


class KnowledgeSearchPlan(BaseModel):
    """
    Represents the knowledge categories
    that should be searched.
    """

    categories: list[str]

    query: str

    reason: str
