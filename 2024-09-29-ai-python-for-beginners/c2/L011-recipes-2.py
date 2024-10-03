from helper_functions import *

# 用字典来定义 Tom 的食物偏好
food_preferences_tommy = {
    "dietary_restrictions": "素食主义",
    "favorite_ingredients": ["豆腐", "橄榄"],
    "experience_level": "中级",
    "maximum_spice_level": 6
}

# 提供的香料列表
available_spices = ["孜然", "姜黄", "牛至", "红椒粉"]

prompt = f"""请推荐一个包含以下食材的食谱：
{food_preferences_tommy["favorite_ingredients"]}。
食谱应符合以下饮食限制：
{food_preferences_tommy["dietary_restrictions"]}。
食谱的难度级别应该是：
{food_preferences_tommy["experience_level"]}。
在 10 分制的辣度等级中，最高辣度应该是：
{food_preferences_tommy["maximum_spice_level"]}。
请提供一个两句话的描述。

食谱中不应包含此列表以外的香料：
香料：{available_spices}
"""
print(prompt)

recipe = get_llm_response(prompt)
print(recipe)