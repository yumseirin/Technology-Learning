# shell编程

## 1.shell编程概述

### 1.1shell名词解释

- Kernel
  - Linux内核主要是为了和硬件打交道

- shell

  - 命令解释器（command interpreter）
  - Shell是一个用C语言编写的程序，它是用户使用Linux的桥梁。Shell既是一种命令语言，又是一种程序设计语言。
  - Shell是指一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务。

- shell两大主流：

  - sh：
    - Bourne shell (sh) ,Solaris,hpux默认shell
    - Bourne again shell (bash) ,Linux系统默认shell
  - csh
    - C shell (csh)
    - tc shell (tcsh)

- #!声明

  - 告诉系统其后路径所指定的程序既是解释此脚本文件的Shell程序

  - ```shell
    #! /bin/bash
    echo "Hello World!"
    ```

### 1.2执行Shell的方式

- 输入脚本的绝对路径或相对路径
  - /root/helloworld.sh
  - ./helloworld/sh
  - 执行的必须是一个可执行文件
- bash或sh+脚本
  - sh helloworld.sh
  - 当脚本没有x权限时，root和文件所有者

通过该方式可以正常执行

- 在脚本的路径前再加"."或source
  - source helloworld.sh
- 区别
  - 第一种和第二种会新开一个bash，不同bash中的变量无法共享
  - 第三种是在同一个shell里面执行的
- export：可以将当前进程的变量传递给子进程去使用
  - 将来配置profile的时候，所有的变量前必须加export

## 2.shell基础入门

### 2.1shell变量

- 定义变量时，变量名不加美元符号

  - 命名只能使用英文字母、数字和下划线，首个字符不能以数字开头。
  - 中间不能有空格，可以使用下划线（_）。
  - 不能使用标点符号。
  - 不能使用bash里的关键字。（可以用help命令查看保留关键字）

- 变量的类型

  - 局部变量
    - 局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量。
  - 环境变量
    - 所有程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。
  - shell变量
    - shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量

- ```shell
  #变量的声明
  name="zhangsan"
  for file in `ls /etc`
  或
  for file in $(ls /etc)
  
  #变量的调用
  echo $name
  echo ${name}
  
  for skill in Ada Coffe Action Java; do
  	echo "I am good at ${skill}Script"
  done
  
  #只读变量 /bin/sh:NAME: This variable is read only.
  url="https://www.google.com"
  readonly url
  url="https://www.runoob.com"
  
  #删除变量
  unset name
  ```

### 2.2shell的字符串

- 字符串是shell编程中最常用最有用的数据类型，字母串可以用单引号，也可以用双引号，也可以不用引号。

- 单引号

  - 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
  - 单引号字符串中不能单独一个的引号，但可成对出现，作为字符串拼接使用。

- 双引号

  - 双引号里可以有变量

  - 双引号里可以出现转义字符

  - ```shell
    #声明字符串
    str1="hello world 1"
    str2="hello world 2"
    
    #字符串拼接--双引号
    name='helloworld'
    name1="hello,"$name" !"
    name2="hello,${name} !"
    
    #字符串拼接--单引号
    passwd='123456'
    passwd1='hello,'$passwd' !'
    passwd2='hello,${passwd} !'
    echo $passwd2 #hello,${passwd} !
    
    #字符串的长度
    email=“123456@qq.com”
    echo ${#email}
    echo ${email:1:4} #输出位置1到4的字符，2345
    ```

### 2.3shell数组

- bash支持一维数组（不支持多维数组），并且没有限定数组的大小

- 数组元素的下标由0开始编号。获取数组中的元素要利用下标，下标可以是整数或算数表达式，其值应大于或等于0.

- ```shell
  #定义数组 括号来表示数组，数组元素用空格符号分隔开
  数组名=(值1 值2 ... 值n)
  favs=("足球" "篮球" "乒乓球" "保龄球")
  
  #读取数组 ${数组名[下标]}
  fav=${favs[1]}
  
  #使用@符号可以获取数组中的所有元素
  echo ${favs[@]}
  
  #获取数组的长度
  length=${#favs[@]}
  length=${#favs[*]}
  ```

