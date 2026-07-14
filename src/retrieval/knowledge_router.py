from src.models.integration_models import IntegrationRequest
from src.models.knowledge_search_plan import (
    KnowledgeSearchPlan,
)


class KnowledgeRouter:
    """
    Determines which knowledge categories
    should be searched.
    """

    def build_search_plan(
        self,
        request: IntegrationRequest,
        query: str,
    ) -> KnowledgeSearchPlan:

        categories = set()

        #
        # Pattern Knowledge
        #

        categories.add("patterns")

        #
        # Connector Knowledge
        #

        categories.add("connectors")

        #
        # Error Handling
        #

        categories.add("error_handling")

        #
        # Monitoring
        #

        categories.add("monitoring")

        #
        # Security
        #

        categories.add("security")

        #
        # Estimation
        #

        categories.add("estimation")

        #
        # Future routing rules
        #

        if request.integration_style == "API / Real-Time":
            categories.add("patterns")

        if request.integration_style == "Batch / Scheduled":
            categories.add("patterns")

        if request.operation_type == "Upsert":
            categories.add("connectors")

        if request.authentication_type:
            categories.add("security")

        return KnowledgeSearchPlan(
            categories=sorted(categories),
            query=query,
            reason=("Knowledge categories selected " "based on integration request."),
        )
