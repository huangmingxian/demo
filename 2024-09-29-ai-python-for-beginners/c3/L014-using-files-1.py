from helper_functions import get_llm_response

# 写下食材列表
ingredients = ['鸡肉', '西兰花', '米饭']

# 编写提示
prompt = f"""
    创建一个使用以下食材的简短食谱：
    {ingredients}
"""

# 从 LLM 获取响应
response = get_llm_response(prompt)

# 打印 LLM 响应
print(response)
