from src.agents.architecture_agent import generate_architecture_recommendation
from src.agents.architecture_review_agent import review_architecture
from src.agents.improvement_agent import build_revision_request
from src.models.architecture_recommendation import ArchitectureRecommendation
from src.models.architecture_version import ArchitectureVersion
from src.models.integration_models import (
    ConnectorRecommendation,
    DevelopmentEstimate,
    IntegrationRequest,
    PatternRecommendation,
)
from src.models.review_result import ReviewResult
from src.workflow.version_manager import VersionManager


class ArchitectureWorkflow:
    """Orchestrates architecture generation, review and revision."""

    def __init__(self, max_revisions: int = 2):
        self.max_revisions = max_revisions
        self.version_manager = VersionManager()

    def _create_version(
        self,
        versions: list[ArchitectureVersion],
        recommendation: ArchitectureRecommendation,
        review: ReviewResult,
    ) -> None:
        versions.append(
            self.version_manager.create_version(
                version_number=len(versions) + 1,
                recommendation=recommendation,
                review=review,
            )
        )

    def run(
        self,
        request: IntegrationRequest,
        pattern: PatternRecommendation,
        connectors: ConnectorRecommendation,
        estimate: DevelopmentEstimate,
        knowledge_context: str,
    ) -> tuple[
        ArchitectureRecommendation,
        ReviewResult,
        int,
        list[ArchitectureVersion],
    ]:
        revision_count = 0
        revision_request = None
        versions: list[ArchitectureVersion] = []

        recommendation = generate_architecture_recommendation(
            request=request,
            pattern=pattern,
            connectors=connectors,
            estimate=estimate,
            knowledge_context=knowledge_context,
            revision_request=revision_request,
        )

        review = review_architecture(recommendation)
        self._create_version(versions, recommendation, review)

        while review.status == "NEEDS_REVISION" and revision_count < self.max_revisions:
            revision_request = build_revision_request(
                recommendation=recommendation,
                review=review,
            )

            revision_count += 1

            recommendation = generate_architecture_recommendation(
                request=request,
                pattern=pattern,
                connectors=connectors,
                estimate=estimate,
                knowledge_context=knowledge_context,
                revision_request=revision_request,
            )

            review = review_architecture(recommendation)
            self._create_version(versions, recommendation, review)

        return recommendation, review, revision_count, versions
