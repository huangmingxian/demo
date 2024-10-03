from helper_functions import print_llm_response, get_llm_response

ice_cream_flavors = [
    "香草", "巧克力", "草莓", "薄荷巧克力碎片"
]


promotional_descriptions = []
for flavor in ice_cream_flavors:
    prompt = f"""对于冰淇淋口味列表中的每一种口味，
    提供一个吸引人的描述，可用于促销目的

    口味: {flavor}
    """
    description = get_llm_response(prompt)
    promotional_descriptions.append(description)
    
print(promotional_descriptions)