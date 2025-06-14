import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def reflect_on_results(state):
    results = state["results"]
    prompt = f"Evaluate each of these results and suggest if they need refinement:\n\n{results}"
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    feedback = response.choices[0].message.content.strip()
    return {"feedback": feedback}
