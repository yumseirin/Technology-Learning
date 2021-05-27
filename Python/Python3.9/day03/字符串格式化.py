# 百分号
name = "武沛齐"
text = "我叫%s，今年18岁" % name

name = "武沛齐"
age = 18
text = "我叫%s，今年%d岁" % (name, age)

tpl = "i am %s" % "alex"
print(tpl)
tpl = "i am %s age %d" % ("alex", 18)
print(tpl)
tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}
print(tpl)
tpl = "percent %.2f" % 99.97623
print(tpl)
tpl = "i am %(pp).2f" % {"pp": 123.425556, }
print(tpl)
tpl = "i am %(pp).2f%%" % {"pp": 123.55, }
print(tpl)

message = "%(name)s你什么时候过来呀？%(user)s今天不在呀。" % {"name": "死鬼", "user": "李杰"}
print(message)

text = "%s，这个片我已经下载了90%%了，居然特么的断网了" % "兄弟"
print(text)

# format
text = "我叫{0}，今年18岁".format("武沛齐")
text = "我叫{0}，今年{1}岁".format("武沛齐", 18)
text = "我叫{0}，今年{1}岁，真是的姓名是{0}。".format("武沛齐", 18)

text = "我叫{}，今年18岁".format("武沛齐")
text = "我叫{}，今年{}岁".format("武沛齐", 18)
text = "我叫{}，今年{}岁，真是的姓名是{}。".format("武沛齐", 18, "武沛齐")

text = "我叫{n1}，今年18岁".format(n1="武沛齐")
text = "我叫{n1}，今年{age}岁".format(n1="武沛齐", age=18)
text = "我叫{n1}，今年{age}岁，真是的姓名是{n1}。".format(n1="武沛齐", age=18)

text = "我叫{0},今年{1}"
data1 = text.format("aaa", 18)
data2 = text.format("bbb", 20)
print(data1)
print(data2)

text = "我叫%s，今年%d岁"
data1 = text % ("aaa", 18)
data2 = text % ("bbb", 20)
print(data1)
print(data2)

# f

action = "跑步"
text = f"嫂子喜欢{action}，跑完之后满身大汗。"
print(text)

name = "喵喵"
age = 19
text = f"嫂子的名字叫{name}，今年{age}岁"
print(text)

text = f"嫂子的名字叫喵喵，今年{19 + 2}岁"
print(text)

# 在Python3.8引入
text = f"嫂子的名字叫喵喵，今年{19 + 2=}岁"
print(text)

# 进制转换
v1 = f"嫂子今年{22}岁"
print(v1)

v2 = f"嫂子今年{22:#b}岁"  # 转换二进制
print(v2)

v3 = f"嫂子今年{22:#o}岁"  # 转换八进制
print(v3)

v4 = f"嫂子今年{22:#x}岁"  # 转换十六进制
print(v4)

v2 = "" or "alex"
print(v2)
