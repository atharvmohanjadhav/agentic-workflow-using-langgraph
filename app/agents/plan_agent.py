import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def plan_tasks(input_state):
    user_input = input_state["input"]
    prompt = f"Split the following query into subtasks:\n\n{user_input}\n\nReturn a list of steps."
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content.strip()
    tasks = [t.strip("-•1234567890. ").strip() for t in content.split("\n") if t.strip()]
    return {"tasks": tasks}
