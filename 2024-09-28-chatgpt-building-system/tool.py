import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("ZHIPU_API_KEY"),
    base_url=os.environ.get("ZHIPU_BASE_URL")
)

model = "glm-4-flash"

def get_completion(prompt, model=model):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一个很有用的助手。"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    return response.choices[0].message.content

def get_completion_from_messages(messages, model=model, temperature=0,max_tokens=500):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content