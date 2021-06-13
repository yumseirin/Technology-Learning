# day05数据类型

常见的数据类型：

- int，整数类型（整形）
- bool，布尔类型
- str，字符串类型
- list，列表类型
- tuple，元组类型
- dict，字典类型
- set，集合类型
- float，浮点类型（浮点型）



## 1.整型

整型其实就是十进制整数的统称，比如：1、68、999都属于整型。他一般用于表示 年龄、序号等。

### 1.1 定义

```python
number = 10
age = 99
```

### 1.2 独有功能

无

```python
v1 = 5
print(bin(v1))  # 0b101
# 调用v1（int）的独有功能，获取v1的二进制有多少个位组成。
result1 = v1.bit_length()
print(result1)  # 3

v2 = 10
print(bin(10))  # 0b1010
# 调用v2（int）的独有功能，获取v2的二进制有多少个位组成。
result2 = v2.bit_length()
print(result2)  # 4
```

### 1.3 公共功能

加减乘除

```python
v1 = 4
v2 = 8
v3 = v1 + v2
```

### 1.4 转换

在项目开发和面试题中经常会出现一些 "字符串" 和 布尔值 转换为 整型的情况。

```python
# 布尔值转整型
n1 = int(True)  # True转换为整数 1
n2 = int(False) # False转换为整数 0

# 字符串转整型
v1 = int("186",base=10) # 把字符串看成十进制的值，然后再转换为 十进制整数，结果：v1 = 186
v2 = int("0b1001",base=2) # 把字符串看成二进制的值，然后再转换为 十进制整数，结果：v1 = 9 (0b表示二进制)
v3 = int("0o144",base=8)  # 把字符串看成八进制的值，然后转换为 十进制整数，结果：v1 = 100 (0o表示八进制)
v4 = int("0x59",base=16)  # 把字符串看成十六进制的值，然后转换为 十进制整数，结果：v1 = 89 （0x表示十六进制）

# 浮点型（小数）
v1 = int(8.7) # 8
```

所以，如果以后别人给你一个按 二进制、八进制、十进制、十六进制 规则存储的字符串时，可以轻松的通过int转换为十进制的整数。

### 1.5 其他

#### 1.5.1 长整型

- Python3：整型（无限制）
- Python2：整型、长整形

在python2中跟整数相关的数据类型有两种：int(整型)、long（长整型），他们都是整数只不过能表示的值范围不同。

<img src="day05数据类型.assets/image-20201102190227431.png" alt="image-20201102190227431" style="zoom:50%;" />

- int，可表示的范围：-9223372036854775808～9223372036854775807
- long，整数值超出int范围之后自动会转换为long类型（无限制）。

在python3中去除了long只剩下：int（整型），并且 int 长度不在限制。

#### 1.5.2 地板除

- Py3：

  ```python
  v1 = 9/2 
  print(v1) # 4.5
  ```

- py2:

  ```python
  v1 = 9/2 
  print(v1) # 4
  ```

  ```python
  from __future__ import division 
  
  v1 = 9/2 
  print(v1) # 4.5
  ```

  

## 2. 布尔类型

布尔值，其实就是 “真”、“假” 。

### 2.1 定义

```python
data = False
alex_is_sb = True
```

### 2.2 独有功能

无

### 2.3 公共功能

无

```python
v1 = True + True
print(v1) # 2
```

### 2.4 转换

在以后的项目开发中，会经常使用其他类型转换为布尔值的情景，此处只要记住一个规律即可。

```
整数0、空字符串、空列表、空元组、空字典转换为布尔值时均为False
其他均为True
```

```python
# 练习题：查看一些变量为True还是False
v1 = bool(0)
v2 = bool(-10)
v3 = bool(10)
v4 = bool("武沛齐")
v5 = bool("")
v6 = bool(" ")
v7 = bool([]) # [] 表示空列表
v8 = bool([11，22，33]) # [11，22，33] 表示非空列表
v9 = bool({}) # {} 表示空字典
v10 = bool({"name":"武沛齐","age":18}) # {"name":"武沛齐","age":18} 表示非空字典
```

### 2.5 其他

#### 2.5.1 做条件自动转换

如果在 `if` 、`while` 条件后面写一个值当做条件时，他会默认转换为布尔类型，然后再做条件判断。

```python
if 0:
	print("太六了")
else:
  print(999)

if "武沛齐":
	print("你好")

if "alex":
	print("你是傻逼？")
else:
	print("你是逗比？")
```

```python
while 1>9:
  pass
```

```python
if 值:
  pass

while 值:
  pass
```

## 3.字符串类型

字符串，我们平时会用他来表示文本信息。例如：姓名、地址、自我介绍等。

### 3.1 定义

```python
v1 = "包治百病"
v2 = '包治百病'
v3 = "包'治百病"
v4 = '包"治百病'
v5 = """
吵架都是我的错，
因为大家打不过。
"""
# 三个引号，可以支持多行/换行表示一个字符串，其他的都只能在一行中表示一个字符串。
```



### 3.2 独有功能（18/48）

```python
"xxxxx".功能(...)

v1 = "xxxxx"
v1.功能(...)
```



1. 判断字符串是否以 XX 开头？得到一个布尔值

   ```python
   v1 = "叨逼叨的一天，烦死了"
   
   # True
   result = v1.startswith("叨逼叨的一天")
   
   print(result) # 值为True
   ```

   ```python
   # 案例
   v1 = input("请输入住址：")
   
   if v1.startswith("北京市"):
   	print("北京人口")
   else:
   	print("非北京人口")
   ```

2. 判断字符串是否以 XX 结尾？得到一个布尔值

   ```python
   v1 = "叨逼叨的一天，烦死了"
   
   result = v1.endswith("烦死了")
   
   print(result) # 值为True
   ```

   ```python
   # 案例
   address = input("请输入地址：")
   
   if address.endswith('村'):
   	print("农业户口")
   else:
   	print("非农户口")
   ```

