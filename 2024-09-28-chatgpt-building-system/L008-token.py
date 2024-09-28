from tool import *

response = get_completion("Take the letters in lollipop \
and reverse them")
print(response)

response = get_completion("""Take the letters in \
l-o-l-l-i-p-o-p and reverse them""")

print(response)

messages = [
    {"role": "user", "content": "Take the letters in l-o-l-l-i-p-o-p and reverse them"},
    {"role": "system", "content": "你是一个很有用的助手。"},
]
content,token_dict= get_completion_and_token_count(messages)

print(token_dict)