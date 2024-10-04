from helper_functions import *

journal_rio_de_janeiro = read_journal("docs/rio_de_janeiro.txt")

prompt = f"""请从以下日记条目中提取包含所有餐馆及其对应最佳菜肴的完整列表。
确保准确识别并列出每个餐馆名称。

将答案提供为 CSV 格式，准备保存。
排除 "```csv" 声明，不要在逗号后添加空格，包含列标题。

格式：
Restaurant, Dish
Res_1, Dsh_1
...

日记条目：
{journal_rio_de_janeiro}
"""

response = get_llm_response(prompt)
print(response)