3. 判断字符串是否为十进制数？得到一个布尔值

   ```python
   v1 = "1238871"
   result = v1.isdecimal()
   print(result) # True
   ```

   ```python
   # 案例,两个数相加。
   
   v1 = input("请输入值：") # ”666“
   v2 = input("请输入值：") # ”999“
   if v1.isdecimal() and v2.isdecimal():
   	data = int(v1) + int(v2)
   	print(data)
   else:
   	print("请正确输入数字")
   ```

   ```python
   v1 = "123"
   print(v1.isdecimal()) # True
   
   v2 = "①"
   print(v2.isdecimal()) # False
   
   v3 = "123"
   print(v3.isdigit()) # True
   
   v4 = "①"
   print(v4.isdigit()) # True
   ```

4. 去除字符串两边的 空格、换行符、制表符，得到一个新字符串

   ```python
   data = input("请输入内容：") #武沛齐,武沛齐   
   print(data)
   ```

   ```python
   msg = " H e ll o啊，树哥 "
   data = msg.strip()
   print(data) # 将msg两边的空白去掉，得到"H e ll o啊，树哥"
   ```

   ```python
   msg = " H e ll o啊，树哥 "
   data = msg.lstrip()
   print(data) # 将msg左边的空白去掉，得到"H e ll o啊，树哥 "
   ```

   ```python
   msg = " H e ll o啊，树哥 "
   data = msg.rstrip()
   print(data) # 将msg右边的空白去掉，得到" H e ll o啊，树哥"
   ```

   补充：去除 空格、换行符、制表符。

   ```python
   # 案例
   code = input("请输入4位验证码：") #  FB87 
   data = code.strip()
   if data == "FB87":
   	print('验证码正确')
   else:
   	print("验证码错误")
   ```

   再补充：去除字符串两边指定的内容

   ```python
   msg = "哥H e ll o啊，树哥"
   data = msg.strip("哥")
   print(data) # 将msg两边的空白去掉，得到"H e ll o啊，树"
   ```

   ```python
   msg = "哥H e ll o啊，树哥"
   data = msg.lstrip("哥")
   print(data) # 将msg左边的空白去掉，得到"H e ll o啊，树哥"
   ```

   ```python
   msg = "哥H e ll o啊，树哥"
   data = msg.rstrip("哥")
   print(data) # 将msg右边的空白去掉，得到"哥H e ll o啊，树"
   ```

5. 字符串变大写，得到一个新字符串

   ```python
   msg = "my name is oliver queen"
   data = msg.upper()
   
   print(msg) # my name is oliver queen
   print(data) # 输出为：MY NAME IS OLIVER QUEEN
   ```

   ```python
   # 案例
   code = input("请输入4位验证码：") #  FB88   fb88 
   value = code.upper() #  FB88  
   data = value.strip() # FB88
   
   if data == "FB87":
   	print('验证码正确')
   else:
   	print("验证码错误")
     
   # 注意事项
   """
   code的值"fb88 "
   value的值"FB88 "
   data的值"FB88"
   """
   ```

6. 字符串变小写，得到一个新字符串

   ```python
   msg = "My Name Is Oliver Queen"
   data = msg.lower()
   
   print(data) # 输出为：my name is oliver queen
   ```

   ```python
   # 案例
   code = input("请输入4位验证码：")
   value = code.strip().lower()
   if value == "fb87":
   	print('验证码正确')
   else:
   	print("验证码错误")
   ```

7. 字符串内容替换，得到一个新的字符串

   ```python
   data = "你是个好人，但是好人不合适我"
   value = data.replace("好人","贱人")
   print(data)  # "你是个好人，但是好人不合适我"
   print(value) # "你是个贱人，但是贱人不合适我"
   ```

   ```python
   # 案例
   video_file_name = "高清无码爱情动作片.mp4"
   
   new_file_name = video_file_name.replace("mp4","avi") # "高清无码爱情动作片.avi"
   
   final_file_name = new_file_name.replace("无码","步兵") # "高清步兵爱情动作片.avi"
   
   print(final_file_name)
   ```

   ```python
   # 案例
   video_file_name = "高清无码爱情动作片.mp4"
   
   new_file_name = video_file_name.replace("mp4","avi") # "高清无码爱情动作片.avi"
   
   final_file_name = video_file_name.replace("无码","步兵") # "高清步兵爱情动作片.mp4"
   
   print(final_file_name)
   ```

   ```python
   # 案例
   content = input("请输入评论信息") # alex是一个草包
   content = content.replace("草","**") # alex是一个**包
   content = content.replace("泥马","***") # alex是一个**包
   print(content) # alex是一个**包
   ```

   ```python
   char_list = ["草拟吗","逗比","二蛋","钢球"]
   
   content = input("请输入评论信息")
   for item in char_list:
     content = content.repalce(item,"**")
   
   print(content)
   ```

8. 字符串切割，得到一个列表 

   ```python
   data = "武沛齐|root|wupeiqi@qq.com"
   result = data.split('|') # ["武沛齐","root","wupeiqi@qq.com"]
   print(data) # "武沛齐|root|wupeiqi@qq.com"
   print(result) # 输出 ["武沛齐","root","wupeiqi@qq.com"] 根据特定字符切开之后保存在列表中，方便以后的操作
   ```

   ```python
   # 案例：判断用户名密码是否正确
   info = "武沛齐,root"   # 备注：字符串中存储了用户名和密码
   user_list = info.split(',')    # 得到一个包含了2个元素的列表 [ "武沛齐" , "root" ]
   
   # user_list[0]
   # user_list[1]
   
   user = input("请输入用户名：")
   pwd = input("请输入密码：")
   
   if user == user_list[0] and pwd == user_list[1]:
   	print("登录成功")
   else:
   	print("用户名或密码错误")
   ```

   扩展，可以指定按此符号切几次

   ```python
   data = "武沛齐|root|wupeiqi@qq.com"
   v1 = data.split("|")   # ['武沛齐', 'root', 'wupeiqi@qq.com']
   print(v1)
   
   v2 = data.split("|", 1) # ['武沛齐', 'root|wupeiqi@qq.com']
   print(v2)
   ```

   再扩展，可以从右侧开始切

   ```python
   data = "武沛齐,root,wupeiqi@qq.com"
   
   v1 = data.rsplit(',')
   print(v1) # ['武沛齐', 'root', 'wupeiqi@qq.com']
   
   v2 = data.rsplit(',',1)
   print(v2) # ['武沛齐,root', 'wupeiqi@qq.com']
   ```

   应用场景：

   ```python
   file_path = "xxx/xxxx/xx.xx/xxx.mp4"
   
   data_list = file_path.rsplit(".",1) # ["xxx/xxxx/xx.xx/xxx","mp4"]
   data_list[0]
   data_list[1]
   ```

