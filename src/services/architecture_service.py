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
from src.retrieval.context_optimizer import ContextOptimizer
from src.retrieval.knowledge_deduplicator import KnowledgeDeduplicator
from src.retrieval.knowledge_ranker import KnowledgeRanker
from src.models.workflow_status import WorkflowStatus


class ArchitectureService:
    def __init__(
        self,
        retriever: KnowledgeRetriever | None = None,
        workflow: ArchitectureWorkflow | None = None,
    ):
        self.retriever = retriever or KnowledgeRetriever()
        self.deduplicator = KnowledgeDeduplicator()
        self.ranker = KnowledgeRanker()
        self.context_optimizer = ContextOptimizer()
        self.workflow = workflow or ArchitectureWorkflow(
            max_revisions=2,
        )

    def generate(
        self,
        request: IntegrationRequest,
        n_results: int = 2,
    ) -> ArchitectureResult:

        workflow_status = WorkflowStatus()
        workflow_status.move_to("PROCESSING")

        pattern = select_integration_pattern(request)

        connectors = recommend_connectors(request)

        estimate = estimate_complexity(request)

        workflow_status.move_to("RETRIEVING_KNOWLEDGE")

        retrieval_query = build_retrieval_query(request)

        retrieved_packets = self.retriever.retrieve(
            retrieval_query,
            n_results=n_results,
        )

        deduplicated_packets = self.deduplicator.deduplicate(retrieved_packets)

        ranked_packets = self.ranker.rank(
            request,
            deduplicated_packets,
        )

        optimized_packets = self.context_optimizer.optimize(
            ranked_packets,
            max_packets=3,
        )

        knowledge_context = build_knowledge_context(optimized_packets)
        workflow_status.move_to("GENERATING_RECOMMENDATION")

        recommendation, review, revision_count = self.workflow.run(
            request=request,
            pattern=pattern,
            connectors=connectors,
            estimate=estimate,
            knowledge_context=knowledge_context,
        )
        workflow_status.move_to("WAITING_FOR_HUMAN_APPROVAL")
        result = ArchitectureResult(
            request=request,
            pattern=pattern,
            connectors=connectors,
            estimate=estimate,
            retrieval_query=retrieval_query,
            knowledge_packets=deduplicated_packets,
            knowledge_context=knowledge_context,
            architecture_recommendation=recommendation,
            architecture_review=review,
            revision_count=revision_count,
            architecture_report=None,
            workflow_status=workflow_status,
        )

        result.architecture_report = generate_architecture_markdown_report(result)

        return result
