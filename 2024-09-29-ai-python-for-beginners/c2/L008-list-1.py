from helper_functions import *

name="张三"

prompt = f"""
为我的朋友{name}写一首四行的生日诗。
这首诗应该以我朋友名字的第一个字母为灵感。
"""

print_llm_response(prompt)