9. 字符串拼接，得到一个新的字符串

   ```python
   data_list = ["alex","是","大烧饼"]
   v1 = "_".join(data_list) # alex_是_大烧饼
   print(v1)
   #将列表的每项通过给定的符号“_”拼接起来
   ```

10. 格式化字符串，得到新的字符串

    ```python
    name = "{0}的喜欢干很多行业，例如有：{1}、{2} 等"
    data = name.format("老王","护士","嫩模")
    print(data) # 老王的喜欢干很多行业，例如有：护士、嫩模 等
    print(name) # "{0}的喜欢干很多行业，例如有：{1}、{2} 等"
    ```

    ```python
    name = "{}的喜欢干很多行业，例如有：{}、{} 等"
    data = name.format("老王","护士","嫩模")
    print(data) # 老王的喜欢干很多行业，例如有：护士、嫩模 等
    ```

    ```python
    name = "{name}的喜欢干很多行业，例如有：{h1}、{h2} 等"
    data = name.format(name="老王",h1="护士",h2="嫩模")
    print(data) # 老王的喜欢干很多行业，例如有：护士、嫩模 等
    ```

11. 字符串转换为字节类型

    ```python
    data = "嫂子"  # unicode，字符串类型
    #encode()编码
    v1 = data.encode("utf-8")  # utf-8，字节类型
    v2 = data.encode("gbk")  # gbk，字节类型
    
    print(v1)  # b'\xe5\xab\x82 \xe5\xad\x90'
    print(v2)  # b'\xc9\xa9 \xd7\xd3'
    #decode()解码
    s1 = v1.decode("utf-8") # 嫂子
    s2 = v2.decode("gbk") # 嫂子
    print(s1)
    print(s2)
    ```

12. 将字符串内容居中、居左、居右展示

    ```python
    v1 = "王老汉"
    # data = v1.center(21, "-")
    # print(data) #---------王老汉---------
    
    # data = v1.ljust(21, "-")
    # print(data) # 王老汉------------------
    
    # data = v1.rjust(21, "-")
    # print(data) # ------------------王老汉
    ```

13. 帮助你填充0

    ```python
    data = "alex"
    v1 = data.zfill(10)
    print(v1) # 000000alex
    ```

    ```python
    # 应用场景：处理二进制数据
    data = "101" # "00000101"
    v1 = data.zfill(8)
    print(v1) # "00000101"
    ```

### 3.3 公共功能

1. 相加：字符串 + 字符串

   ```python
   v1 = "alex" + "大sb"
   print(v1)
   ```

2. 相乘：字符串 * 整数

   ```python
   data = "嫂子" * 3
   print(data) # 嫂子嫂子嫂子
   ```

3. 长度

   ```python
   data = "嫂子满身大汉"
   value = len(data) 
   print(value) # 6
   ```

4. 获取字符串中的字符，索引

   ```python
   message = "来做点py交易呀"
   #          0 1 2345 6 7
   #           ... -3 -2 -1
   print(message[0]) # "来"
   print(message[1]) # "做"
   print(message[2]) # "点"
   
   print(message[-1]) # 呀
   print(message[-2]) # 易
   print(message[-3]) # 交
   ```

   注意：字符串中是能通过索引取值，无法修改值。【字符串在内部存储时不允许对内部元素修改，想修改只能重新创建。】

   ```python
   message = "来做点py交易呀"
   index = 0
   while index < len(message):
   	value = message[index]
       print(value)
       index += 1
   ```

   ```python
   message = "来做点py交易呀"
   index = len(message) - 1
   while index >=0:
       value = message[index]
       print(value)
       index -= 1
   ```

5. 获取字符串中的子序列，切片

   ```python
   message = "来做点py交易呀"
   
   print(message[0:2]) # "来做"
   print(message[3:7]) # "py交易"
   print( message[3:] ) # "py交易呀"
   print( message[:5] ) # "来做点py"
   
   print(message[4:-1]) # "y交易"
   print(message[4:-2]) # "y交"
   
   print( message[4:len(message)] ) # "y交易呀"
   ```

   注意：字符串中的切片只能读取数据，无法修改数据。【字符串在内部存储时不允许对内部元素修改，想要修改只能重新创建】

   ```python
   message = "来做点py交易呀"
   
   value = message[:3] + "Python" + message[5:]
   print(value)
   ```

6. 步长，跳着去字符串的内容

   ```python
   name = "生活不是电影，生活比电影苦"
   
   print( name[ 0:5:2 ] )   # 输出：生不电 【前两个值表示区间范围，最有一个值表示步长】
   print( name[ :8:2 ] )    # 输出：生不电，  【区间范围的前面不写则表示起始范围为0开始】
   print( name[ 2::3 ] )    # 输出：不影活影 【区间范围的后面不写则表示结束范围为最后】
   print( name[ ::2 ] )     # 输出：生不电，活电苦 【区间范围不写表示整个字符串】
   print( name[ 8:1:-1 ] )  # 输出：活生，影电是不 【倒序】
   ```

   ```python
   name = "生活不是电影，生活比电影苦"
   
   print(name[8:1:-1])  # 输出：活生，影电是不 【倒序】
   print(name[-1:1:-1])  # 输出：苦影电比活生，影电是不 【倒序】
   
   # 面试题：给你一个字符串，请将这个字符串翻转。
   value = name[-1::-1]
   print(value)  # 苦影电比活生，影电是不活生
   ```

