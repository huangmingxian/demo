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
        {"role": "system", "content": "当我请求帮助写一些东西时，你会回复一份文档，其中每段至少包含一个笑话或有趣的评论。"},
        {"role": "user", "content": "给我的螺纹钢供应商写一封感谢信，感谢他们在短时间内准时交货。这使我们能够交付一份重要的订单。"},
    ],
    stream=False
)

# 3. 打印返回的对话的文本
print(response.choices[0].message.content)
