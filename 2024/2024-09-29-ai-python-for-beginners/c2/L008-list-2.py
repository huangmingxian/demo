from helper_functions import *

friends_list = ["张三", "李四", "王五"]

prompt = f"""
为我的朋友们{friends_list}写一组四行的生日诗。
这些诗应该以每个朋友名字的第一个字母为灵感。
"""

print_llm_response(prompt)

