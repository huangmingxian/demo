import requests
import json
import os

url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
headers = {
    "Authorization": os.getenv("ZHIPU_API_KEY"),
    "Content-Type": "application/json"
}
data = {
    "model": "glm-4-flash",
    "messages": [
        {"role": "system", "content": "你是一个很有用的助手"},
        {"role": "user", "content": "你好，你是谁？"}
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
response_json = response.json()

print(response_json['choices'][0]['message']['content'])