### 2.4shell的注释

- 以#开头的行就是注释，会被解释器忽略。

- 通过每一行加一个#号设置多行注释

- ```shell
  #----------------------------
  # 这是一个注释
  # author:
  # site:
  #----------------------------
  ####  服务器配置-start  ####
  #
  #
  #
  #
  ####  服务器配置-end ####
  
  
  # 特殊的多行注释
  
  :<<EOF
  注释内容...
  注释内容...
  注释内容...
  EOF
  
  :<<!
  注释内容...
  注释内容...
  注释内容...
  !
  ```

### 2.5shell参数传递

- 执行shell脚本时，向脚本传递参数，脚本内获取参数的格式为：$n   （n代表一个数字）

- | 参数处理 | 参数说明                                                     |
  | -------- | ------------------------------------------------------------ |
  | $#       | 传递到脚本的参数个数                                         |
  | $*       | 以一个单字符显示所有向脚本传递的参数。                       |
  | $$       | 脚本运行的当前进程ID号                                       |
  | $!       | 后台运行的最后一个进程的ID号                                 |
  | $?       | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。 |
  | $0       | 执行的文件名                                                 |

- ```shell
  #! /bin/bash
  
  echo "shell 传递参数实例！";
  echo "执行的文件名：$0";
  echo "第一个参数为：$1";
  echo "第二个参数为：$2";
  echo "第三个参数为：$3";
  
  # ./hello.sh 11 22 33 44
  ```

## 3.shell高级进阶

### 3.1shell运算符

