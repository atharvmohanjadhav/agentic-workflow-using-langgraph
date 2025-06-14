import wikipedia

def wiki_search(task):
    try:
        summary = wikipedia.summary(task, sentences=2)
        return summary
    except Exception as e:
        return f"Error in Wikipedia search: {str(e)}"
