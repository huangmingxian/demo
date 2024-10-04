# 定义一个函数，用于将华氏度转换为摄氏度
def fahrenheit_to_celsius(fahrenheit):
    # 将华氏度转换为摄氏度
    celsius = (fahrenheit - 32) * 5 / 9
    # 输出转换结果，保留两位小数
    print(f"{fahrenheit}°F 相当于 {celsius:.2f}°C")

fahrenheit_to_celsius(68)