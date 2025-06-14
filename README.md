#  Agentic Workflow with LangGraph 

## Overview
This project uses LangGraph to implement an agentic workflow that:
- Splits a user query into subtasks (PlanAgent)
- Solves them using tools (ToolAgent)
- Reflects and improves (ReflectionAgent)

##  Setup

1. Clone the repo:
```bash
git clone <your-repo-url>
cd agentic-workflow-using-langgraph
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your Groq API key to `.env`:
```
GROQ_API_KEY=your_groq_api_key
```

##  Run

### CLI:
```bash
python main.py
```

### Web (Streamlit):
```bash
streamlit run streamlit_app.py
```

##  Hosting
https://agentic-workflow-using-langgraph.streamlit.app/
