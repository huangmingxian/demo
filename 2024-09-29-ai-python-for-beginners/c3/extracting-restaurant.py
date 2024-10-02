from helper_functions import *

journal_rio_de_janeiro = read_journal("docs/rio_de_janeiro.txt")

prompt = f"""
根据以下食品评论家的日志条目，识别餐厅及其最佳菜肴。
在原始文本中突出并加粗每个餐厅（橙色）和最佳菜肴（蓝色）。

日志条目：
{journal_rio_de_janeiro}
"""

response = get_llm_response(prompt)
print(response)