7. 循环

   - while循环

     ```python
     message = "来做点py交易呀"
     index = 0
     while index < len(message):
     	value = message[index]
         print(value)
         index += 1
     ```

   - for循环

     ```python
     message = "来做点py交易呀"
     for char in message:
         print(char)
     ```

   - range，帮助我们创建一系列的数字

     ```python
     range(10) # [0,1,2,3,4,5,6,7,8,9]
     range(1,10) # [1,2,3,4,5,6,7,8,9]
     range(1,10,2) # [1,3,5,7,9]
     range(10,1,-1) # [10,9,8,7,6,5,4,3,2] #前取后不取
     ```

   - For + range

     ```python
     for i in range(10):
         print(i)
     ```

     ```python
     message = "来做点py交易呀"
     
     for i in range(5): # [0,1,2,3,4]
         print(message[i])
     ```

     ```python
     message = "来做点py交易呀"
     for i in range( len(message) ): # [0,1,2,3,4,5,6,7]
         print(message[i])
     ```

   一般应用场景：

   - while，一般在做无限制（未知）循环此处时使用。

     ```python
     while True:
         ...
     ```

     ```python
     # 用户输入一个值，如果不是整数则一直输入，直到是整数了才结束。
     num = 0
     while True:
         data = input("请输入内容:")
         if data.isdecimal():
             num = int(data)
             break
     	else:
             print("输入错误，请重新输入！")
     ```

   - for循环，一般应用在已知的循环数量的场景。

     ```python
     message = "来做点py交易呀"
     for char in message:
         print(char)
     ```

     ```python
     for i in range(30):
         print(message[i])
     ```


   - break和continue关键字

     ```python
     message = "来做点py交易呀"
     for char in message:
         if char == "p":
             continue
         print(char)
     
     # 输出：
     来
     做
     点
     y
     交
     易
     呀
     ```

     ```python
     message = "来做点py交易呀"
     for char in message:
         if char == "p":
             break
         print(char)
     
     # 输出：
     来
     做
     点
     ```

     ```python
     for i in range(5):
         print(i)# 0 1 2 3 4
         for j in range(3):
             break
             print(j) # 0 1 2  # 0 1 2  # 0 1 2  # 0 1 2  # 0 1 2  
     ```

     



### 3.4 转换

```python
num = 999
data = str(num)
print(data) # "999"
```

```python
data_list = ["alex","eric",999]
data = str(data_list)
print(data) # '["alex","eric",999]'
```

一般情况下，只有整型转字符串才有意义。



### 3.5 其他

#### 3.5.1 字符串不可被修改

```python
name = "武沛齐"

name[1]
name[1:2]
```

```python
num_list = [11,22,33]

num_list[0]
num_list[0] = 666
```



## 4.列表（list）

列表（list），是一个**有序**且**可变**的容器，在里面可以存放**多个不同类型**的元素。

### 4.1 定义

```python
user_list =  ["苍老师","有坂深雪","大桥未久"]
number_list = [98,88,666,12,-1]
data_list = [1,True,"Alex","宝强","贾乃亮"]
```

```python
user_list = []
user_list.append("铁锤")
user_list.append(123)
user_list.append(True)
print(user_list) # ["铁锤",123,True]
```

不可变类型：字符串、布尔、整型（已最小，内部数据无法进行修改）

可变类型：列表（内部数据元素可以修改）



### 4.2 独有功能

Python中为所有的列表类型的数据提供了一批独有的功能。

在开始学习列表的独有功能之前，先来做一个字符串和列表的对比：

- 字符串，不可变，即：创建好之后内部就无法修改。【独有功能都是新创建一份数据】

  ```python
  name = "alex"
  data = name.upper()
  print(name)
  print(data)
  ```

- 列表，可变，即：创建好之后内部元素可以修改。【独有功能基本上都是直接操作列表内部，不会创建新的一份数据】

  ```python
  user_list = ["车子","妹子"]
  user_list.append("嫂子")
  
  print(user_list) # ["车子","妹子","嫂子"]
  ```

列表中的常见独有功能如下：

1. 追加，在原列表中尾部追加值。

   ```python
   data_list = []
   
   v1 = input("请输入姓名")
   data_list.append(v1)
   
   v2 = input("请输入姓名")
   data_list.append(v2)
   
   print(data_list) # ["alex","eric"]
   ```

   ```python
   # 案例1
   user_list = []
   
   while True:
       user = input("请输入用户名(Q退出)：")
       if user == "Q":
           break
       user_list.append(user)
       
   print(user_list) 
   ```

   ```python
   # 案例2
   welcome = "欢迎使用NB游戏".center(30, '*')
   print(welcome)
   
   user_count = 0
   while True:
       count = input("请输入游戏人数：")
       if count.isdecimal():
           user_count = int(count)
           break
       else:
           print("输入格式错误，人数必须是数字。")
   
   
   message = "{}人参加游戏NB游戏。".format(user_count)
   print(message)
   
   
   user_name_list = []
   
   for i in range(1, user_count + 1):
       tips = "请输入玩家姓名（{}/{}）：".format(i, user_count)
       name = input(tips)
       user_name_list.append(name)
   
   print(user_name_list)
   ```

2. 批量追加，将一个列表中的元素逐一添加另外一个列表。

   ```python
   tools = ["搬砖","菜刀","榔头"]
   tools.extend( [11,22,33] ) # weapon中的值逐一追加到tools中
   print(tools) # ["搬砖","菜刀","榔头",11,22,33]
   ```

   ```python
   tools = ["搬砖","菜刀","榔头"]
   weapon = ["AK47","M6"]
   #tools.extend(weapon) # weapon中的值逐一追加到tools中
   #print(tools) # ["搬砖","菜刀","榔头","AK47","M6"]
   
   weapon.extend(tools)
   print(tools) # ["搬砖","菜刀","榔头"]
   print(weapon) # ["AK47","M6","搬砖","菜刀","榔头"]
   ```

   ```python
   # 等价于(扩展)
   weapon = ["AK47","M6"]
   for item in weapon:
       print(item)
   
   # 输出：
   #  AK47
   #  M6
   tools = ["搬砖","菜刀","榔头"]
   weapon = ["AK47","M6"]
   for item in weapon:
       tools.append(item)  
   print(tools) # ["搬砖","菜刀","榔头","AK47","M6"]
   ```

