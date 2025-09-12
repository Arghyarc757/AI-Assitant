import os
from openai import OpenAI
from apikey import apikey

# Try to load API key from environment variable, else fallback to default
api_key = os.getenv("HF_TOKEN", apikey)

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=api_key,
)

def ask_ai(prompt: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1:together",
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error contacting AI: {str(e)}"