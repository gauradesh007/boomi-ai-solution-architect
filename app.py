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

    st.divider()

    mode = st.radio(
        "Application Mode",
        [
            "🏢 Production",
            "🛠 Developer",
        ],
    )

    st.divider()

    st.markdown("## 🧠 Capabilities")

    st.markdown("""
✅ AI Architecture Recommendation

✅ Enterprise Knowledge Retrieval

✅ Deterministic Engineering Rules

✅ Architecture Review

✅ Revision Workflow

✅ Human Approval

✅ Conversation Memory

✅ Version Management

✅ Markdown Report
""")

    st.divider()

    st.markdown("## 🚀 Product Status")

    st.markdown("""
🟢 **Current Release**

Version **v1.0.0**

Status **Release Candidate**
""")

    st.divider()

    st.markdown("## 📅 Roadmap")

    st.markdown("""
### Version 1.1

⬜ PDF Export

⬜ DOCX Export

⬜ Architecture Diagram Generation

### Version 2.0

⬜ Multi-Platform Support

⬜ OpenAI Provider

⬜ Enterprise Knowledge Connectors

⬜ Architecture Comparison
""")

    if "last_request" in st.session_state:

        st.divider()

        st.markdown("## 📌 Recent Request")

        last_request = st.session_state["last_request"]

        st.markdown(f"""
**Source**

{last_request["source_system"]}

**Target**

{last_request["target_system"]}

**Integration**

{last_request["integration_style"]}

**Operation**

{last_request["operation_type"]}
""")

        reuse_last_request = st.checkbox(
            "Reuse this request",
            value=False,
        )
    else:
        reuse_last_request = False

    st.divider()

    st.caption("© 2026 Boomi AI Solution Architect")

st.title("Boomi AI Solution Architect")
st.caption("AI-powered enterprise integration architecture assistant")

st.markdown("""
    Generate Boomi-oriented solution recommendations from structured requirements,
    deterministic tools, enterprise knowledge, and AI reasoning.
    """)

st.info(
    "Enter an integration requirement below and generate an architecture "
    "recommendation with review score, revision feedback, and a Markdown report."
)

default_values = st.session_state.get("last_request") if reuse_last_request else None

request = build_request_form(
    default_values=default_values,
)

if request:
    st.session_state["last_request"] = request.model_dump()

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
