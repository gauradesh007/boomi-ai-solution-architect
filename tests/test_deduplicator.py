from src.models.integration_models import (
    IntegrationRequest,
)

from src.retrieval.query_builder import (
    build_retrieval_query,
)

from src.retrieval.knowledge_retriever import (
    KnowledgeRetriever,
)

from src.retrieval.knowledge_deduplicator import (
    KnowledgeDeduplicator,
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

print()

print("Before")

print(len(packets))

deduplicator = KnowledgeDeduplicator()

unique = deduplicator.deduplicate(packets)

print()

print("After")

print(len(unique))

print()

for packet in unique:

    print(packet.source)
