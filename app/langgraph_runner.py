from langgraph.graph import StateGraph, END
from app.agents.plan_agent import plan_tasks
from app.agents.tool_agent import tool_agent
from app.agents.reflection_agent import reflect_on_results
from app.agents.summary_agent import summarize_results
from typing import TypedDict, List


class WorkflowState(TypedDict):
    input: str
    tasks: List[str]
    results: List[str]
    feedback: str
    summary: str


def build_workflow():
    builder = StateGraph(state_schema=WorkflowState)

    builder.add_node("plan", plan_tasks)
    builder.add_node("tool", tool_agent)
    builder.add_node("reflect", reflect_on_results)
    builder.add_node("summarize", summarize_results)

    builder.set_entry_point("plan")
    builder.add_edge("plan", "tool")
    builder.add_edge("tool", "reflect")
    builder.add_edge("reflect", "summarize")
    builder.add_edge("summarize", END)

    return builder.compile()
