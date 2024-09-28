import os
from openai import OpenAI
from rich import print

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


def get_completion_and_token_count(messages, 
                                   model=model, 
                                   temperature=0, 
                                   max_tokens=500):
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
 
    content = response.choices[0].message.content
    
    token_dict = {
        'prompt_tokens': response.usage.prompt_tokens,
        'completion_tokens': response.usage.completion_tokens,
        'total_tokens': response.usage.total_tokens,
    }

    return content, token_dict