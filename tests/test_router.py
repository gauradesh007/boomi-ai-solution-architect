from src.models.integration_models import IntegrationRequest
from src.retrieval.query_builder import build_retrieval_query
from src.retrieval.knowledge_router import KnowledgeRouter

request = IntegrationRequest(
    source_system="Local Database",
    target_system="Salesforce",
    integration_style="Batch / Scheduled",
    operation_type="Upsert",
    frequency="Daily",
    expected_volume="50000",
    business_requirement="Sync customers",
)

query = build_retrieval_query(request)

router = KnowledgeRouter()

plan = router.build_search_plan(
    request,
    query,
)

print(plan.model_dump())
