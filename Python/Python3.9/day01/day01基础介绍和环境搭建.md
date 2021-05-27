# 基础介绍和环境搭建

## 1.Python的介绍

### 1.1 Python火爆的原因

- 语法简洁，适合学习。相较于其他语言Python的学习成本非常低。
- 类库强大。
- 开发效率高。

### 1.2 Python的解释器种类

- CPython【主流】，底层是由C语言开发的解释器。
- JPython，由Java语言开发出来的解释器，方便让Python和Java代码做集成。
- IronPython，是由C#语言开发出来的解释器。
- RubyPython
- PyPy，是对CPython的优化，它执行的效率提高了。引入了编译器的功能，本质上将Python的代码进行了编译，再去执行编译后的代码。 
- ...

> 注意：常说的Python解释器就是CPython解释器。

### 1.3 CPython解释器

CPython解释器主要有两大版本：

- 2.x，目前最新的Python2.7.18。（2020年后不再维护）

- 3.x，目前学习的为3.9。



## 2.环境搭建

- Python解释器，将程序员编写的Python代码翻译成计算机能够识别的指令。

### 2.1 安装Python解释器

- Python官网下载Python解释器

  > https://www.python.org/

- 在电脑上安装

- 编写一个Python代码并交给Python解释器去运行

  ```python
  	# coding=gbk
  	name = input("请输入用户名")
  	print("欢迎使用本系统",name)
  ```

  并将文件保存为hello.py

  打开终端

  输入	python 文件路径\hello.py

- 优化配置

  将python路径添加到系统环境变量中。

### 2.2 安装PyCharm编辑器

- 下载PyCharm

  > https://www.jetbrains.com/pycharm/

- 安装

- 快速使用

  New Project时，选择Proviously configured interpreter先前配置的解释器选项，选择自己安装的解释器。



