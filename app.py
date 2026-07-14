import streamlit as st

from src.services.architecture_service import ArchitectureService
from src.ui.display import display_architecture_result
from src.ui.form import build_request_form

st.set_page_config(
    page_title="Boomi AI Solution Architect",
    page_icon="🧩",
    layout="wide",
)


with st.sidebar:
    st.title("🧩 Boomi AI")
    st.caption("Enterprise Integration Solution Architect")

    mode = st.radio(
        "Application Mode",
        [
            "🏢 Production",
            "🛠 Developer",
        ],
    )

    st.divider()

    st.markdown("### Capabilities")
    st.markdown("""
        ✅ Pattern recommendation  
        ✅ Connector recommendation  
        ✅ Knowledge retrieval  
        ✅ AI reasoning  
        ✅ Architecture review  
        ✅ Revision workflow  
        ✅ Markdown report  
        """)

    st.divider()

    st.markdown("### Roadmap")
    st.markdown("""
        🚧 Human approval  
        🚧 PDF export  
        🚧 Architecture diagrams  
        🚧 Source attribution  
        """)

    st.divider()

    st.success("Prototype Active")


st.title("Boomi AI Solution Architect")

st.markdown("""
    AI-powered enterprise integration architecture assistant for generating
    Boomi-oriented solution recommendations from structured requirements,
    deterministic tools, enterprise knowledge, and AI reasoning.
    """)

st.info(
    "Enter an integration requirement below and generate an architecture "
    "recommendation with review score, revision feedback, and a Markdown report."
)


request = build_request_form()


if request:
    service = ArchitectureService()

    with st.status(
        "Generating architecture recommendation...",
        expanded=True,
    ) as status:
        st.write("Analyzing structured requirement...")
        st.write("Running deterministic architecture tools...")
        st.write("Retrieving and optimizing knowledge context...")
        st.write("Generating AI architecture recommendation...")
        st.write("Reviewing and revising architecture output...")

        result = service.generate(
            request=request,
            n_results=5,
        )

        status.update(
            label="Architecture recommendation generated.",
            state="complete",
        )

    display_architecture_result(
        result,
        mode=mode,
    )
else:
    st.markdown("""
        ### What this assistant produces

        - Recommended integration pattern
        - Boomi connector strategy
        - Mapping and validation guidance
        - Error handling and retry strategy
        - Monitoring and security recommendations
        - Development and testing estimate
        - Architecture review score
        - Downloadable Markdown report
        """)
