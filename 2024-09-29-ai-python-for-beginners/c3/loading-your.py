from helper_functions import *

# 打开食谱文件并读取内容
f = open("docs/recipe.txt", "r")
recipe = f.read()
f.close()

prompt = f"""请总结以下文本的内容，最多两句话。

文本：
{recipe}"""

response=get_llm_response(prompt)
print(response)