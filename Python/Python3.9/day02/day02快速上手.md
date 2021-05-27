# 快速上手

## 1.编码初体验

- 编码保存打开必须要保持一致，否则会乱码。

- 默认Python解释器是以UTF-8编码的形式打开文件。如果想要修改Python的默认解释器编码，

  ```python
  	# -*- coding:gbk -*-
  
  	print("我是seirin")
  ```

- 建议：所有Python代码文件的都要以UTF-8编码保存和读取。



## 2.输出

将结果或内容想要呈现给用户。

```python
print("                                                            * *  ")
print("                                                         * * * *  ")
print("                                                      * * * * * *  ")
print("                                                   * * * * * * * *  ")
print("                                                * * * * * * * * * *  ")
print("                                             * * * * * * * * * * * *  ")
print("                                              * * * * * * * * * * * *  ")
print("                                               * * * * * * * * * * * *  ")
print("                                      * *       * * * * * * * * * * * *  ")
print("                                   * * * *       * * * * * * * * * * * *  ")
print("                                * * * * * *       * * * * * * * * * * * *  ")
print("                             * * * * * * * *       * * * * * * * * * * * *  ")
print("                          * * * * * * * * * *       * * * * * * * * * * * *  ")
print("                       * * * * * * * * * * * *       * * * * * * * * * * * *  ")
print("                        * * * * * * * * * * * *       * * * * * * * * * * * *  ")
print("                         * * * * * * * * * * * *       * * * * * * * * * * * *  ")
print("                * *       * * * * * * * * * * * *       * * * * * * * * * * * *  ")
print("             * * * *       * * * * * * * * * * * *       * * * * * * * * * * * *  ")
print("          * * * * * *       * * * * * * * * * * * *       * * * * * * * * * * * *  ")
print("       * * * * * * * *       * * * * * * * * * * * *       * * * * * * * * * * * *  ")
print("    * * * * * * * * * *       * * * * * * * * * * * *       * * * * * * * * * * * *  ")
print(" * * * * * * * * * * * *       * * * * * * * * * * * *       * * * * * * * * * * * *  ")
print("  * * * * * * * * * * * *       * * * * * * * * * * * *       * * * * * * * * * * * *  ")
print("   * * * * * * * * * * * *       * * * * * * * * * * * *       * * * * * * * * * * * *  ")
```

关于输出：

- 默认print在尾部会加换行符

```Python
print("看着风景美如画")
print("本想吟诗赠天下")

输出：
看着风景美如画
本想吟诗增天下
```

- 想要不换行

```python
print("看着风景美如画",end="")
print("本想吟诗赠天下",end="")

输出：
看着风景美如画本想吟诗增天下
```

```python 
print("看着风景美如画",end=",")
print("本想吟诗赠天下",end=".")

输出：
看着风景美如画,本想吟诗增天下.
```



## 3.初识数据类型

### 3.1整型（int）

```python
print(666)

print(2 + 10)

print(2 * 10)

print(10 / 2)

print(10 % 3)

print(2 ** 4)

```

> 注：这个 * * 的意思是次方，2 * * 4 是2的4次方。

### 3.2字符串（str）

字符串有一个特点，他必须由引号引起来，如：

单行字符串

```python
print("我是seirin")
print('我是seirin')
print('我是"seirin')
```

多行字符串

```python
print("""这里
可以
放
多行""")
print('''这里
可以放多行''')
```



对于字符串：

- 加，两个字符串可以通过加号拼接起来。

  ```python
  print( "seirin" + "在学习Python" )
  ```

- 乘，让整形和字符串进行相乘，以实现让字符串重复出现N次并拼接起来。

  ```python
  print(3 * "我好饿！")
  ```



### 3.3布尔类型（bool）

布尔类型中共有两个值：True / False

```python
print(1 > 2)
print(False)

print(1 == 1)
print(True)
```

```python
name = input("请输入你的用户名:")

if name == "seirin":
    print("用户登录成功")
else:
    print("用户登录失败")
```



补充：

```python
1 > 2 
1 == 3
"aaa" == "bbb"
1 == "aaa"

1 > "aaa"  是无法进行比较大小
```



### 3.4 类型转换

上文数据类型int/str/bool有了初步了解，他们都有自己不同的定义方式。

- int，整型定义时，必须是数字且无引号，例如：5、8、9
- str，字符串定义时，必须用双引号括起来，例如：”中国”、
- bool，布尔值定义时，只能写True和False

不同的数据类型都有不同的功能，例如：整型可以加减乘除 而 字符串只能加(拼接)和乘法。
如果想要做转换可遵循一个基本规则：想转换什么类型就让他包裹一些。

例如：str(666) = "666"是将整型转换为字符串、int(“888”)是将字符串转 888。



转换为整形：

```python
# 字符串转换为整形（度可度之人）
  int("666")
  int("999")
  "6" + "9" 的结果应该是： "69"
  int("6") + int("9") 的结果是：15

  int("alex是sb") 报错
  
# 布尔类型转换为整形
  int(True)  转换完等于 1
  int(False) 转换完等于 0
```



