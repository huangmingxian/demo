from helper_functions import print_llm_response

high_priority_tasks = [
    "写一封简短的邮件给我的老板，解释我明天的会议会迟到。",
    "创建一个关于远程工作优势的演讲大纲。"
]

medium_priority_tasks = [
    "为奥托写一首庆祝他28岁生日的生日诗。",
    "为我的邻居达平德写一封感谢信，他在我度假时帮忙浇花。"
]

low_priority_tasks = [
    "写一篇300字的电影《降临》影评。"
]

prioritized_tasks = {
    "high_priority": high_priority_tasks,
    "medium_priority": medium_priority_tasks,
    "low_priority": low_priority_tasks
}

# 让 AI 处理高优先级的任务
for task in prioritized_tasks["high_priority"]:
    print_llm_response(task)