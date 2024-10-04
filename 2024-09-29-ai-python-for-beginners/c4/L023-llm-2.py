import os
from openai import OpenAI

# 1. 创建 OpenAI 客户端，这里调用了之前设置的环境变量
client = OpenAI(
    api_key=os.environ.get("ZHIPU_API_KEY"),
    base_url=os.environ.get("ZHIPU_BASE_URL")
)

#  2. 完成一次对话
response = client.chat.completions.create(
    model="glm-4-flash", # 调用智谱的免费模型
    messages=[
        {"role": "system", "content": "你是一个很有用的助手"},
        {"role": "user", "content": "你好,请问你是谁?"},
    ],
    stream=False
    # API 的响应将一次性返回完整的生成内容, 而不是流式返回生成的内容。

)

# 3.看看返回的数据结构
print(response)

# 4. 打印返回的对话的文本
print(response.choices[0].message.content)