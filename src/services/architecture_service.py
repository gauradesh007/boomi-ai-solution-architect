from src.models.integration_models import ArchitectureResult
from src.models.integration_models import IntegrationRequest
from src.retrieval.context_builder import build_knowledge_context
from src.retrieval.knowledge_retriever import KnowledgeRetriever
from src.retrieval.query_builder import build_retrieval_query
from src.tools.complexity_estimator import estimate_complexity
from src.tools.connector_recommender import recommend_connectors
from src.tools.pattern_selector import select_integration_pattern


class ArchitectureService:
    """
    Application service that orchestrates the current
    architecture recommendation workflow.

    The UI should call this service instead of calling
    tools and retrievers directly.
    """

    def __init__(
        self,
        retriever: KnowledgeRetriever | None = None,
    ):
        self.retriever = retriever or KnowledgeRetriever()

    def generate(
        self,
        request: IntegrationRequest,
        n_results: int = 2,
    ) -> ArchitectureResult:
        """
        Generates the current Sprint 2 architecture result.

        This currently includes:
        - deterministic tool outputs
        - retrieval query
        - retrieved knowledge packets
        - knowledge context

        AI report generation will be added later.
        """

        pattern = select_integration_pattern(request)

        connectors = recommend_connectors(request)

        estimate = estimate_complexity(request)

        retrieval_query = build_retrieval_query(request)

        knowledge_packets = self.retriever.retrieve(
            retrieval_query,
            n_results=n_results,
        )

        knowledge_context = build_knowledge_context(knowledge_packets)

        return ArchitectureResult(
            request=request,
            pattern=pattern,
            connectors=connectors,
            estimate=estimate,
            retrieval_query=retrieval_query,
            knowledge_packets=knowledge_packets,
            knowledge_context=knowledge_context,
            architecture_recommendation=None,
            architecture_report=None,
        )
