import os
from openai import OpenAI
from rich import print

# 1. 创建 OpenAI 客户端，这里调用了之前设置的环境变量
client = OpenAI(
    api_key=os.environ.get("ZHIPU_API_KEY"),
    base_url=os.environ.get("ZHIPU_BASE_URL")
)

#  2. 完成一次对话
response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "system", "content": "以一致的风格回答"},
        {"role": "user", "content": "教我耐心。"},
        {"role": "assistant", "content": "河流冲刷出最深的山谷，发源于温和的泉水；最伟大的交响乐源自一个音符；最复杂的挂毯都是从一根单独的线开始的。"},
        {"role": "user", "content": "教我有关海洋的知识。"}
    ],
    stream=False
)

# 3. 打印返回的对话的文本
print(response.choices[0].message.content)
