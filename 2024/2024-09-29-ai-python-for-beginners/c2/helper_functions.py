import os
from openai import OpenAI
from rich import print

# 初始化 OpenAI 客户端
client = OpenAI(
    api_key=os.getenv('ZHIPU_API_KEY'), # 你申请的 API 密钥
    base_url=os.getenv('ZHIPU_BASE_URL') # 'https://open.bigmodel.cn/api/paas/v4/'
)

model = "glm-4-flash"

def print_llm_response(prompt):
    """此函数接受一个提示作为输入，该提示必须是用引号括起来的字符串，
    并将其传递给智谱的 glm-4-flash 模型。然后，函数打印模型的响应。
    """
    llm_response = get_llm_response(prompt)
    print(llm_response)


def get_llm_response(prompt):
    """此函数接受一个提示作为输入，该提示必须是用引号括起来的字符串，
    并将其传递给智谱的 glm-4-flash 模型。然后，函数将模型的响应保存为
    字符串。
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("输入必须是用引号括起来的字符串。")
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "你是一个有帮助但简洁的人工智能助手，直截了当地回答问题。",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        response = completion.choices[0].message.content
        return response
    except TypeError as e:
        print("错误：", str(e))


def get_chat_completion(prompt, history):
    """此函数接受一个提示和历史记录作为输入，将它们传递给智谱的 glm-4-flash 模型，
    并返回模型的响应。
    """
    history_string = "\n\n".join(["\n".join(turn) for turn in history])
    prompt_with_history = f"{history_string}\n\n{prompt}"
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "你是一个有帮助但简洁的人工智能助手，直截了当地回答问题。",
            },
            {"role": "user", "content": prompt_with_history},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response

def calculate_llm_cost(characters, price_per_1000_tokens=0.015):
    """此函数接受一个字符数作为输入，并根据给定的价格计算模型的成本。"""
    tokens = characters / 4
    cost = (tokens / 1000) * price_per_1000_tokens
    return f"${cost:.4f}"
