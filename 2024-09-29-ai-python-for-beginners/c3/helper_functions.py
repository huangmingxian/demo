#import gradio as gr
import os

from openai import OpenAI
import io
import csv


# 设置 OpenAI 客户端
client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url=os.getenv("ZHIPU_BASE_URL")
)

model = "glm-4-flash"


def read_csv_dict(csv_file_path):
    """此函数读取 CSV 文件并将其加载为字典。"""

    # 初始化一个空列表来存储数据
    data_list = []

    # 打开 CSV 文件
    with open(csv_file_path, mode='r') as file:
        # 创建一个 CSV 阅读器对象
        csv_reader = csv.DictReader(file)
    
        # 遍历 CSV 文件中的每一行
        for row in csv_reader:
            # 将该行追加到数据列表中
            data_list.append(row)

    # 将列表转换为字典
    data_dict = {i: data_list[i] for i in range(len(data_list))}
    return data_dict


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

def list_files_in_directory(directory='.'):
    """
    列出指定目录中所有非隐藏文件。
    
    参数:
        directory (str): 列出文件的目录。默认为当前工作目录。
    """
    try:
        files = [f for f in os.listdir(directory) if (not f.startswith('.') and not f.startswith('_'))]
        for file in files:
            print(file)
    except Exception as e:
        print(f"发生错误: {e}")

def read_journal(journal_file):
    f = open(journal_file, "r")
    journal = f.read()
    f.close()
    return journal