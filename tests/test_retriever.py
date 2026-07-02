from src.retrieval.knowledge_retriever import (
    KnowledgeRetriever,
)

retriever = KnowledgeRetriever()

results = retriever.retrieve(
    query="Salesforce batch upsert",
)

for result in results:
    print("=" * 60)
    print(result.source)
    print(result.category)
    print()
    print(result.content)