- 运算符的分类

  - 算数运算符

  - | 运算符 | 说明                                          | 举例                          |
    | :----- | :-------------------------------------------- | :---------------------------- |
    | +      | 加法                                          | `expr $a + $b` 结果为 30。    |
    | -      | 减法                                          | `expr $a - $b` 结果为 -10。   |
    | *      | 乘法                                          | `expr $a \* $b` 结果为  200。 |
    | /      | 除法                                          | `expr $b / $a` 结果为 2。     |
    | %      | 取余                                          | `expr $b % $a` 结果为 0。     |
    | =      | 赋值                                          | a=$b 将把变量 b 的值赋给 a。  |
    | ==     | 相等。用于比较两个数字，相同则返回 true。     | [ $a == $b ] 返回 false。     |
    | !=     | 不相等。用于比较两个数字，不相同则返回 true。 | [ $a != $b ] 返回 true。      |

    **注意：**条件表达式要放在方括号之间，并且要有空格，例如: **[$a==$b]** 是错误的，必须写成 **[ $a == $b ]**。

  - 关系运算符

  - | 运算符 | 说明                                                  | 举例                       |
    | :----- | :---------------------------------------------------- | :------------------------- |
    | -eq    | 检测两个数是否相等，相等返回 true。                   | [ $a -eq $b ] 返回 false。 |
    | -ne    | 检测两个数是否不相等，不相等返回 true。               | [ $a -ne $b ] 返回 true。  |
    | -gt    | 检测左边的数是否大于右边的，如果是，则返回 true。     | [ $a -gt $b ] 返回 false。 |
    | -lt    | 检测左边的数是否小于右边的，如果是，则返回 true。     | [ $a -lt $b ] 返回 true。  |
    | -ge    | 检测左边的数是否大于等于右边的，如果是，则返回 true。 | [ $a -ge $b ] 返回 false。 |
    | -le    | 检测左边的数是否小于等于右边的，如果是，则返回 true。 | [ $a -le $b ] 返回 true。  |

    关系运算符只支持数字，不支持字符串，除非字符串的值是数字。

  - 布尔运算符

  - | 运算符 | 说明                                                | 举例                                     |
    | :----- | :-------------------------------------------------- | :--------------------------------------- |
    | !      | 非运算，表达式为 true 则返回 false，否则返回 true。 | [ ! false ] 返回 true。                  |
    | -o     | 或运算，有一个表达式为 true 则返回 true。           | [ $a -lt 20 -o $b -gt 100 ] 返回 true。  |
    | -a     | 与运算，两个表达式都为 true 才返回 true。           | [ $a -lt 20 -a $b -gt 100 ] 返回 false。 |

  - 逻辑运算符

  - | 运算符 | 说明       | 举例                                       |
    | :----- | :--------- | :----------------------------------------- |
    | &&     | 逻辑的 AND | [[ $a -lt 100 && $b -gt 100 ]] 返回 false  |
    | \|\|   | 逻辑的 OR  | [[ $a -lt 100 \|\| $b -gt 100 ]] 返回 true |

  - 字符串运算符

  - | 运算符 | 说明                                         | 举例                     |
    | :----- | :------------------------------------------- | :----------------------- |
    | =      | 检测两个字符串是否相等，相等返回 true。      | [ $a = $b ] 返回 false。 |
    | !=     | 检测两个字符串是否不相等，不相等返回 true。  | [ $a != $b ] 返回 true。 |
    | -z     | 检测字符串长度是否为0，为0返回 true。        | [ -z $a ] 返回 false。   |
    | -n     | 检测字符串长度是否不为 0，不为 0 返回 true。 | [ -n "$a" ] 返回 true。  |
    | $      | 检测字符串是否为空，不为空返回 true。        | [ $a ] 返回 true。       |

  - 文件测试运算符：用于检测 Unix 文件的各种属性。

  - | 操作符  | 说明                                                         | 举例                      |
    | :------ | :----------------------------------------------------------- | :------------------------ |
    | -b file | 检测文件是否是块设备文件，如果是，则返回 true。              | [ -b $file ] 返回 false。 |
    | -c file | 检测文件是否是字符设备文件，如果是，则返回 true。            | [ -c $file ] 返回 false。 |
    | -d file | 检测文件是否是目录，如果是，则返回 true。                    | [ -d $file ] 返回 false。 |
    | -f file | 检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 | [ -f $file ] 返回 true。  |
    | -g file | 检测文件是否设置了 SGID 位，如果是，则返回 true。            | [ -g $file ] 返回 false。 |
    | -k file | 检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。  | [ -k $file ] 返回 false。 |
    | -p file | 检测文件是否是有名管道，如果是，则返回 true。                | [ -p $file ] 返回 false。 |
    | -u file | 检测文件是否设置了 SUID 位，如果是，则返回 true。            | [ -u $file ] 返回 false。 |
    | -r file | 检测文件是否可读，如果是，则返回 true。                      | [ -r $file ] 返回 true。  |
    | -w file | 检测文件是否可写，如果是，则返回 true。                      | [ -w $file ] 返回 true。  |
    | -x file | 检测文件是否可执行，如果是，则返回 true。                    | [ -x $file ] 返回 true。  |
    | -s file | 检测文件是否为空（文件大小是否大于0），不为空返回 true。     | [ -s $file ] 返回 true。  |
    | -e file | 检测文件（包括目录）是否存在，如果是，则返回 true。          | [ -e $file ] 返回 true。  |

    其他检查符：

    - **-S**: 判断某文件是否 socket。
    - **-L**: 检测文件是否存在并且是一个符号链接。

#### 3.1.1算数运算符

- expr是一款表达式计算工具，使用它能完成表达式求值操作。

- ```shell
  #!/bin/bash
  a=10
  b=20
  
  val=`expr $a + $b`
  echo "a + b : $val"
  
  val=`expr $a - $b`
  echo "a - b : $val"
  
  val=`expr $a \* $b`
  echo "a * b : $val"
  
  val=`expr $b / $a`
  echo "b / a : $val"
  
  val=`expr $b % $a`
  echo "b % a : $val"
  
  if [ $a == $b ]
  then
     echo "a 等于 b"
  fi
  if [ $a != $b ]
  then
     echo "a 不等于 b"
  fi
  ```

