#import gradio as gr
import os

from openai import OpenAI
import io



# 设置 OpenAI 客户端
client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url=os.getenv("ZHIPU_BASE_URL")
)

model = "glm-4-flash"

def print_llm_response(prompt):
    """此函数接受一个字符串形式的提示，并将其传递给 智谱 AI 的 glm-flash-4 模型。
    然后打印模型的响应结果。
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("输入必须是用引号括起来的字符串。")
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "你是一个简明扼要的 AI 助手，直接切入重点。",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        response = completion.choices[0].message.content
        print(response)
    except TypeError as e:
        print("错误:", str(e))


def get_llm_response(prompt):
    """此函数接受一个字符串形式的提示，并将其传递给 OpenAI 的 GPT3.5 模型。
    函数会将模型的响应保存为字符串。
    """
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "你是一个简明扼要的 AI 助手，直接切入重点。",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response

    f = open(file, "r")
    
    csv_reader = csv.DictReader(f)
    data = []
    for row in csv_reader:
        data.append(row)
    f.close()
    
    return data