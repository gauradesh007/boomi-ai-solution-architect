from src.models.integration_models import (
    IntegrationRequest,
)
from src.retrieval.query_builder import (
    build_retrieval_query,
)
from src.retrieval.knowledge_retriever import (
    KnowledgeRetriever,
)
from src.retrieval.knowledge_ranker import (
    KnowledgeRanker,
)

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

retriever = KnowledgeRetriever()

packets = retriever.retrieve(query)

ranker = KnowledgeRanker()

ranked = ranker.rank(
    request,
    packets,
)

for item in ranked:

    print("=" * 60)

    print(item.priority)

    print(item.score)

    print(item.packet.category)

    print(item.packet.source)