3. 插入，在原列表的指定索引位置插入值

   ```python
   user_list = ["苍老师","有坂深雪","大桥未久"]
   user_list.insert(0,"马蓉")
   user_list.insert(2,"李小璐")
   print(user_list)
   ```

   ```python
   # 案例
   name_list = []
   while True:
       name = input("请输入购买火车票用户姓名（Q/q退出）：")
       if name.upper() == "Q":
           break
       if name.startswith("刁"):
           name_list.insert(0, name)
       else:
           name_list.append(name)
   print(name_list)
   ```

4. 在原列表中根据值删除（从左到右找到第一个删除）【慎用，里面没有会报错】

   ```python
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   user_list.remove("Alex")
   print(user_list)
   
   
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   if "Alex" in user_list:
   	user_list.remove("Alex")
   print(user_list)
   
   
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   while True:
       if "Alex" in user_list:
           user_list.remove("Alex")
   	else:
           break
   print(user_list)
   ```

   ```python
   # 案例：自动抽奖程序
   import random
   
   data_list = ["iphone12", "二手充气女友", "大保健一次", "泰国5日游", "避孕套"]
   
   while data_list:
       name = input("自动抽奖程序，请输入自己的姓名：")
   
       # 随机从data_list抽取一个值出来
       value = random.choice(data_list) # "二手充气女友"
       print( "恭喜{}，抽中{}.".format(name, value) )
       
       data_list.remove(value) # "二手充气女友"
   ```

5. 在原列表中根据索引踢出某个元素（根据索引位置删除）

   ```python
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   #               0       1      2      3       4
   user_list.pop(1)
   print(user_list) #  ["王宝强","Alex","贾乃亮","Alex"]
   
   user_list.pop()
   print(user_list) # ["王宝强","Alex","贾乃亮"]
   
   item = user_list.pop(1)
   print(item) # "Alex"
   print(user_list) # ["王宝强","贾乃亮"]
   ```

   ```python
   # 案例：排队买火车票
   
   # ["alex","李杰","eric","武沛齐","老妖","肝胆"]
   user_queue = []
   
   while True:
       name = input("北京~上海火车票，购买请输入姓名排队(Q退出)：")
       if name == "Q":
           break
       user_queue.append(name)
   
   ticket_count = 3
   for i in range(ticket_count):
       username = user_queue.pop(0)
       message = "恭喜{},购买火车票成功。".format(username)
       print(message)
   
   # user_queue = ["武沛齐","老妖","肝胆"]
   faild_user = "、".join(user_queue) # "武沛齐、老妖、肝胆"
   faild_message = "非常抱歉，票已售完，以下几位用户请选择其他出行方式，名单：{}。".format(faild_user)
   print(faild_message)
   ```

6. 清空原列表

   ```python
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   user_list.clear()
   print(user_list) # []
   ```

7. 根据值获取索引（从左到右找到第一个删除）【慎用，找不到报错】

   ```python
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   #               0       1      2       3      4
   if "Alex" in user_list:
   	index = user_list.index("Alex")
   	print(index) # 2
   else:
       print("不存在")
   ```

8. 列表元素排序

   ```python
   # 数字排序
   num_list = [11, 22, 4, 5, 11, 99, 88]
   print(num_list)
   num_list.sort()  # 让num_list从小到大排序
   num_list.sort(reverse=True)  # # 让num_list从大到小排序
   print(num_list)
   
   
   # 字符串排序
   user_list = ["王宝强", "Ab陈羽凡", "Alex", "贾乃亮", "贾乃", "1"]
   #       [29579, 23453, 24378]
   #       [65, 98, 38472, 32701, 20961]
   #       [65, 108, 101, 120]
   #       [49]
   print(user_list)
   """
   sort的排序原理
       [ "x x x" ," x x x x x " ]
   """
   user_list.sort()
   print(user_list)
   ```

   注意：排序时内部元素无法进行比较时，程序会报错（尽量数据类型统一）。

9. 反转原列表

   ```python
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   user_list.reverse()
   
   print(user_list)
   ```

### 4.3 公共功能

1. 相加，两个列表相加获取生成一个新的列表。

   ```python
   data = ["赵四","刘能"] + ["宋晓峰","范德彪"]
   print(data) # ["赵四","刘能","宋晓峰","范德彪"]
   
   v1 = ["赵四","刘能"]
   v2 = ["宋晓峰","范德彪"]
   v3 = v1 + v2
   print(v3) # ["赵四","刘能","宋晓峰","范德彪"]
   ```

2. 相乘，列表*整型 将列表中的元素再创建N份并生成一个新的列表。

   ```python
   data = ["赵四","刘能"] * 2
   print(data) # ["赵四","刘能","赵四","刘能"]
   
   v1 = ["赵四","刘能"]
   v2 = v1 * 2
   print(v1) # ["赵四","刘能"]
   print(v2) # ["赵四","刘能","赵四","刘能"]
   ```

3. 运算符in包含
   由于列表内部是由多个元素组成，可以通过in来判断元素是否在列表中。

   ```python
   user_list = ["狗子","二蛋","沙雕","alex"] 
   result = "alex" in user_list
   # result = "alex" not in user_list
   print(result) #  True
   
   if "alex" in user_list:
       print("在，把他删除")
       user_list.remove("alex")
   else:
       print("不在")
   ```

   ```python
   user_list = ["狗子","二蛋","沙雕","alex"] 
   if "alex" in user_list:
       print("在，把他删除")
       user_list.remove("alex")
   else:
       print("不在")
   
   text = "打倒小日本"
   data = "日" in text
   ```

   ```python
   # 案例
   user_list = ["狗子","二蛋","沙雕","alex"] 
   if "alex" in user_list:
       print("在，把他删除")
       user_list.remove("alex")
   else:
       print("不在")
   ```

   ```python
   # 案例user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]if "Alex" in user_list:	index = user_list.index("Alex")	user_list.pop(index)
   ```

   ```python
   # 案例：敏感词替换
   text = input("请输入文本内容：") # 按时打发第三方科技爱普生豆腐啊；了深刻的房价破阿偶打飞机
   forbidden_list = ["草","欧美","日韩"]
   for item in forbidden_list:
       text = text.replace(item,"**")
   print(text)
   ```

   注意：**列表检查元素是否存在时，是采用逐一比较的方式，效率会比较低。**