- ```sh
  a + b : 30
  a - b : -10
  a * b : 200
  b / a : 2
  b % a : 0
  a 不等于 b
  ```

#### 3.1.2关系运算符

- 关系运算符只支持数字，不支持字符串，除非字符串的值是数字。

- ```shell
  #!/bin/bash
  
  a=10
  b=20
  
  if [ $a -eq $b ]
  then
     echo "$a -eq $b : a 等于 b"
  else
     echo "$a -eq $b: a 不等于 b"
  fi
  if [ $a -ne $b ]
  then
     echo "$a -ne $b: a 不等于 b"
  else
     echo "$a -ne $b : a 等于 b"
  fi
  if [ $a -gt $b ]
  then
     echo "$a -gt $b: a 大于 b"
  else
     echo "$a -gt $b: a 不大于 b"
  fi
  if [ $a -lt $b ]
  then
     echo "$a -lt $b: a 小于 b"
  else
     echo "$a -lt $b: a 不小于 b"
  fi
  if [ $a -ge $b ]
  then
     echo "$a -ge $b: a 大于或等于 b"
  else
     echo "$a -ge $b: a 小于 b"
  fi
  if [ $a -le $b ]
  then
     echo "$a -le $b: a 小于或等于 b"
  else
     echo "$a -le $b: a 大于 b"
  fi
  ```

- ```sh
  10 -eq 20: a 不等于 b
  10 -ne 20: a 不等于 b
  10 -gt 20: a 不大于 b
  10 -lt 20: a 小于 b
  10 -ge 20: a 小于 b
  10 -le 20: a 小于或等于 b
  ```

#### 3.1.3布尔运算符

- ```shell
  #!/bin/bash
  a=10
  b=20
  
  if [ $a != $b ]
  then
     echo "$a != $b : a 不等于 b"
  else
     echo "$a == $b: a 等于 b"
  fi
  if [ $a -lt 100 -a $b -gt 15 ]
  then
     echo "$a 小于 100 且 $b 大于 15 : 返回 true"
  else
     echo "$a 小于 100 且 $b 大于 15 : 返回 false"
  fi
  if [ $a -lt 100 -o $b -gt 100 ]
  then
     echo "$a 小于 100 或 $b 大于 100 : 返回 true"
  else
     echo "$a 小于 100 或 $b 大于 100 : 返回 false"
  fi
  if [ $a -lt 5 -o $b -gt 100 ]
  then
     echo "$a 小于 5 或 $b 大于 100 : 返回 true"
  else
     echo "$a 小于 5 或 $b 大于 100 : 返回 false"
  fi
  ```

- ```sh
  10 != 20 : a 不等于 b
  10 小于 100 且 20 大于 15 : 返回 true
  10 小于 100 或 20 大于 100 : 返回 true
  10 小于 5 或 20 大于 100 : 返回 false
  ```

#### 3.1.4逻辑运算符

- ```shell
  #!/bin/bash
  a=10
  b=20
  
  if [[ $a -lt 100 && $b -gt 100 ]]
  then
     echo "返回 true"
  else
     echo "返回 false"
  fi
  
  if [[ $a -lt 100 || $b -gt 100 ]]
  then
     echo "返回 true"
  else
     echo "返回 false"
  fi
  ```

- ```sh
  返回 false
  返回 true
  ```

#### 3.1.5字符串运算符

- ```shell
  #!/bin/bash
  a="abc"
  b="efg"
  
  if [ $a = $b ]
  then
     echo "$a = $b : a 等于 b"
  else
     echo "$a = $b: a 不等于 b"
  fi
  if [ $a != $b ]
  then
     echo "$a != $b : a 不等于 b"
  else
     echo "$a != $b: a 等于 b"
  fi
  if [ -z $a ]
  then
     echo "-z $a : 字符串长度为 0"
  else
     echo "-z $a : 字符串长度不为 0"
  fi
  if [ -n "$a" ]
  then
     echo "-n $a : 字符串长度不为 0"
  else
     echo "-n $a : 字符串长度为 0"
  fi
  if [ $a ]
  then
     echo "$a : 字符串不为空"
  else
     echo "$a : 字符串为空"
  fi
  ```

