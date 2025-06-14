import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_results(state):
    results = state["results"]
    joined = "\n".join(results)
    prompt = f"""You are an expert assistant. Given the following results from multiple tools, extract the final answer for the user's query. Be concise and accurate.

Results:
{joined}

Return only the final, summarized answer in 2-3 sentences.
"""
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"summary": response.choices[0].message.content.strip()}