4. 获取长度

   ```python
   user_list = ["范德彪","刘华强",'尼古拉斯赵四']
   print( len(user_list) )
   ```

5. 索引，一个元素的操作

   ```python
   # 读
   user_list = ["范德彪","刘华强",'尼古拉斯赵四']
   print( user_list[0] )
   print( user_list[2] )
   print( user_list[3] ) # 报错
   ```

   ```python
   # 改
   user_list = ["范德彪","刘华强",'尼古拉斯赵四']
   user_list[0] = "武沛齐"
   print(user_list) # ["武沛齐","刘华强",'尼古拉斯赵四']
   ```

   ```python
   # 删
   user_list = ["范德彪","刘华强",'尼古拉斯赵四']
   del user_list[1]
   
   user_list.remove("刘华强")
   ele = user_list.pop(1)
   ```

   注意：超出索引范围会报错。
   提示：由于字符串是不可变类型，所以他只有索引读的功能，而列表可以进行 读、改、删

6. 切片，多个元素的操作（很少用）

   ```python
   # 读
   user_list = ["范德彪","刘华强",'尼古拉斯赵四']
   
   print( user_list[0:2] ) # ["范德彪","刘华强"]
   print( user_list[1:] )
   print( user_list[:-1] )
   ```

   ```python
   # 改
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   user_list[0:2] = [11, 22, 33, 44]
   print(user_list) # 输出 [11, 22, 33, 44, '尼古拉斯赵四']
   
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   user_list[2:] = [11, 22, 33, 44]
   print(user_list) # 输出 ['范德彪', '刘华强', 11, 22, 33, 44]
   
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   user_list[3:] = [11, 22, 33, 44]
   print(user_list) # 输出 ['范德彪', '刘华强', '尼古拉斯赵四', 11, 22, 33, 44]
   
   
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   user_list[10000:] = [11, 22, 33, 44]
   print(user_list) # 输出 ['范德彪', '刘华强', '尼古拉斯赵四', 11, 22, 33, 44]
   
   
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   user_list[-10000:1] = [11, 22, 33, 44]
   print(user_list) # 输出 [11, 22, 33, 44, '刘华强', '尼古拉斯赵四']
   ```

   ```python
   # 删
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   del user_list[1:]
   print(user_list) # 输出 ['范德彪']
   ```

7. 步长

   ```python
   user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   #              0        1        2          3       4
   print( user_list[1:4:2] )
   print( user_list[0::2] )
   print( user_list[1::2] )
   print( user_list[4:1:-1] )
   ```

   ```python
   # 案例：实现列表的翻转
   user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   new_data = user_list[::-1]
   print(new_data)
   
   
   data_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   data_list.reverse()
   print(data_list)
   
   # 给你一个字符串请实现字符串的翻转？
   name = "武沛齐"
   name[::-1]
   ```

8. for循环

   ```python
   user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   for item in user_list:
   	print(item)
   ```

   ```python
   user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   
   for index in range( len(user_list) ):
       item = user_index[index]
       print(item)
   ```

   切记，循环的过程中对数据进行删除会踩坑【面试题】。

   ```python
   # 错误方式， 有坑，结果不是你想要的。拿的数据不对，删了之后，后边的数据会前移
   
   user_list = ["刘的话", "范德彪", "刘华强", '刘尼古拉斯赵四', "宋小宝", "刘能"]
   for item in user_list:
       if item.startswith("刘"):
           user_list.remove(item)
           
   print(user_list)
   
   
   ```

   ```python
   # 正确方式，倒着删除。
   user_list = ["刘的话", "范德彪", "刘华强", '刘尼古拉斯赵四', "宋小宝", "刘能"]
   for index in range(len(user_list) - 1, -1, -1):
       item = user_list[index]
       if item.startswith("刘"):
           user_list.remove(item)
   print(user_list)
   ```

### 4.4 转换

- int、bool无法转换成列表

- str

  ```python
  name = "武沛齐"
  
  data = list(name)  # ["武","沛","齐"]
  print(data)
  ```

- 超前

  ```python
  v1 = (11,22,33,44) # 元组
  vv1 = list(v1)     # 列表 [11,22,33,44]
  
  v2 = {"alex","eric","dsb"} # 集合
  vv2 = list(v2) # 列表 ["alex","eric","dsb"]
  ```

  

### 4.5. 其他

#### 4.5.1 嵌套

列表属于容器，内部可以存放各种数据，所以他也支持列表的嵌套，如：

```python
data = [ "谢广坤",["海燕","赵本山"],True,[11,22,[999,123],33,44],"宋小宝" ]
```

对于嵌套的值，可以根据之前学习的索引知识点来进行学习，例如：

```python
data = [ "谢广坤",["海燕","赵本山"],True,[11,22,33,44],"宋小宝" ]

print( data[0] ) # "谢广坤"
print( data[1] ) # ["海燕","赵本山"]
print( data[0][2] ) # "坤"
print( data[1][-1] ) # "赵本山"

data.append(666)
print(data) # [ "谢广坤",["海燕","赵本山"],True,[11,22,33,44],"宋小宝",666]

data[1].append("谢大脚")
print(data) # [ "谢广坤",["海燕","赵本山","谢大脚"],True,[11,22,33,44],"宋小宝",666 ]


del data[-2]
print(data) # [ "谢广坤",["海燕","赵本山","谢大脚"],True,[11,22,33,44],666 ]


data[-2][1] = "alex"
print(data) # [ "谢广坤",["海燕","赵本山","谢大脚"],True,[11,"alex",33,44],666 ]


data[1][0:2] = [999,666]
print(data) # [ "谢广坤",[999,666,"谢大脚"],True,[11,"alex",33,44],666 ]
```

