from helper_functions import *

files = ["cape_town.txt", "istanbul.txt", "new_york.txt", "paris.txt", 
          "rio_de_janeiro.txt", "sydney.txt", "tokyo.txt"]

for file in files:
    
    filename ="docs/" + file
    journal_entry = read_journal(filename)

    prompt = f"""请从以下日记条目中提取包含所有餐馆及其对应最佳菜肴的完整列表。
    确保准确识别并列出每个餐馆名称。

    将答案提供为 CSV 格式，准备保存。
    排除 "```csv" 声明，不要在逗号后添加空格，包含列标题。

    格式：
    Restaurant, Dish
    Res_1, Dsh_1
    ...

    日记条目：
    {journal_entry}
    """
    
    print_llm_response(prompt)
    print("") 