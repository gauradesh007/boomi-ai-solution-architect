import streamlit as st

from src.retrieval.context_builder import build_knowledge_context
from src.retrieval.knowledge_retriever import KnowledgeRetriever
from src.retrieval.query_builder import build_retrieval_query
from src.tools.complexity_estimator import estimate_complexity
from src.tools.connector_recommender import recommend_connectors
from src.tools.pattern_selector import select_integration_pattern
from src.ui.display import display_debug_results
from src.ui.form import build_request_form

st.set_page_config(
    page_title="Boomi AI Solution Architect",
    page_icon="🧩",
    layout="wide",
)


st.title("Boomi AI Solution Architect")

st.write(
    "Generate Boomi-oriented integration architecture recommendations "
    "from structured inputs, deterministic tools, and retrieved knowledge."
)

st.info(
    "Sprint 2 mode: validating tools, retrieval, and knowledge context. "
    "AI report generation is temporarily disabled."
)


request = build_request_form()


if request:
    with st.status(
        "Processing integration architecture inputs...",
        expanded=True,
    ) as status:
        st.write("Selecting integration pattern...")
        pattern = select_integration_pattern(request)

        st.write("Recommending connectors...")
        connectors = recommend_connectors(request)

        st.write("Estimating complexity and effort...")
        estimate = estimate_complexity(request)

        st.write("Building retrieval query...")
        query = build_retrieval_query(request)

        st.write("Retrieving relevant Boomi knowledge...")
        retriever = KnowledgeRetriever()
        knowledge_packets = retriever.retrieve(
            query,
            n_results=2,
        )

        st.write("Building knowledge context...")
        knowledge_context = build_knowledge_context(knowledge_packets)

        status.update(
            label="Sprint 2 processing complete.",
            state="complete",
        )

    display_debug_results(
        request=request,
        pattern=pattern,
        connectors=connectors,
        estimate=estimate,
        query=query,
        knowledge_packets=knowledge_packets,
        knowledge_context=knowledge_context,
    )
