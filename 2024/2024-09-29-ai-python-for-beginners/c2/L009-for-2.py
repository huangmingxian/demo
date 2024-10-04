from helper_functions import print_llm_response, get_llm_response

list_of_tasks = [
    "给我的老板写一封简短的电子邮件，解释我明天的会议会迟到。",
    "为奥托写一首生日诗，庆祝他的28岁生日。",
    "写一篇300字的电影《降临》的影评。"
]

for task in list_of_tasks:
    print_llm_response(task)
    