friends_list = ["张三", "李四", "王五"]

print(friends_list)
print(type(friends_list))
print(len(friends_list))

first_friend = friends_list[0]
print(first_friend)
print(friends_list[1])
friends_list.append("老六")
friends_list.remove("张三")
print(friends_list)