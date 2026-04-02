import json
from pathlib import Path
import streamlit as st
from src.workflow import run_workflow
from src.logger import save_result

st.set_page_config(page_title="Agentic Content Workflow", layout="wide")

@st.cache_data
def load_products():
    path = Path("data/sample_products.json")
    return json.loads(path.read_text(encoding="utf-8"))

st.title("Agentic Content Workflow Demo")
st.write("Generate, critique, refine, and adapt product content across channels.")

products = load_products()
product_names = [p["product_name"] for p in products]
selected_name = st.selectbox("Choose a product", product_names)

selected_product = next(p for p in products if p["product_name"] == selected_name)

st.subheader("Product Input")
st.json(selected_product)

if st.button("Run workflow"):
    with st.spinner("Running AI workflow..."):
        result = run_workflow(selected_product)
        save_result(selected_product["product_name"], result)

    st.success("Done.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Strategy")
        st.json(result["strategy"])

        st.subheader("Draft")
        st.json(result["draft"])

        st.subheader("Critique")
        st.json(result["critique"])

    with col2:
        st.subheader("Refined")
        st.json(result["refined"])

        st.subheader("Adapted")
        st.json(result["adapted"])