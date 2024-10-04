from helper_functions import *
import csv

# 1. 读取 CSV 文件
f = open("docs/itinerary.csv", 'r')

# 2. 使用 csv.DictReader 读取 CSV 文件,将CSV文件的每一行读取为一个字典，其中列名作为字典的键，保存为一个列表
csv_reader = csv.DictReader(f)

itinerary = []
for row in csv_reader:
    itinerary.append(row)
    
f.close()
print(itinerary)

# 3. 从 itinerary 列表中提取第一站的信息
trip_stop = itinerary[0]
city = trip_stop["City"]
country = trip_stop["Country"]
arrival = trip_stop["Arrival"]
departure = trip_stop["Departure"]

# 4. 请求 LLM 生成一个详细的每日行程。
prompt = f"""我将从 {arrival} 到 {departure} 访问 {city}, {country}。
请创建一个详细的每日行程。"""

response = get_llm_response(prompt)
print(response)