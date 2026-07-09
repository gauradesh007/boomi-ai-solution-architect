from src.models.integration_models import ArchitectureResult
from src.models.integration_models import IntegrationRequest
from src.retrieval.context_builder import build_knowledge_context
from src.retrieval.knowledge_retriever import KnowledgeRetriever
from src.retrieval.query_builder import build_retrieval_query
from src.services.architecture_report_generator import (
    generate_architecture_markdown_report,
)
from src.tools.complexity_estimator import estimate_complexity
from src.tools.connector_recommender import recommend_connectors
from src.tools.pattern_selector import select_integration_pattern
from src.workflow.architecture_workflow import ArchitectureWorkflow


class ArchitectureService:
    def __init__(
        self,
        retriever: KnowledgeRetriever | None = None,
        workflow: ArchitectureWorkflow | None = None,
    ):
        self.retriever = retriever or KnowledgeRetriever()
        self.workflow = workflow or ArchitectureWorkflow(
            max_revisions=2,
        )

    def generate(
        self,
        request: IntegrationRequest,
        n_results: int = 2,
    ) -> ArchitectureResult:
        pattern = select_integration_pattern(request)

        connectors = recommend_connectors(request)

        estimate = estimate_complexity(request)

        retrieval_query = build_retrieval_query(request)

        knowledge_packets = self.retriever.retrieve(
            retrieval_query,
            n_results=n_results,
        )

        knowledge_context = build_knowledge_context(knowledge_packets)

        recommendation, review, revision_count = self.workflow.run(
            request=request,
            pattern=pattern,
            connectors=connectors,
            estimate=estimate,
            knowledge_context=knowledge_context,
        )

        result = ArchitectureResult(
            request=request,
            pattern=pattern,
            connectors=connectors,
            estimate=estimate,
            retrieval_query=retrieval_query,
            knowledge_packets=knowledge_packets,
            knowledge_context=knowledge_context,
            architecture_recommendation=recommendation,
            architecture_review=review,
            revision_count=revision_count,
            architecture_report=None,
        )

        result.architecture_report = generate_architecture_markdown_report(result)

        return result