转换为字符串

```python
# 整形转字符串
str(345)
str(666) + str(9) 结果为："6669"

# 布尔类型转换为字符串
str(True)  "True"
str(False) "False"
```



转换为布尔类型

```python
# 整形转布尔
bool(1) True
bool(2) True
bool(0) False
bool(-10) True

# 字符串转布尔
bool("aaa") True
bool("啊啊啊") True
bool("") False
bool(" ") True
```



三句话搞定类型转换：

- 其他所有类型转换为布尔类型时，除了 空字符串、0以为其他都是True。

- 字符串转整形时，只有那种 "988" 格式的字符串才可以转换为整形，其他都报错。

- 想要转换为那种类型，就用这类型的英文包裹一下就行。 

  ```
  str(...)
  int(...)
  bool(...)
  ```

  

## 4.变量

变量，其实就是我们生活中起别名和外号，让变量名指向某个值，格式为： 【变量名 = 值】，以后可以通过变量名来操作其对应的值。

```python
name = "啊啊啊啊"
print(name) # 啊啊啊啊
```

```python
age = 18
name = "a"
flag = 1 > 18
address = "北京" + "沙河"
addr = "北京" + "沙河" + name   # "北京沙河a"

print(addr)
print(flag)
```

```python
age = 18
number = 1 == 2
```

注意：

- 给变量赋值 `age = 18`
- 让age代指值 `age = 18`



### 4.1 变量名的规范

```python
age = 18
name = "alex"
flag = 1 > 18
address = "北京昌平" + "沙河"
```

三个规范（只要有一条就会报错）：

- 变量名只能由 字母、数字、下划线 组成。

- 不能以数字开头

  ```
  na9me9 = "alex"
  ```

- 不能用Python内置的关键字

  ```
  def = "alex"
  break = 123
  ```

  *[‘and’, ‘as’, ‘assert’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘exec’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘not’, ‘or’, ‘pass’, ‘print’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]*

两个建议：

- 下划线连接命名（小写）

  ```
  father_name = "爸爸"
  brother_age = 19
  ```

- 见名知意

  ```
  age = 18
  color = "red"
  current_user_name = "比利"
  ```

### 4.2 变量内存指向关系

通过学习上述变量知识让我们对变量了有了初步认识，接下来我们就要从稍稍高级一些的角度来学习变量，即：内存指向（在电脑的内存中是怎么存储的）。

**情景一**

```python
name = "wupeiqi"
```

在计算机的内存中创建一块区域保存字符串”wupeiqi”，name变量名则指向这块区域。

<img src="day02快速上手.assets/image-20201011163312491.png" alt="image-20201011163312491" style="zoom:50%;" />

**情景二**

```python
name = "wupeiqi"
name = "alex"
```

在计算机的内存中创建一块区域保存字符串”wupeiqi”，name变量名则指向这块区域。然后又再内存中创建了一块域保存字符串”alex”，name变量名则指向”alex”所在的区域，不再指向”wupeiqi”所在区域（无人指向的数据会被标记为垃圾，由解释器自动化回收）

<img src="day02快速上手.assets/image-20201011163344305.png" alt="image-20201011163344305" style="zoom:50%;" />



**情景三**

```python
name = "wupeiqi"
new_name = name
```

在计算机的内存中创建一块区域保存字符串”wupeiqi”，name变量名则指向这块区域。new_name变量名指向name变量，因为被指向的是变量名，所以自动会转指向到name变量代表的内存区域。

<img src="day02快速上手.assets/image-20201011163427166.png" alt="image-20201011163427166" style="zoom:50%;" />

**情景四**

```python
name = "wupeiqi"
new_name = name
name = "alex"
```

在计算机的内存中创建一块区域保存字符串”wupeiqi”，name变量名则指向这块区域(灰色线)， 然后new_name指向name所指向的内存区域，最后又创建了一块区域存放”alex”，让name变量指向”alex”所在区域.

<img src="day02快速上手.assets/image-20201011163503412.png" alt="image-20201011163503412" style="zoom:50%;" />



**情景五**

```python
num = 18
age = str(num)
```

在计算机的内存中创建一块区域保存整型18，name变量名则指向这块区域。通过类型转换依据整型18再在内存中创建一个字符串”18”, age变量指向保存这个字符串的内存区域。

<img src="day02快速上手.assets/image-20201011163528779.png" alt="image-20201011163528779" style="zoom:50%;" />



## 5. 注释

写代码时候，如果想要对某写内容进行注释处理，即：解释器忽略不会按照代码去运行。

- 单行注释

  ```python
  # 声明一个name变量
  name = "alex"
  
  age = 19 # 这表示当前用户的年龄
  
  注意：快捷点 control + ?
  ```

- 多行注释

  ```python
  # 声明一个name变量
  # 声明一个name变量
  # 声明一个name变量
  name = "alex"
  
  
  """
  多行注释内容
  多行注释内容
  多行注释内容
  """
  age = 19
  ```

  

## 6. 输入