```python
# 创建用户列表
#    用户列表应该长： [ ["alex","123"],["eric","666"] ]

# user_list = [["alex","123"],["eric","666"],]
# user_list.append(["alex","123"])
# user_list.append(["eric","666"])


user_list = []
while True:
    user = input("请输入用户名：")
    pwd = input("请输入密码：")

    data = []
    data.append(user)
    data.append(pwd)
    
    user_list.append(data)
```

```python
user_list = []
while True:
    user = input("请输入用户名(Q退出)：")
    if user == "Q":
        break
    pwd = input("请输入密码：")
    data = [user,pwd]
    user_list.append(data)

print(user_list)
```



## 5.元组

列表（list），是一个**有序**且**可变**的容器，在里面可以存放**多个不同类型**的元素。

元组（tuple），是一个**有序**且**不可变**的容器，在里面可以存放**多个不同类型**的元素。

> 如何体现不可变呢？
> 记住一句话：《"我儿子永远不能换成是别人，但我儿子可以长大"》

### 5.1 定义

```python
v1 = (11,22,33)
v2 = ("李杰","Alex")
v3 = (True,123,"Alex",[11,22,33,44])

# 建议：在元组的最后多加一个逗v3 = ("李杰","Alex",)
```

```python
d1 = (1)  # 1
d2 = (1,) # (1,)

d3 = (1,2)
d4 = (1,2)
```

注意：建议在元组的最后多加一个逗号，用于标识他是一个元组。

```python
# 面试题
1. 比较值 v1 = (1) 和 v2 = 1 和 v3 = (1,) 有什么区别？
2. 比较值 v1 = ( (1),(2),(3) ) 和 v2 = ( (1,) , (2,) , (3,),) 有什么区别？
              (1,2,3)
```

### 5.2 独有功能

无

### 5.3 公共功能

1. 相加，两个列表相加获取生成一个新的列表。

   ```python
   data = ("赵四","刘能") + ("宋晓峰","范德彪")
   print(data) # ("赵四","刘能","宋晓峰","范德彪")
   
   v1 = ("赵四","刘能")
   v2 = ("宋晓峰","范德彪")
   v3 = v1 + v2
   print(v3) # ("赵四","刘能","宋晓峰","范德彪")
   ```

2. 相乘，列表*整型 将列表中的元素再创建N份并生成一个新的列表。

   ```python
   data = ("赵四","刘能") * 2
   print(data) # ("赵四","刘能","赵四","刘能")
   
   v1 = ("赵四","刘能")
   v2 = v1 * 2
   print(v1) # ("赵四","刘能")
   print(v2) # ("赵四","刘能","赵四","刘能")
   ```

3. 获取长度

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',)
   print( len(user_list) )
   ```

4. 索引

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',)
   print( user_list[0] )
   print( user_list[2] )
   print( user_list[3] )#报错
   ```

5. 切片

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',)
   print( user_list[0:2] )
   print( user_list[1:] )
   print( user_list[:-1] )
   ```

6. 步长

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能")
   print( user_list[1:4:2] )
   print( user_list[0::2] )
   print( user_list[1::2] )
   print( user_list[4:1:-1] )
   ```

   ```python
   # 字符串 & 元组。
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能")
   data = user_list[::-1]#只能生成新的元组
   
   # 列表
   user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   data = user_list[::-1]
   
   user_list.reverse()
   print(user_list)
   ```

7. for循环

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能")
   for item in user_list:
   	print(item)
   ```

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能")
   for item in user_list:
    if item == '刘华强':
   	 continue
    print(name)
   ```

   目前：只有 str、list、tuple 可以被for循环。 "xxx"  [11,22,33]  (111,22,33)

   ```python
   # len + range + for + 索引
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能")
   for index in range(len(user_list)):
       item = user_list[index]
       print(item)
   ```

   



### 5.4 转换

其他类型转换为元组，使用`tuple(其他类型)`，目前只有字符串和列表可以转换为元组。

```python
data = tuple(其他)

# str / list 
```

```python
name = "武沛齐"
data = tuple(name)
print(data) # 输出 ("武","沛","齐")
```

```python
name = ["武沛齐",18,"pythonav"]
data = tuple(name)
print(data) # 输出 ("武沛齐",18,"pythonav")
```



### 5.5 其他

#### 5.5.1 嵌套

由于元组和列表都可以充当`容器`，他们内部可以放很多元素，并且也支持元素内的各种嵌套。

```python
tu = ( '今天姐姐不在家', '姐夫和小姨子在客厅聊天', ('姐夫问小姨子税后多少钱','小姨子低声说道说和姐夫还提钱') )
tu1 = tu[0]
tu2 = tu[1]
tu3 = tu[2][0]
tu4 = tu[2][1]
tu5 = tu[2][1][3]

print(tu1) # 今天姐姐不在家
print(tu2) # 姐夫和小姨子在客厅聊天
print(tu3) # 姐夫问小姨子税后多少钱
print(tu4) # 小姨子低声说道说和姐夫还提钱
```



## 6.集合（set）

集合是一个 无序 、可变、不允许数据重复的容器。

### 6.1 定义

```python
v1 = { 11, 22, 33, "alex" }
```

- 无序，无法通过索引取值。

- 可变，可以添加和删除元素。

  ```python
  v1 = {11,22,33,44}
  v1.add(55)
  print(v1) # {11,22,33,44,55}
  ```

- 不允许数据重复。

  ```python
  v1 = {11,22,33,44}
  v1.add(22)
  print(v1) # {11,22,33,44}
  ```

一般什么时候用集合呢？

> 就是想要维护一大堆不重复的数据时，就可以用它。比如：做爬虫去网上找图片的链接，为了避免链接重复，可以选择用集合去存储链接地址。



**注意**：定义空集合时，只能使用`v = set()`，不能使用 `v={}`（这样是定义一个空字典）。

```python
v1 = []
v11 = list()

v2 = ()
v22 = tuple()

v3 = set()

v4 = {} # 空字典
v44 = dict()
```



### 6.2 独有功能

