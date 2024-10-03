from helper_functions import *

# 列出所有的文件名
files = ["cape_town.txt", "madrid.txt", "rio_de_janeiro.txt", "sydney.txt", "tokyo.txt"]

for file in files:
    # 读取城市的日志文件
    f = open("docs/" + file, "r")
    journal = f.read()
    f.close()

    # 创建提示
    prompt = f"""请回复"相关"或"不相关"：
    日志是否描述了餐厅及其特色菜肴。

    日志：
    {journal}"""

    # 使用LLM判断日志条目是否有用
    print(f"{file} -> {get_llm_response(prompt)}")
