from helper_functions import *

# 获取行程的详细信息
itinerary = read_csv("docs/itinerary.csv")


# 获取某一站信息
trip_stop = itinerary[6]
city = trip_stop["City"]
country = trip_stop["Country"]
arrival = trip_stop["Arrival"]
departure = trip_stop["Departure"]

# 获取对应城市的餐厅信息
sydney_restaurants = read_csv("docs/Sydney.csv")
restaurants = sydney_restaurants

prompt = f"""我将从 {arrival} 到 {departure} 访问 {city}, {country}。
请创建一个包含详细活动的每日行程。
为早餐、午餐和晚餐指定时间。

我想访问餐馆字典中列出的餐馆，且不要重复任何地点。
请确保提到我应该在每个餐馆尝试的特色菜。

餐馆字典:
{restaurants}

"""

print_llm_response(prompt)


# 创建一个空字典来存储每个目的地的详细行程
detailed_itinerary = {}

 # 遍历行程中的每一站
for trip_stop in itinerary:
    city = trip_stop["City"]
    country = trip_stop["Country"]
    arrival = trip_stop["Arrival"]
    departure = trip_stop["Departure"]

    rest_dict = read_csv(f"docs/{city}.csv")

    print(f"正在为 {city}, {country} 创建详细行程。")

    prompt = f"""我将从 {arrival} 到 {departure} 访问 {city}, {country}。
    请创建一个包含详细活动的每日行程。
    为早餐、午餐和晚餐指定时间。

    我想访问餐馆字典中列出的餐馆，且不要重复任何地点。
    请确保提到我应该在每个餐馆尝试的特色菜。

    餐馆字典:
    {rest_dict}

    """
    # 将该城市的详细行程存储到字典中
    detailed_itinerary[city] = get_llm_response(prompt)

print(detailed_itinerary)