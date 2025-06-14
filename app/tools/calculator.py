def solve_math(task):
    try:
        result = eval(task)
        return f"Answer: {result}"
    except Exception as e:
        return f"Error evaluating math: {str(e)}"