1. 添加元素

   ```python
   data = {"刘嘉玲", '关之琳', "王祖贤"}
   data.add("郑裕玲")
   print(data)
   ```

   ```python
   data = set()
   data.add("周杰伦")
   data.add("林俊杰")
   print(data)
   ```

2. 删除元素

   ```python
   data = {"刘嘉玲", '关之琳', "王祖贤","张曼⽟", "李若彤"}
   data.discard("关之琳") 
   print(data)
   ```

3. 交集

   ```python
   s1 = {"刘能", "赵四", "⽪⻓⼭"}
   s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
   
   s4 = s1.intersection(s2) # 取两个集合的交集 
   print(s4) # {"⽪⻓⼭"}
   
   s3 = s1 & s2   			  # 取两个集合的交集
   print(s3)
   ```

4. 并集

   ```python
   s1 = {"刘能", "赵四", "⽪⻓⼭"}
   s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
   s4 = s1.union(s2) 		# 取两个集合的并集  {"刘能", "赵四", "⽪⻓⼭","刘科⻓", "冯乡⻓", }
   print(s4)
   s3 = s1 | s2   			# 取两个集合的并集
   print(s3)
   ```

5. 差集

   ```python
   s1 = {"刘能", "赵四", "⽪⻓⼭"}
   s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
   s4 = s1.difference(s2) 		# 差集，s1中有且s2中没有的值 {"刘能", "赵四"}
   s6 = s2.difference(s1)   	# 差集，s2中有且s1中没有的值 {"刘科⻓", "冯乡⻓"}
   
   s3 = s1 - s2   			   # 差集，s1中有且s2中没有的值
   s5 = s2 - s1   			   # 差集，s2中有且s1中没有的值
   
   print(s5,s6)
   ```



### 6.3 公共功能

1. 减，计算差集

   ```python
   s1 = {"刘能", "赵四", "⽪⻓⼭"}
   s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
   
   s3 = s1 - s2 
   s4 = s2 - s1
   print(s3)
   print(s4)
   ```

2. &，计算交集

   ```python
   s1 = {"刘能", "赵四", "⽪⻓⼭"}
   s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
   s3 = s1 & s2
   print(s3)
   ```

3. |，计算并集

   ```python
   s1 = {"刘能", "赵四", "⽪⻓⼭"}
   s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
   s3 = s1 | s2
   print(s3)
   ```

4. 长度

   ```python
   v = {"刘能", "赵四", "尼古拉斯"}
   data = len(v)
   print(data)
   ```

5. for循环

   ```python
   v = {"刘能", "赵四", "尼古拉斯"}
   for item in v:
   	print(item)
   ```

### 6.4 转换

其他类型如果想要转换为集合类型，可以通过set进行转换，并且如果数据有重复自动剔除。

提示：int/list/tuple/dict都可以转换为集合。

```python
v1 = "武沛齐"
v2 = set(v1)
print(v2) # {"武","沛","齐"}
```

```python
v1 = [11,22,33,11,3,99,22]
v2 = set(v1)
print(v2) # {11,22,33,3,99}
```

```python
v1 = (11,22,3,11)
v2 = set(v1)
print(v2) # {11,22,3}
```

提示：这其实也是去重的一个手段。

```python
data = {11,22,33,3,99}

v1 = list(data) # [11,22,33,3,99]

v2 = tuple(data) # (11,22,33,3,99)
```



### 6.5 其他

#### 6.5.1 集合的存储原理

<img src="day05数据类型.assets/image-20201120193837492.png" alt="image-20201120193837492" style="zoom:50%;" />

#### 6.5.2 元素必须可哈希

因存储原理，集合的元素必须是可哈希的值，即：内部通过通过哈希函数把值转换成一个数字。

<img src="day05数据类型.assets/image-20201120190454120.png" alt="image-20201120190454120" style="zoom: 25%;" />

目前可哈希的数据类型：int、bool、str、tuple，而list、set是不可哈希的。

总结：集合的元素只能是 int、bool、str、tuple 。

- 转换成功

  ```python
  v1 = [11,22,33,11,3,99,22]
  v2 = set(v1)
  print(v2) # {11,22,33,3,99}
  ```

- 转换失败

  ```python
  v1 = [11,22,["alex","eric"],33]
  v2 = set(v1) # 报错 
  print(v2) 
  ```



#### 6.5.3 查找速度特别快

因存储原理特殊，集合的查找效率非常高（数据量大了才明显）。

- 低

  ```python
  user_list = ["武沛齐","alex","李璐"]
  if "alex" in user_list:
      print("在")
  else:
      print("不在")
      
      
  user_tuple = ("武沛齐","alex","李璐")
  if "alex" in user_tuple:
      print("在")
  else:
      print("不在")
  ```

- 效率高

  ```python
  user_set = {"武沛齐","alex","李璐"}
  if "alex" in user_set:
      print("在")
  else:
      print("不在")
  ```

  

#### 6.5.4 对比和嵌套

| 类型  | 是否可变 | 是否有序 | 元素要求 | 是否可哈希 | 转换        | 定义空            |
| ----- | -------- | -------- | -------- | ---------- | ----------- | ----------------- |
| list  | 是       | 是       | 无       | 否         | list(其他)  | `v=[]或v=list()`  |
| tuple | 否       | 是       | 无       | 是         | tuple(其他) | `v=()或v=tuple()` |
| set   | 是       | 否       | 可哈希   | 否         | set(其他)   | `v=set()`         |

```python
data_list = [
    "alex",
    11,
    (11, 22, 33, {"alex", "eric"}, 22),
    [11, 22, 33, 22],
    {11, 22, (True, ["中国", "北京"], "沙河"), 33}
]
```

注意：由于True和False本质上存储的是 1 和 0 ，而集合又不允许重复，所以在整数 0、1和False、True出现在集合中会有如下现象：

```python
v1 = {True, 1}
print(v1)  # {True}

v2 = {1, True}
print(v2)  # {1}

v3 = {0, False}
print(v3)  # {0}

v4 = {False, 0}
print(v4)  # {False}
```

