# 打印布尔类型的值
print(True)
print(False)

# 查看类型
print(type(True))
print(type(False))

# 比较操作返回布尔类型
isabel_age = 28
daniel_age = 30
tommy_age = 30

print(isabel_age > daniel_age)     
print(tommy_age <= daniel_age)
print(isabel_age == daniel_age) 

is_isabel_older_than_daniel = isabel_age > daniel_age
print(is_isabel_older_than_daniel)

# 逻辑运算符
is_tommy_my_friend = True
is_isabel_my_friend = True
print(is_tommy_my_friend and is_isabel_my_friend)
print(is_tommy_my_friend or is_isabel_my_friend)

isabel_age = 28
daniel_age = 30
otto_age = 29
is_isabel_younger_than_tommy = isabel_age < tommy_age
is_isabel_younger_than_daniel = isabel_age < daniel_age
print(is_isabel_younger_than_tommy and is_isabel_younger_than_daniel)