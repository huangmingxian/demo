from helper_functions import print_llm_response, get_llm_response

import csv

def read_csv(file):
    f = open(file, "r")

    csv_reader = csv.DictReader(f)
    data = []
    for row in csv_reader:
        data.append(row)
    f.close()

    return data

itinerary = read_csv("docs/itinerary.csv")
print(itinerary)


def read_journal(journal_file):
    f = open(journal_file, "r")
    journal = f.read()
    f.close()

    # Return the journal content
    return journal

journal = read_journal("docs/sydney.txt")

print(journal)


prompt = f"""请从以下日志条目中提取餐馆及其相应特色菜的完整列表。
确保准确识别并列出每家餐馆的名称。
以 CSV 格式提供答案，准备保存。
请排除 "```csv" 声明，逗号后不加空格，并包含列标题。

格式:
餐馆, 特色菜
餐馆_1, 特色菜_1
...

日志条目:
{journal}
"""

print_llm_response(prompt)