from helper_functions import *

task_list = [
    {
        "description": "撰写一封简短的电子邮件给我的老板，说明我下周会议会迟到。",
        "time_to_complete": 3
    },
    {
        "description": "为关于远程工作的好处的演示创建一个大纲。",
        "time_to_complete": 60
    },
    {
        "description": "撰写一篇关于电影《降临》的300字评论。",
        "time_to_complete": 30
    },
    {
        "description": "为豆腐和橄榄炒菜创建一个购物清单。",
        "time_to_complete": 5
    }
]

tasks_for_later = []

for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do)
    else:
        tasks_for_later.append(task)
        
print(tasks_for_later)