from helper_functions import print_llm_response, get_llm_response

list_of_tasks = [
    "给我的老板写一封简短的电子邮件，解释我明天的会议会迟到。",
    "为奥托写一首生日诗，庆祝他的28岁生日。",
    "写一篇300字的电影《降临》的影评。"
]

for task in list_of_tasks:
    print_llm_response(task)
    
ice_cream_flavors = [
    "香草", "巧克力", "草莓", "薄荷巧克力碎片" 
]

for flavor in ice_cream_flavors:
    prompt = f"""对于冰淇淋口味列表中的每一种口味，
    提供一个吸引人的描述，可用于促销目的

    口味: {flavor}

    """
    print_llm_response(prompt)
    

promotional_descriptions = []
for flavor in ice_cream_flavors:
    prompt = f"""对于冰淇淋口味列表中的每一种口味，
    提供一个吸引人的描述，可用于促销目的

    口味: {flavor}
    """
    description = get_llm_response(prompt)
    promotional_descriptions.append(flavor + ":" + description)
    
print(promotional_descriptions)