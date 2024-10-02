from helper_functions import print_llm_response, get_llm_response

name="张三"

prompt = f"""
为我的朋友{name}写一首四行的生日诗。
这首诗应该以我朋友名字的第一个字母为灵感。
"""

# print_llm_response(prompt)

friends_list = ["张三", "李四", "王五"]

# print(friends_list)
# print(type(friends_list))
# print(len(friends_list))

prompt = f"""
为我的朋友们{friends_list}写一组四行的生日诗。
这些诗应该以每个朋友名字的第一个字母为灵感。
"""

# print_llm_response(prompt)

list_of_tasks = [
    "给我的老板写一封简短的电子邮件，解释我明天的会议会迟到。",
    "为奥托写一首生日诗，庆祝他的28岁生日。",
    "写一篇300字的电影《降临》的影评。"
]

task = list_of_tasks[0]
print_llm_response(task)
