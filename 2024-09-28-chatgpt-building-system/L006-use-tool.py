from tool import get_completion_from_messages

messages=[
    {"role": "system", "content": "当我请求帮助写一些东西时，你会回复一份文档，其中每段至少包含一个笑话或有趣的评论。"},
    {"role": "user", "content": "给我的螺纹钢供应商写一封感谢信，感谢他们在短时间内准时交货。这使我们能够交付一份重要的订单。"}
]

print(get_completion_from_messages(messages))