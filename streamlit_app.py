import streamlit as st
from app.langgraph_runner import build_workflow

st.title("Agentic Workflow Using LangGraph")

user_input = st.text_area("Enter your query")

if st.button("Run Workflow"):
    with st.spinner("Running agentic workflow..."):
        graph = build_workflow()
        result = graph.invoke({"input": user_input})

        st.markdown("### Final Answer Summary")
        st.success(result.get("summary", "No summary generated."))

        with st.expander("Full Output (Debug Info)", expanded=False):
            st.json(result)