- ```sh
  abc = efg: a 不等于 b
  abc != efg : a 不等于 b
  -z abc : 字符串长度不为 0
  -n abc : 字符串长度不为 0
  abc : 字符串不为空
  ```

#### 3.1.6文件测试运算符

- ```shell
  #!/bin/bash
  #变量 file 表示文件 /var/www/runoob/test.sh，它的大小为 100 字节，具有 rwx 权限。
  
  file="/var/www/runoob/test.sh"
  if [ -r $file ]
  then
     echo "文件可读"
  else
     echo "文件不可读"
  fi
  if [ -w $file ]
  then
     echo "文件可写"
  else
     echo "文件不可写"
  fi
  if [ -x $file ]
  then
     echo "文件可执行"
  else
     echo "文件不可执行"
  fi
  if [ -f $file ]
  then
     echo "文件为普通文件"
  else
     echo "文件为特殊文件"
  fi
  if [ -d $file ]
  then
     echo "文件是个目录"
  else
     echo "文件不是个目录"
  fi
  if [ -s $file ]
  then
     echo "文件不为空"
  else
     echo "文件为空"
  fi
  if [ -e $file ]
  then
     echo "文件存在"
  else
     echo "文件不存在"
  fi
  ```

- ```sh
  文件可读
  文件可写
  文件可执行
  文件为普通文件
  文件不是个目录
  文件不为空
  文件存在
  ```

### 3.2echo打印数据

- shell的echo指令与PHP的echo指令类似，都是用于字符串的输出。

- ```shell
  ## 显示普通字符串
  echo "Hello World"
  
  ## 显示转义字符
  echo "\"Hello World\""
  
  ## 显示变量
  name="zhangsan"
  echo "$name Hello World"
  
  ## 显示换行
  echo -e "OK! \n"
  echo "Hello World"
  
  ## 显示不换行
  echo -e "OK! \c"
  echo "Hello World"
  
  ## 显示结果定向至文件
  echo "Hello World" > myfile
  
  ## 原样输出字符串
  echo '$name\"'
  
  ## 显示命令执行结果
  echo `date`
  ```

### 3.3test命令

- Shell中的 test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。

- 数值测试

  - | 参数 | 说明           |
    | :--- | :------------- |
    | -eq  | 等于则为真     |
    | -ne  | 不等于则为真   |
    | -gt  | 大于则为真     |
    | -ge  | 大于等于则为真 |
    | -lt  | 小于则为真     |
    | -le  | 小于等于则为真 |

- 字符串测试

  - | 参数      | 说明                     |
    | :-------- | :----------------------- |
    | =         | 等于则为真               |
    | !=        | 不相等则为真             |
    | -z 字符串 | 字符串的长度为零则为真   |
    | -n 字符串 | 字符串的长度不为零则为真 |

- 文件测试

  - | 参数      | 说明                                 |
    | :-------- | :----------------------------------- |
    | -e 文件名 | 如果文件存在则为真                   |
    | -r 文件名 | 如果文件存在且可读则为真             |
    | -w 文件名 | 如果文件存在且可写则为真             |
    | -x 文件名 | 如果文件存在且可执行则为真           |
    | -s 文件名 | 如果文件存在且至少有一个字符则为真   |
    | -d 文件名 | 如果文件存在且为目录则为真           |
    | -f 文件名 | 如果文件存在且为普通文件则为真       |
    | -c 文件名 | 如果文件存在且为字符型特殊文件则为真 |
    | -b 文件名 | 如果文件存在且为块特殊文件则为真     |

- ```shell
  num1=100
  num2=100
  if test $[num1] -eq $[num2]
  then
      echo '两个数相等！'
  else
      echo '两个数不相等！'
  fi
  ```

### 3.4shell流程控制

#### 3.4.1 if

- if

  - ```shell
    if condition
    then
      command1 
      command2
      ...
      commandN 
    fi
    ```

