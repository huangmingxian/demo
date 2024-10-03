from helper_functions import *

# 1. 读取文件
f = open("docs/rio_de_janeiro.txt", "r")
journal_rio_de_janeiro = f.read()
f.close()

# 2. 写提示词
prompt = f"""
根据以下美食评论家的日记条目，识别餐馆及其最佳菜肴。
在原文中将每个餐馆标记为橙色加粗，将最佳菜肴标记为蓝色加粗。

将输出内容为 HTML ，不需要用代码块包裹。

日记条目：
{journal_rio_de_janeiro}
"""

# 3. 向 AI 提问
response = get_llm_response(prompt)
print(response)


# 4. 保存结果
f = open("outputs/rio_de_janeiro.html", "w")
f.write(response)
f.close()