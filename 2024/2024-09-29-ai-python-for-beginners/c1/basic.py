# print
print("你好，世界")
print("""你好，世界！
      很高兴来到这里！""")


# type 
type("123")
type(123)


# 表达式
print(28+35+43+50+65+70+68+66+75+80+95)

# 运算顺序
print(75 - 32 * 5 / 9)
print((75 - 32) * 5 / 9)

# 格式化输出
print(f"75华氏度转换为摄氏度为 {(75 - 32) * 5 / 9}摄氏度")
print(f"""
    大多数国家使用公制系统来测量食谱，但美国烘焙师使用不同的系统。例如，他们使用液体盎司来测量液体，而不是毫升（ml）。
    
    所以你需要将食谱单位转换为你当地的计量系统！
    
    例如，8液体盎司的牛奶是 {8 * 29.5735} 毫升。
    而100毫升的水是 {100 / 29.5735} 液体盎司。
""")

# 变量
age = 28
name = "Otto"
gnome_height = 12.7

print(f"Age: {age}")
print(f"Name: {name}")
print(f"Gnome height: {gnome_height}")

score = 0
score = score + 50
print(score) 

dog_age = 49 / 7
print(f"""奥托的狗年龄是 {dog_age} 岁。因此，一只大约 {dog_age} 岁的狗与奥托的年龄相同。任何大约在 {dog_age} 年前出生的狗，都处于与奥托相同的生活阶段。""")

# 函数
print(type(123))
print( len("你好，世界！") )
print(round(42.17))