- if else

  - ```shell
    if condition
    then
      command1 
      command2
      ...
      commandN
    else
      command
    fi
    ```
  
- if else-if else
  - ```shell
    if condition1
    then
      command1
    elif condition2 
    then 
      command2
    else
      commandN
    fi
    ```

- 实例

  - ```shell
    a=10
    b=20
    if [ $a == $b ]
    then
       echo "a 等于 b"
    elif [ $a -gt $b ]
    then
       echo "a 大于 b"
    elif [ $a -lt $b ]
    then
       echo "a 小于 b"
    else
       echo "没有符合的条件"
    fi
    ```

  - ```sh
    a 小于 b
    ```

#### 3.4.2 case ... esac

- **case ... esac** 为多选择语句，是一种多分枝选择结构，每个 case 分支用右圆括号开始，用两个分号 **;;** 表示 break，即执行结束，跳出整个 case ... esac 语句，esac（就是 case 反过来）作为结束标记

- 可以用 case 语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令。

- 语法格式：

  - ```shell
    case 值 in
    模式1)
        command1
        command2
        ...
        commandN
        ;;
    模式2）
        command1
        command2
        ...
        commandN
        ;;
    esac
    ```

- 实例

  - ```shell
    echo '输入 1 到 4 之间的数字:'
    echo '你输入的数字为:'
    read aNum
    case $aNum in
        1)  echo '你选择了 1'
        ;;
        2)  echo '你选择了 2'
        ;;
        3)  echo '你选择了 3'
        ;;
        4)  echo '你选择了 4'
        ;;
        *)  echo '你没有输入 1 到 4 之间的数字'
        ;;
    esac
    ```

  - ```sh
    输入 1 到 4 之间的数字:
    你输入的数字为:
    3
    你选择了 3
    ```

#### 3.4.3 for

- 当变量值在列表里，for 循环即执行一次所有命令，使用变量名获取列表中的当前取值。

- 命令可为任何有效的 shell 命令和语句。in 列表可以包含替换、字符串和文件名。

- in列表是可选的，如果不用它，for循环使用命令行的位置参数

- 格式：

  - ```shell
    for var in item1 item2 ... itemN
    do
        command1
        command2
        ...
        commandN
    done
    
    #写成一行
    for var in item1 item2 ... itemN; do command1; command2… done;
    ```

- 实例

  - ```shell
    for loop in 1 2 3 4 5
    do
        echo "The value is: $loop"
    done
    
    for str in This is a string
    do
        echo $str
    done
    ```

  - ```sh
    The value is: 1
    The value is: 2
    The value is: 3
    The value is: 4
    The value is: 5
    
    This
    is
    a
    string
    ```

#### 3.4.4 while循环

- while 循环用于不断执行一系列命令，也用于从输入文件中读取数据。命令通常为测试条件。

- ```shell
  while condition
  do
      command
  done
  ```

- ```shell
  #  Bash let 命令，它用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量
  #!/bin/bash
  int=1
  while(( $int<=5 ))
  do
      echo $int
      let "int++"
  done
  ```

- 无限循环

  - ```shell
    while :
    do
        command
    done
    
    #或者
    
    while true
    do
        command
    done
    
    #或者
    
    for (( ; ; ))
    ```

#### 3.4.5 until循环

- until 循环执行一系列命令直至条件为 true 时停止。

- until 循环与 while 循环在处理方式上刚好相反。

- ```shell
  until condition
  do
      command
  done
  ```

- condition 一般为条件表达式，如果返回值为 false，则继续执行循环体内的语句，否则跳出循环。

#### 3.4.6 break

- break命令允许跳出所有循环（终止执行后面的所有循环）。

- ```shell
  #!/bin/bash
  while :
  do
      echo -n "输入 1 到 5 之间的数字:"
      read aNum
      case $aNum in
          1|2|3|4|5) echo "你输入的数字为 $aNum!"
          ;;
          *) echo "你输入的数字不是 1 到 5 之间的! 游戏结束"
              break
          ;;
      esac
  done
  ```

