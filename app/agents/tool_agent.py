from app.tools.calculator import solve_math
from app.tools.wikipedia_search import wiki_search

def tool_agent(state):
    tasks = state.get("tasks", [])
    results = []

    for task in tasks:
        if any(char.isdigit() for char in task) or "calculate" in task.lower():
            results.append(solve_math(task))
        else:
            results.append(wiki_search(task))

    return {"results": results}