输入，可以实现程序和用户之间的交互。

```python
# 1. 右边 input("请输入用户名：") 是让用户输入内容。
# 2. 将用户输入的内容赋值给name变量。
name = input("请输入用户名：")

if name == "seirin":
  print("登录成功")
else:
  print("登录失败")
```

```python
data = input(">>>")
print(data)
```

**特别注意**：用户输入的任何内容本质上都是字符串。

1. 提示输入姓名，然后给姓名后面拼接一个“烧饼”，提示输入姓名，然后给姓名后面拼接一个“烧饼”，最终打印结果。

   ```python
   name = input("请输入用户名：")
   text = name + "烧饼"
   print(text)
   ```

2. 提示输入 姓名/位置/行为，然后做拼接并打印：xx 在 xx 做 xx 。

   ```python
   name = input("请输入用户名：")
   address = input("请输入位置：")
   action = input("请输入行为：")
   
   text = name + "在" + address + action
   print(text)
   ```

3. 提示输入两个数字，计算两个数的和。

   ```python
   number1 = input("请输入一个数字：") # "1"
   number2 = input("请输入一个数字：") # "2"
   
   value = int(number1) + int(number2)
   print(value)
   ```

   

## 7.条件语句

```python
if 条件 :
    条件成立之后的代码...
    条件成立之后的代码...
    条件成立之后的代码...
else:
    条件不成立之后执行的代码...
    条件不成立之后执行的代码...
    条件不成立之后执行的代码...
```

```python
name = input("请输入用户名:")
if name == "alex":
  print("sb")
else:
  print("db")
```

提醒：统一缩进问题（都是使用四个空格 = tab）。

```python
#以下会报错
name = input("请输入用户名:")
if name == "alex":
    print("sb")
   print("sb")
else:
    print("db")
```

### 7.1基本条件语句

- 示例1

  ```python
  print("开始")
  if True:
    print("123")
  else:
    print("456")
  print("结束")
  
  # 输出结果
  开始
  123
  结束
  ```

- 示例2

  ```python
  print("开始")
  if 5==5:
    print("123")
  else:
    print("456")
  print("结束")
  # 输出结果
  开始
  123
  结束
  ```

- 示例3

  ```python
  num = 19
  if num > 10:
  	print("num变量对应值大于10")
  else:
  	print("num变量对应值不大于10")
  # 输出结果
  num变量对应值大于10
  ```

- 示例4

  ```python
  username = "wupeiqi"
  password = "666"
  if username == "wupeiqi" and password == "666":
  	print("恭喜你，登录成功")
  else:
  	print("登录失败")
  # 输出结果
  恭喜你，登录成功
  ```

- 示例5

  ```python
  username = "wupeiqi"
  
  if username == "wupeiqi" or username == "alex":
  	print("VIP大会员用户")
  else:
  	print("普通用户")
  # 输出结果
  VIP大会员用户
  ```

- 示例6

  ```python
  number = 19
  if number%2 == 1:
  	print("number是奇数")
  else:
  	print("number是偶数")
  # 输出结果
  number是奇数
  ```

  ```python
  number = 19
  data = number%2 == 1
  if data:
  	print("number是奇数")
  else:
  	print("number是偶数")
  # 输出结果
  number是奇数
  ```

- 示例7

  ```python
  if 条件:
    成立
  ```

  ```python
  print("开始")
  if 5 == 5:
    print("5等于5")
  print("结束")
  ```

  ### 7.2多条件判断

  ```python
  if 条件A:
    A成立，执行此缩进中的所有代码
    ...
  elif 条件B:
    B成立，执行此缩进中的所有代码
    ...
  elif 条件C:
    C成立，执行此缩进中的所有代码
    ...
  else:
    上述ABC都不成立。
  ```

  ```python
  num = input("请输入数字")
  data = int(num)
  if data>6:
    print("太大了")
  elif data == 6:
    print("刚刚好")
  else:
    print("太小了")
  ```

  ```python
  score = input("请输入分数")
  data = int(score)
  
  if data > 90:
    print("优")
  elif data > 80:
    print("良")
  elif data > 70:
    print("中")
  elif data > 60:
    print("差")
  else:
    print("不及格")
  ```

  

  ### 7.3 条件嵌套

  ```python
  if 条件A:
    ...
  elif 条件B:
    ...
  ```

  ```python
  if 条件A:
      if 条件A1:
          ...
      else：
     	    ...
  elif 条件B:
      ...
  ```

  模拟10086客服

  ```python
  print("欢迎致电10086，我们提供了如下服务： 1.话费相关；2.业务办理；3.人工服务")
  
  choice = input("请选择服务序号")
  
  if choice == "1":
      print("话费相关业务")
      cost = input("查询话费请按1;交话费请按2")
      if cost == "1":
          print("查询话费余额为100")
      elif cost == "2":
          print("交互费")
      else:
          print("输入错误")
  elif choice == "2":
      print("业务办理")
  elif choice == "3":
      print("人工服务")
  else:
      print("序号输入错误")
  ```

  