- ```sh
  输入 1 到 5 之间的数字:3
  你输入的数字为 3!
  输入 1 到 5 之间的数字:7
  你输入的数字不是 1 到 5 之间的! 游戏结束
  ```

#### 3.4.7 continue

- continue命令不会跳出所有循环，仅仅跳出当前循环。

- ```shell
  #!/bin/bash
  while :
  do
      echo -n "输入 1 到 5 之间的数字: "
      read aNum
      case $aNum in
          1|2|3|4|5) echo "你输入的数字为 $aNum!"
          ;;
          *) echo "你输入的数字不是 1 到 5 之间的!"
              continue
              echo "游戏结束"
          ;;
      esac
  done
  ```

- 当输入大于5的数字时，该例中的循环不会结束，语句 **echo "游戏结束"** 永远不会被执行。

### 3.5 shell函数

- linux shell 可以用户定义函数，然后在shell脚本中可以随便调用。

- 可以带function fun() 定义，也可以直接fun() 定义,不带任何参数。

- 参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255)

- 格式如下：

  - ```shell
    [ function ] funname [()]
    
    {
    
        action;
    
        [return int;]
    
    }
    ```

- 实例

  - ```shell
    #!/bin/bash
    
    ## 第一个函数-------------------
    demoFun(){
        echo "这是我的第一个 shell 函数!"
    }
    echo "-----函数开始执行-----"
    demoFun
    echo "-----函数执行完毕-----"
    
    ## 函数返回值-----------------
    funWithReturn(){
        echo "这个函数会对输入的两个数字进行相加运算..."
        echo "输入第一个数字: "
        read aNum
        echo "输入第二个数字: "
        read anotherNum
        echo "两个数字分别为 $aNum 和 $anotherNum !"
        return $(($aNum+$anotherNum))
    }
    funWithReturn
    # 函数返回值在调用该函数后通过 $? 来获得
    echo "输入的两个数字之和为 $? !"
    
    ## 函数参数----------------------
    #在Shell中，调用函数时可以向其传递参数。在函数体内部，通过 $n 的形式来获取参数的值
    funWithParam(){
        echo "第一个参数为 $1 !"
        echo "第二个参数为 $2 !"
        echo "第十个参数为 $10 !"
        echo "第十个参数为 ${10} !"
        echo "第十一个参数为 ${11} !"
        echo "参数总数有 $# 个!"
        echo "作为一个字符串输出所有参数 $* !"
    }
    funWithParam 1 2 3 4 5 6 7 8 9 34 73
    ```

  - ```sh
    ## 第一个函数-------------------
    -----函数开始执行-----
    这是我的第一个 shell 函数!
    -----函数执行完毕-----
    
    ## 函数返回值-----------------
    这个函数会对输入的两个数字进行相加运算...
    输入第一个数字: 
    1
    输入第二个数字: 
    2
    两个数字分别为 1 和 2 !
    输入的两个数字之和为 3 !
    
    ## 函数参数----------------------
    第一个参数为 1 !
    第二个参数为 2 !
    第十个参数为 10 ! #这里其实是$1得到的第一个参数加字符0
    第十个参数为 34 !
    第十一个参数为 73 !
    参数总数有 11 个!
    作为一个字符串输出所有参数 1 2 3 4 5 6 7 8 9 34 73 !
    
    ```

- 注意，$10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数。

- 还有几个特殊字符处理参数：

  - | 参数处理 | 说明                                                         |
    | :------- | :----------------------------------------------------------- |
    | $#       | 传递到脚本或函数的参数个数                                   |
    | $*       | 以一个单字符串显示所有向脚本传递的参数                       |
    | $$       | 脚本运行的当前进程ID号                                       |
    | $!       | 后台运行的最后一个进程的ID号                                 |
    | $@       | 与$*相同，但是使用时加引号，并在引号中返回每个参数。         |
    | $-       | 显示Shell使用的当前选项，与set命令功能相同。                 |
    | $?       | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。 |
