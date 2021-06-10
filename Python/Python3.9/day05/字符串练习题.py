# 1
data = "alibaba"
if data.startswith("al"):
    print("是的")
else:
    print("不是的")

# 2
data = "alibabaNb"
if data.endswith("Nb"):
    print("是的")
else:
    print("不是的")

# 3
name = "bilibili"
pname = name.replace('l', 'p')
print(pname)

# 4
# data = input("请输入整数")
# if data.isdecimal():
#     print(int(data))
# else:
#     print("请输入数字")

# 5
data1 = "5+9"
data2 = "al+999"
sum = 0
number = data1.split("+")
print(number)
for num in number:
    if not num.isdecimal():
        print("输入的值不都是数字")
        sum += 1
        break
if sum == 0:
    print("所有的值都是数字")

# 6
# data = input("请输入两个整数相加")
# tip = 0
# sum = 0
# number = data.split("+")
# print(number)
# for num in number:
#     if not num.isdecimal():
#         print("输入的值不都是数字")
#         tip = 1
#         break
#     else:
#         sum += int(num)
# if tip != 1:
#     print(sum)
#     print(data+"="+str(sum))

# 7
# data = input("请输入两个整数相加")
# tip = 0
# sum = 0
# number = data.split("+")
# print(number)
# for num in number:
#     num = num.strip()
#     if not num.isdecimal():
#         print("输入的值不都是数字")
#         tip = 1
#         break
#     else:
#         sum += int(num)
# if tip != 1:
#     print(sum)
#     print(data + "=" + str(sum))

# 8
# import random
#
# code = random.randrange(1000, 9999)  # 生成动态验证码
# code = str(code)
# msg = '欢迎登陆PythonAV系统，您的验证码为：{}，手机号为：{}'.format(code, "12345678901")
# print(msg)
# yzm = input("请输入验证码：")
# phone = input("请输入手机号：")
# if yzm.upper() == code.upper() and phone.strip() == "12345678901":
#     print("登录成功")
# else:
#     print("登录失败")

# 9
data_list = []
while True:
    hobby = input("请输入你的爱好(Q/q)退出：")
    if hobby.upper() == 'Q':
        break
    # 把输入的值添加到data_list中，如：data_list = [“小姨子”,"哥们的女朋友]
    else:
        data_list.append(hobby)
# 将所有的爱好通过符号“、”拼接起来并输出
hobbys = "、".join(data_list)
print(hobbys)
