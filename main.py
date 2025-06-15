from app.langgraph_runner import build_workflow

def main():
    user_input = input("Enter your query: ")
    graph = build_workflow()
    result = graph.invoke({"input": user_input})
    print("\nFinal Answer Summary:\n", result.get("summary"))
    print("\nFull State:\n", result)


if __name__ == "__main__":
    main()
