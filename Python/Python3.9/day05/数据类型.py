v1 = 5 / 2
print(v1)

v1 = "1238871"
result = v1.isdecimal()
print(result)  # True

# 案例,两个数相加。

# v1 = input("请输入值：")  # ”666“
# v2 = input("请输入值：")  # ”999“
# if v1.isdecimal() and v2.isdecimal():
#     data = int(v1) + int(v2)
#     print(data)
# else:
#     print("请正确输入数字")

data = "武沛齐|root|wupeiqi@qq.com"
result = data.split('|')  # ["武沛齐","root","wupeiqi@qq.com"]
print(data)  # "武沛齐|root|wupeiqi@qq.com"
print(result)  # 输出 ["武沛齐","root","wupeiqi@qq.com"] 根据特定字符切开之后保存在列表中，方便以后的操作

data = "武沛齐|root|wupeiqi@qq.com"
v1 = data.split("|")  # ['武沛齐', 'root', 'wupeiqi@qq.com']
print(v1)

v2 = data.split("|", 1)  # ['武沛齐', 'root|wupeiqi@qq.com']
print(v2)

data = "武沛齐,root,wupeiqi@qq.com"

v1 = data.rsplit(',')
print(v1)  # ['武沛齐', 'root', 'wupeiqi@qq.com']

v2 = data.rsplit(',', 1)
print(v2)  # ['武沛齐,root', 'wupeiqi@qq.com']

str
