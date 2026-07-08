import streamlit as st

from src.services.architecture_service import ArchitectureService
from src.ui.display import display_architecture_result
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
    "Sprint 2 mode: validating the application service, tools, "
    "retrieval, and knowledge context. AI report generation is "
    "temporarily disabled."
)


request = build_request_form()


if request:
    service = ArchitectureService()

    with st.status(
        "Processing integration architecture inputs...",
        expanded=True,
    ) as status:
        st.write("Running architecture service...")

        result = service.generate(
            request=request,
            n_results=2,
        )

        status.update(
            label="Sprint 2 processing complete.",
            state="complete",
        )

    display_architecture_result(result)
