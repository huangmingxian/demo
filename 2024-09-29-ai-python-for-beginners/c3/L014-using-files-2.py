from helper_functions import get_llm_response

f = open("docs/email.txt", "r")
email = f.read()
f.close()

prompt = f"""从以下电子邮件中提取要点。
包括发件人信息。

电子邮件：
{email}"""

bullet_points= get_llm_response(prompt)
print(bullet_points)
