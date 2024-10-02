from helper_functions import *

f = open("docs/cape_town.txt", "r")
journal_cape_town = f.read()
f.close()


f = open("docs/tokyo.txt", "r")
journal_tokyo = f.read() 
f.close()

prompt = f"""请回复“相关”或“不相关”： 
该日志描述了餐厅及其特色菜。

日志：
{journal_tokyo}"""

response = get_llm_response(prompt)
print(response)