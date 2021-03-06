# CentOS7学习

## 一、下载安装

访问linux.org，选择centos，找到centos对应版本的镜像网站下载。

新建虚拟机

安装：

1. 语言默认英文，最好不要改动，不然有可能会有乱码问题。
2. 时区选择shanghai
3. 软件software，按需求选择，也可以默认安装minimal版本，其他软件后续单独安装。
4. 硬盘分区
   1. 选择“I will configure partioning”，自定义配置。
   2. 添加引导分区/boot，分配256M
   3. 添加交换空间swap，分配4096M（内存的两倍）
   4. 添加根目录/，分配剩余所有磁盘空间

5. 配置主机名host name
6. root用户设置密码
7. 重启

## 二、配置Linux

### 1、网络配置

vi /etc/sysconfig/network-scripts/ifcfg-ens33

sysconfig：系统配置

network-scripts：网络的脚本

ifcfg-ens33：ens33的网络网卡配置

```
--修改
ONBOOT=yes
BOOTPROTO=static	//静态网络IP	dhcp 动态网络获取IP
--添加
IPADDR=192.168.11.100	//1和2都不能用
NETMASK=255.255.255.0
GATEWAY=192.168.11.2
DNS1=114.114.114.114
--删除
UUID
```

虚拟机VMware-->编辑-->虚拟网络配置

查看NAT模式的子网IP和子网掩码。

点击NAT设置，查看网关

重启网卡重新加载配置文件

- ip addr
- systemctl restart network.service
- ping www.baidu.com
- ctrl+c 终止命令

### 2、配置虚拟机防火墙

防火墙保护本机端口不被别人访问

如果端口需要被别人访问，需要添加端口的防火墙例外

关闭防火墙：

- systemctl stop firewalld（本次服务内关闭防火墙，立即关闭仅本次生效）
- systemctl disable firewalld（下次重启后禁用防火墙服务，长期生效）

### 3、软件安装限制

vi /etc/selinux/config

 SELinux是部署在 Linux 上用于增强系统安全的功能模块。

修改：SELINUX=disabled

此举让SELinux不生效了，关闭它其实就是因为太麻烦了，Linux其实挺安全的了，但是它仍然设定了更多的条规，如果不是足够了解（读那个麻烦的要死的文档）它很可能会给你带来很多不确定因素，倒不如关了一了百了。

### 4、创建快照

虚拟机-->快照-->快照管理器

点击“拍摄快照”，对快照命名（如：base），添加描述。

### 5、克隆

链接克隆

- 当前节点文件夹只存储差异性数据
- 相同数据存放在原始节点上
- 优点：节省空间 缺点：耦合性大

完整克隆

- 就是基于原始节点完全拷贝到新节点的文件夹中
- 优点：耦合性低 缺点：硬盘空间使用大
- 推荐使用完整克隆

![image-20210911172508793](centos7.assets/image-20210911172508793.png)

克隆出来的系统要修改ip和主机名。

输入hostname 新主机名  只能临时生效，可exit退出账户再登录查看，但重启后无效。

vi /etc/hostname	可彻底修改

## 三、Linux的文件系统

> **万事万物皆文件**

文件系统：操作系统如何管理文件，内部定义了一些规则或者定义。

在Linux中所有的东西都是以文件的方式进行操作

Linux维护着一个树状结构的文件模型：

- 只有一个根节点/
- 一个节点上可以有多个子节点

查找文件的方式：

- 相对路径
  - 以当前路径为基准点，查找其他资源
  - vi  ../etc/sysconfig/network
- 绝对路径
  - 以根目录为基准点，查找其他资源
  - vi /etc/sysconfig/network-scripts/ifcfg-ens33
- 日常使用中，只要找到路径即可，但是如果是一些配置文件，尽量写绝对路径

可以随意的挂载磁盘

- 如：mount /dev/disk1 /usr/download

### Linux 根目录（/）

1、一级目录

| 一级目录 | 功能（作用）                                                 |
| -------- | ------------------------------------------------------------ |
| /bin/    | 存放系统命令，普通用户和 root 都可以执行。放在 /bin 下的命令在单用户模式下也可以执行 |
| /boot/   | 系统启动目录，保存与系统启动相关的文件，如内核文件和启动引导程序（grub）文件等 |
| /dev/    | 设备文件保存位置                                             |
| /etc/    | 配置文件保存位置。系统内所有采用默认安装方式（rpm 安装）的服务配置文件全部保存在此目录中，如用户信息、服务的启动脚本、常用服务的配置文件等 |
| /home/   | 普通用户的主目录（也称为家目录）。在创建用户时，每个用户要有一个默认登录和保存自己数据的位置，就是用户的主目录，所有普通用户的主目录是在 /home/ 下建立一个和用户名相同的目录。如用户 liming 的主目录就是 /home/liming |
| /lib/    | 系统调用的函数库保存位置                                     |
| /media/  | 挂载目录。系统建议用来挂载媒体设备，如软盘和光盘             |
| /mnt/    | 挂载目录。早期 Linux 中只有这一个挂载目录，并没有细分。系统建议这个目录用来挂载额外的设备，如 U 盘、移动硬盘和其他操作系统的分区 |
| /misc/   | 挂载目录。系统建议用来挂载 NFS 服务的共享目录。虽然系统准备了三个默认挂载目录 /media/、/mnt/、/misc/，但是到底在哪个目录中挂载什么设备可以由管理员自己决定。例如，笔者在接触 Linux 的时候，默认挂载目录只有 /mnt/，所以养成了在 /mnt/ 下建立不同目录挂载不同设备的习惯，如 /mnt/cdrom/ 挂载光盘、/mnt/usb/ 挂载 U 盘，都是可以的 |
| /opt/    | 第三方安装的软件保存位置。这个目录是放置和安装其他软件的位置，手工安装的源码包软件都可以安装到这个目录中。不过笔者还是习惯把软件放到 /usr/local/ 目录中，也就是说，/usr/local/ 目录也可以用来安装软件 |
| /root/   | root 的主目录。普通用户主目录在 /home/ 下，root 主目录直接在“/”下 |
| /sbin/   | 保存与系统环境设置相关的命令，只有 root 可以使用这些命令进行系统环境设置，但也有些命令可以允许普通用户查看 |
| /srv/    | 服务数据目录。一些系统服务启动之后，可以在这个目录中保存所需要的数据 |
| /tmp/    | 临时目录。系统存放临时文件的目录，在该目录下，所有用户都可以访问和写入。建议此目录中不能保存重要数据，最好每次开机都把该目录清空 |

FHS 针对根目录中包含的子目录仅限于上表，但除此之外，Linux 系统根目录下通常还包含下表中的几个一级目录

> 注：FHS（Filesystem Hierarchy Standard），文件系统层次化标准，该标准规定了 Linux 系统中所有一级目录以及部分二级目录（/usr 和 /var）的用途。发布此标准的主要目的就是为了让用户清楚地了解每个目录应该存放什么类型的文件。

| 一级目录     | 功能（作用）                                                 |
| ------------ | ------------------------------------------------------------ |
| /lost+found/ | 当系统意外崩溃或意外关机时，产生的一些文件碎片会存放在这里。在系统启动的过程中，fsck 工具会检查这里，并修复已经损坏的文件系统。这个目录只在每个分区中出现，例如，/lost+found 就是根分区的备份恢复目录，/boot/lost+found 就是 /boot 分区的备份恢复目录 |
| /proc/       | 虚拟文件系统。该目录中的数据并不保存在硬盘上，而是保存到内存中。主要保存系统的内核、进程、外部设备状态和网络状态等。如 /proc/cpuinfo 是保存 CPU 信息的，/proc/devices 是保存设备驱动的列表的，/proc/filesystems 是保存文件系统列表的，/proc/net 是保存网络协议信息的...... |
| /sys/        | 虚拟文件系统。和 /proc/ 目录相似，该目录中的数据都保存在内存中，主要保存与内核相关的信息 |

### Linux /usr目录

usr（注意不是 user），全称为 Unix Software Resource，此目录用于存储系统软件资源。FHS 建议所有开发者，应把软件产品的数据合理的放置在 /usr 目录下的各子目录中，而不是为他们的产品创建单独的目录。

Linux 系统中，所有系统默认的软件都存储在 /usr 目录下，/usr 目录类似 Windows 系统中 C:\Windows\ + C:\Program files\ 两个目录的综合体。

| 子目录       | 功能（作用）                                                 |
| ------------ | ------------------------------------------------------------ |
| /usr/bin/    | 存放系统命令，普通用户和超级用户都可以执行。这些命令和系统启动无关，在单用户模式下不能执行 |
| /usr/sbin/   | 存放根文件系统不必要的系统管理命令，如多数服务程序，只有 root 可以使用。 |
| /usr/lib/    | 应用程序调用的函数库保存位置                                 |
| /usr/XllR6/  | 图形界面系统保存位置                                         |
| /usr/local/  | 手工安装的软件保存位置。我们一般建议源码包软件安装在这个位置 |
| /usr/share/  | 应用程序的资源文件保存位置，如帮助文档、说明文档和字体目录   |
| /usr/src/    | 源码包保存位置。我们手工下载的源码包和内核源码包都可以保存到这里。不过笔者更习惯把手工下载的源码包保存到 /usr/local/src/ 目录中，把内核源码保存到 /usr/src/linux/ 目录中 |
| /usr/include | C/[C++](http://c.biancheng.net/cplus/) 等编程语言头文件的放置目录 |

### Linux /var 目录

/var 目录用于存储动态数据，例如缓存、日志文件、软件运行过程中产生的文件等。

| /var子目录        | 功能（作用）                                                 |
| ----------------- | ------------------------------------------------------------ |
| /var/lib/         | 程序运行中需要调用或改变的数据保存位置。如 [MySQL](http://c.biancheng.net/mysql/) 的数据库保存在 /var/lib/mysql/ 目录中 |
| /var/log/         | 登陆文件放置的目录，其中所包含比较重要的文件如 /var/log/messages, /var/log/wtmp 等。 |
| /var/run/         | 一些服务和程序运行后，它们的 PID（进程 ID）保存位置          |
| /var/spool/       | 里面主要都是一些临时存放，随时会被用户所调用的数据，例如 /var/spool/mail/ 存放新收到的邮件，/var/spool/cron/ 存放系统定时任务。 |
| /var/www/         | RPM 包安装的 Apache 的网页主目录                             |
| /var/nis和/var/yp | NIS 服务机制所使用的目录，nis 主要记录所有网络中每一个 client 的连接信息；yp 是 linux 的 nis 服务的日志文件存放的目录 |
| /var/tmp          | 一些应用程序在安装或执行时，需要在重启后使用的某些文件，此目录能将该类文件暂时存放起来，完成后再行删除 |

## 四、Linux的命令

### 1.Linux命令的首要须知

- Linux命令与参数之间必须用空格隔开
- Linux命令是区分大小写的
- 如果输入了错误的命令
  - -bash: abc: command not found
  - 命令敲错了
  - 命令未安装
- type 命令
  - type工具用于显示命令的类型信息。它将展示在命令行上输入给定的命令将如何解释。
  - ls is aliased to  ls --color=tty
  - cd is a shell builtin
  - vim is hashed (/usr/bin/vim)
  - sleep is /usr/bin/sleep
- 命令的帮助文档
  - help
    - 内置命令的帮助文档
  - man
    - 外部命令的帮助文档
    - 如果是minimal版的系统，very basic没有man包
    - 需要手动安装man
      - yum install -y man man-pages

### 2.常用的命令

- whereis 查询命令文件的位置
- file查看文件的类型
- who查看当前在线的用户
- whoami 我是谁
- pwd 我在哪儿
- uname -a 查看内核信息
- echo 类似于 sout syso ，打印语句
- clear 清屏
- history历史

### 3.特殊字符

- .  点：
  - 如果文件的开始是.说明当前文件是一个隐藏文件
  - .指向当前目录
  - ..指向当前目录的上级目录
- $
  - 说明这是一个变量
    - $PATH Linux的环境变量
- * 星号
    * 通配符
- ~
  - 当前用户的家目录
  - 每个用户的家目录是不同的
  - root用户家目录在系统根目录下
  - 其他用户的家目录在/home/用户名
- 空格
  - Linux的命令与参数用空格隔开
- /
  - 整个Linux的文件根目录
- 命令的参数
  - 如果是单词 一般加--
  - 如果是字母或者缩写一般加-

### 4.文件的操作命令

- cd
  - 改变当前工作目录
- ls    ll
  - 显示出指定目录下所有的文件
  - 文件的类型
    - -普通文件
    - d文件夹
    - l软连接
  - -rw-r--r--. 1 root root 3384 Nov 11 23:25 install.log.syslog
- mkdir
  - 创建文件目录
  - mkdir -p a/b/c/d/e/f 会自动创建文件父目录
  - mkdir -p aaa/{1,2,3}ls 一次可以创建多个子目录1ls,2ls,3ls
- rmdir
  - 删除空文件夹
    - rmdir:failed to remove 'a1': Directory not empty
    - rmdir:failed to remove 'baidu': Not a directory
  - 可以安全的删除文件目录
- cp
  - 拷贝文件或者文件目录
  - cp 源文件 目标目录
    - cp abcd /opt
    - cp /opt/abcd ./
  - 拷贝文件夹
    - cp -r abc /opt  （-r是递归的意思）
    - 拷贝文件夹下所有的内容
    - cp: omitting directory '/root/a1'
- mv
  - 移动文件或者文件夹
    - mv a1 /opt
    - mv abc /opt
  - 修改文件名称
    - mv a abcd
- rm
  - 删除文件
    - rm install.log
    - rm -f install.log  （-f强制删除）
  - 删除文件夹
    - rm -r abcd
    - rm -rf abcd **谨慎使用**
- touch
  - 如果没有就创建一个文件
  - 如果该文件已经存在，修改文件的三个时间，将三个时间改为当前时间
- stat
  - 查看文件的状态
  - Inode当前文件在文件系统的唯一标识，类似于ID
  - 时间
    - access访问时间
    - modify修改文件内容时间
    - change修改文件元数据信息时间
      - 文件大小，文件所有者，文件权限
      - 对于文件的描述信息
- ln
  - 创建文件的链接
  - 软（符号）链接
    - ln -s a1 sl
    - 软连接和原始文件不是同一个文件
      - a1  67170161
      - sl   67170154
    - 软连接指向的是那个路径，如果源文件删除或改名了就找不到了，如果再建一个同名的文件，inode不同软连接也将指向这个新文件。
    - rm -rf sl
  - 硬链接
    - ln a2 hl
    - 硬链接和原始文件使用文件系统中的同一个文件
    - 硬链接与源文件指向的是同一块硬盘空间只认inode，如果删除了源文件，硬链接仍然可以找到这块硬盘空间，如果建立同名文件，这个新文件是指向新的硬盘空间新的inode，与前文件和硬链接无关
    - 如果你害怕一个文件被别人误删，你可以使用硬链接保护这个文件
  - 软硬链接在链接文件的时候，推荐使用文件的绝对路径，否则有可能会出现问题

### 5.文件的读取命令

- cat
  - 将整个文档加载到内存中，并进行一次性显示
  - 除非后面使用管道，传递数据
- tac
  - 将整个文档加载到内存中，并进行一次性按行逆序显示
- more less
  - 分页查看文档内容
  - 快捷键
    - 回车  下一行
    - 空格  下一页
    - b  回退
    - q  退出
- head
  - 从文章开始读取N行
  - 默认如果超过10行读取10行，否则读取现在行数
  - head -5 profile
- tail
  - 从文章末尾读取N行
  - head -3 profile | tail -1
    - 利用管道只读取第N行
    - 管道的作用就相当于把前面的结果以参数的方式传递给后面的命令
  - 读取新增数据
    - ping www.baidu.com >> baidu
    - tail -F baidu
    - 如果f：
      - 它会监听inode的文件数据变化，但是当文件被删除后
      - 即使新创建，inode也会发生变化，于是监听失败
    - 如果F：
      - 他会监听指定名字的文件，如果文件被删除后，重新创建
      - 他会重新监听新文件的数据变化，监听不受影响
- find
  - 查找指定的文件
  - find 要查找的范围 -name 名字
  - find /etc -name profile

### 6.文件大小

- 查看分区信息
  - df -h
- 指定文件目录大小
  - du -h --max-depth=1 a/
  - 查看这个目录下所有文件所占大小
  - --max-depth=1 是该命令查看的深度，只看1层
- swap
  - 一个特殊分区，以硬盘代替内存
  - 当内存使用满的时候可以将一部分数据写出到swap分区

## 五、VI和VIM编辑器

### 1.打开文件

- 正常打开
  - vi profile
- 打开文件，并将光标置于第8行
  - vi +8 profile
- 打开最后一行
  - vi + profile
  - 按n查找下一个，按N查找上一个
- 打开指定搜索单词的位置
  - vi +/if profile

### 2.三种模式

- 编辑模式
  - 编辑模式中，每一个按键都有其他的功能
- 输入模式
  - 每一个按键按下什么，就向文本中输入什么
- 末行（命令行）模式
  - 可以直接在vi中输入特定的命令

![image-20210913012352909](centos7.assets/image-20210913012352909.png)

![image-20210913012944240](centos7.assets/image-20210913012944240.png)

- 编辑模式-->输入模式
  - i在当前位置插入数据
  - a追加数据
  - o在当前行后面开启一个新的输入行
  - I行首
  - A行尾
  - O上一行
- 输入模式-->编辑模式
  - 按下ESC
- 编辑模式-->末行模式
  - 按下：
- 末行模式-->编辑模式
  - 按下ESC

### 3.编辑模式

- G最后一行
- gg跳转到第一行
- 数字gg跳转到第数字行
- w下个单词
- 数字w
- dw删除一个单词
- 3dw删除三个单词
- dd 删除一行
- 3dd删除三行
- u回退到前面的操作
- .回退u执行的操作
- yw复制一个单词
- 3yw复制三个单词
- yy复制一行
- 3yy复制三行
- p粘贴
- 6p粘贴6次
- x剪切
- 3x剪切三个字符
- r替换，然后输入一个字符替换
- 3r替换三个
- hjkl方向键
- ZZ保存并退出
- ctrl+s锁屏 ctrl+q解锁

### 4.末行模式

- set nu 设置行号
- set nonu 取消行号
- w保存
- q退出
- wq保存并退出
- q! 强制退出，但是不保存
- 如果上次异常退出会保留同名隐藏文件，每次启动会给与提示
  - 如果确定当前文件没问题，请删除隐藏文件
- /pattern
  - /搜索指定的字符串
  - /usr n向下查找 N逆向查找
- s/p1/p2/g
  - p1替换成字符串p2
  - g替换当前行所有  没有g只替换当前行第一个
    - s/abc/xyz/g
  - 查找指定行
    - 3,8s/abc/xyz/g
  - 替换全文
    - g/abc/s//xyz/g

## 六、计算机间的数据传输

### 1.Windows--Linux

- lrzsz
  - 需要手动安装
    - yum instal lrzsz -y
  - rz
    - received（接收）
    - 将文件从Windows上传到Linux
  - sz 文件
    - send（发送）
    - 将文件从Linux传输到Windows
  - 不论是rz还是sz，动作都是在服务器上发起的
- xftp
  - 较为通用的文件传输方式

### 2.Linux--Linux

- scp 源数据地址(source) 目标数据地址(target)
- scp abc.md root@192.168.11.101:/opt
- scp root@192.168.11.101:/opt/abc.md ./
- scp -r a root@192.168.11.101:/opt
  - 如果拷贝的文件夹，需要加-r迭代

## 七、文件压缩

### 1.tar

- 主要是针对文件是  abc.tar.gz
- 解压缩
  - tar -zx(解压)v(过程)f(文件) abc.tar.gz
- 压缩
  - tar -zc(压缩)f(文件) tomcat.tar.gz(压缩后的名字) apache-tomcat-7.0.61(源文件)
  - tar -zxf tomcat.tar.gz -C /opt/
    - -C指定解压缩的文件目录

### 2.zip和unzip

- 安装
  - yum install zip unzip -y
- 压缩
  - zip -r tomcat.zip apache-tomcat-7.0.61
- 解压缩
  - unzip tomcat.zip

## 八、Linux的网络信息

### 1.主机名称

- 临时修改
  - hostname school
- 长久修改
  - vi /etc/hosthome

### 2.DNS解析

- 域名解析服务
- 可以将域名转换为IP地址
- DNS域名劫持
  - windows --> C:\Windows\System32\drivers\etc\hosts
  - 123.45.123.45 www.baidu.com
- 修改主机域名
  - vi /etc/hosts
  - 将来需要把所有的虚拟机都配置hosts文件
  - 192.168.11.101 centos7_test2
  - 192.168.11.102 centos7_test3

### 3.网络相关命令

- ifconfig
  - 查看当前网卡的配置信息
  - 这个命令属于net-tools中的一个命令，但是CentOS7中minimal版并没有集成这个包
  - 所以需要自己手动安装yum install net-tools -y
  - 如果没有ifconfig，可以使用ip addr临时代替
- netstat
  - 查看当前网络的状态信息
  - 一个机器默认有65536个端口号[0,65535]
  - 这是一个逻辑的概念，将来我们需要使用程序监听指定的端口，等待别人的访问
  - netstat -anp 看端口的监控情况，端口和端口的监控程序
  - netstat -r 核心路由表  == route
- ping
  - 查看与目标IP地址是否能够连通
- telnet
  - 查看与目标IP的指定端口是否能够连通
  - yum install telnet -y
  - telnet 192.168.11.101 22

- curl
  - restful 所有的资源在网络上都有唯一的定位
  - 那么就可以通过这个唯一定位标识指定的资源
  - http://localhost:8080/abc/user.cation/123
  - curl -X GET http://www.baidu.com

### 4.加密算法

#### 4.1不可逆加密算法

- 可以通过数据计算加密后的结果，但是通过结果无法计算出加密数据
- 应用场景
  - Hash算法常用在不可还原的密码存储、信息完整性校验
  - 文档、音视频文件、软件安装包等用新老摘要对比是否一样（接收到的文件是否被修改）
  - 用户名或者密码加密后数据库存储（数据库大多数不会存储关键信息的明文，就像很多登录功能的忘记密码不能找回，只能重置）

#### 4.2对称加密算法

![image-20210914201248391](centos7.assets/image-20210914201248391-16316215697371.png)

- Symmetric Key Encryption
- 代表性算法叫做DES , 3DES , Blowfish , IDEA , RC4 , RC5 , RC6 和 AES
- 特点
  - 加密和解密使用相同的密钥
- 优点
  - 生成密钥的算法公开，计算量小，加密速度快，加密效率高，密钥较短
- 缺点
  - 双方共同的密钥，有一方密钥被窃取，双方都影响
  - 如果为每个顾客都生成不同密钥，则密钥数量巨大，密钥管理有压力
- 应用场景
  - 登录信息用户名和密码加密，传输加密，指令加密

#### 4.3非对称加密算法

![image-20210914210155828](centos7.assets/image-20210914210155828.png)

- Asymmetric Key Encryption
- 非对称加密算法需要一对密钥（两个密钥）：
  - 公开密钥（publickey）和私有密钥（privatekey）（简称公钥、私钥）。
  - 公开密钥与私有密钥生成时是一对
  - 用公钥加密只能是对应的私钥解密，同理用私钥加密只能用对应的公钥解密。
- 代表性算法叫做RSA、ECC、Diffie-Hellman、EI Gamal、DSA（数字签名用）
- 优点：
  - 安全性高（几乎很难破解）
- 缺点：
  - 加解密相对速度慢、密钥长、计算量大、效率低
- 应用场景
  - HTTPS（ssl）证书的制作，CRS请求证书、金融通信加密、蓝牙等硬件信息加密配对传输、关键的登录信息验证。
- http://tool.chacuo.net/cryptrsaprikey

### 5.主机间的相互免密钥

- 可以通过ssh命令免密钥连接到其他主机
- 如果是第一次建立连接，需要输入yes
  - 在~/.ssh/known_hosts文件记录了以前访问地址（ip hostname）的信息
  - 在访问地址的时候如果没有收录到known_hosts文件中，就需要输入yes
  - 如果以前收录到known_hosts中，直接输入密码即可
- 需要输入密码
  - 生成秘钥
    - ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
  - 如果想免密钥登录谁，只需要把自己的公钥传递给对方主机即可
  - 这个密钥放在 ~/.ssh/authorized_keys
    - ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.11.101
- 相互免密钥工作流程

### 6.主机名与Host校验

- 错误原因

- Cannot determine realm for numeric host

- 解决方案1---本次

  - ssh -v -o GSSAPIAuthentication=no root@192.168.11.101

- 解决方案2--所有

  - 修改/etc/ssh/ssh_config文件的配置，以后则不会在出现此问题

  - 最后面添加：

  - StrictHostKeyChecking no

    UserKnownHostsFile /dev/null

## 九、日期与时间

### 1.时间命令

- date
  - 查看当前系统时间
- cal 查看日历
  - cal 2020
- 修改时间
  - date -s 10:10:10
  - date -s 2020-10-10
  - date -s '2020-10-10 10:10:10'

### 2.日期自动同步

- 自动同步时间
  - yum install ntp -y
  - ntpdate cn.ntp.org.cn

### 3.命令执行时间统计

```shell
#！/bin/bash
start=$(date +%s)
nmap man.linuxde.net &> /dev/null

end=$(date +%s)
difference=$((end - start))
echo $difference seconds.
```

## 十、用户-组-权限

### 1.用户

- 新增用户
  - useradd boss
  - 会创建同名的组和家目录
- 设置密码
  - passwd boss
- 删除用户
  - userdel -r boss
  - 级联删除家目录和组
- 修改用户信息
  - usermod -l aoss（新名） boss (旧名)
    - 家目录和组名称是不会被修改的
  - usermod -L boss 锁定用户名
  - usermod -U boss解锁用户名
- 常用文件
  - cat /etc/shadow
    - 用户名和密码
  - cat /etc/passwd
    - 用户名，编号，组编号，家目录，命令，目录
    - 6.5系统0-499普通从500+开始
    - 7系统0-999 普通从1000+开始
- 切换账户
  - su boss

### 2.组

- 创建组
  - groupadd leader
- 删除组
  - groupdel leader
- 修改组名字
  - groupmod -n teacher leader
- 查看用户对应的组
  - groups
    - 查看当前用户的组
  - groups boss
    - boss ：boss 可以查看该用户所属的组
    - 当我们创建用户的时候，会默认创建一个同名的主组
- 修改用户的组
  - usermod -g leader boss（主组）
  - usermod -G teacher boss（附属组，没有就添加，有就替换）
- /etc/group中是所有的用户组

### 3.权限

![image-20210915210944548](centos7.assets/image-20210915210944548.png)

- 查看文件的权限
  - drw-r-xr-x 9 n1 m1 4096 Nov 13 00:03 apache-tomcat-7.0.1
  - 三组权限，每组3个字母
    - r：读取权限
    - w：写入权限
    - x：执行权限
    - -：没有权限
  - root：所属用户（属主）
  - root：所属的组（属组）
- 权限的UGO模型
  - 三组权限
  - 属主的权限：属组的权限：其他的权限
  - 修改文件的权限，可以从rwx和ugo两个方面进行修改
- 修改文件的权限
  - 修改文件所属
    - chown n1 /var/abc1 改主
    - chown n1:m1 /var/abc2 改主和组
    - 修改文件夹时，让子目录迭代修改
      - chown -R n1:m1 school
    - chgrp m2 abc3
      - 当用户的组被修改之后，需要重新登录才能获取新组的权限
  - 修改文件的rwx
    - chmod o+w abc4
    - chmod ug+rw abc4
    - chmod ugo-rw abc4
    - （权限rwx分别对应数字421 5=4+0+1 r-x）
      - chmod 664 abc4 -->（rw-rw-r--）

![image-20210915214248543](centos7.assets/image-20210915214248543.png)

### 4.权限赋予

- 可以将管理用的权限分配给普通用户
- 文件位置在 vim /etc/sudoers
- 但是修改这个文件需要使用命令
  - visudo
  - 修改Line 99
  - n1 ALL=(root) /sbin/*  （n1是用户名）
  - n1 ALL=(root) /sbin/useradd  （给n1添加用户的命令）
  - n1 ALL=(root) /sbin/chkconfig
- 如何使用
  - su n1
  - sudo chkconfig iptables off

## 十一、管道与重定向

### 1.管道

- | 将前面命令的结果作为参数传递给后面的命令
- grep
  - 强大的文本搜索工具
  - cat profile | grep if
  - ls / | grep ^t

### 2.重定向

- 改变数据输出的位置，方向
- 0 in    1 out     2 err
  - ls / 1> abc 标准输出
  - ls / > abc 标准输出
  - ls abcd 2> 错误输出
  - 1> 重定向正确的信息
  - 2>重定向错误的信息
  - 默认重定向正确的信息
- \> 替换   >> 追加
  - ls / 1>> abc
  - ls / 1> abc
- 结合使用
  - ls /etc/abcd > abc 2>&1
  - ls /etc/abcd >> abc 2>&1
- 信息黑洞
  - ls /etc/abcd >> /dev/null 2>&1

## 十二、Linux的系统进程

### 1.进程信息

- echo $$ 返回登录shell的PID

- ps -ef
  - UID   PID  PPID   C   STIME   TTY     TIME  CMD
  - UID所属用户
  - PID当前进程编号
  - PPID当前进程编号的父进程编号
- ps -ef | grep redis  
  - 以前边命令获得的结果为参数进行模糊查询搜索这个字符串
- ps -aux
  - 所有信息
- ps -aux --sort -pcpu
- top
  - 当前服务器内存使用率 

### 2.后台进程

- 只需要在命令的后面添加一个&符号
  - ping www.baidu.com >> baidu &
- jobs -l
  - 可以查看当前的后台进程
  - 但是只有当前用户界面可以获取到
- nohup可以防止后台进程被挂起
  - nohup ping www.baidu.com >> baidu 2>&1 &

### 3.杀死进程

- kill -9 29948

## 十三、Linux的软件安装

### 1.环境变量

Linux的环境变量是$PATH

配置文件在/etc/profile

window路径与路径之间用;分号连接

Linux路径与路径之间用:冒号连接

Linux每次修改完成之后，需要重新加载文件 source /etc/profile

### 2.软件的安装方式

- 解压直接使用
- 使用安装包安装（window-exe；Linux-rpm）
  - 自己下载安装包
  - 使用统一的软件帮助安装
- 通过源码安装

### 3.RPM安装

- RedHat Package Manager，属于红帽的一种包管理方式

- 通过RPM命令安装软件

  - rpm -ivh jdk-8u301-linux-x64.rpm

- 可以查询软件

  - rpm -qa | grep jdk
  - rpm -q jdk

- 卸载

  - rpm -e jdk1.8-1.8.0_301-fcs.x86_64

- 需要手动配置Java的环境变量

  - vim /etc/profile

  - ```SHELL
    export JAVA_HOME=/usr/java/jdk1.8.0_301-amd64
    export PATH=$JAVA_HOME/bin:$PATH
    ```

  - 重新加载配置文件

    - source /etc/profile

### 4.压缩包解压安装

- 解压文件
  - tar -zxf apache-tomcat-8.5.71.tar.gz
- 拷贝到/opt目录下
  - cp -r apache-tomcat-8.5.71 /opt
- 启动tomcat
  - cd /opt/apache-tomcat-8.5.71/bin/
  - ./startup.sh

### 5.YUM安装

#### 5.1yum的作用

- 可以管理RPM包
- 可以安装软件
- 如果软件有其他依赖，会先安装依赖后再安装软件
- 类似于Maven

#### 5.2yum命令

- search 查询命令或者软件
  - yum search ifconfig
- info 查看包的信息
  - yum info ntp
- list
  - yum list 查看所有可安装的rpm包
  - yum list java-1.8* 只查询某一种包

5.3更换yum源

- 首先安装wget
  - yum install wget -y
- 将系统原始配置文件失效
  - mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
- 使用wget获取阿里yum源配置文件
  - wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
- 清空以前yum源的缓存
  - yum clean all
- 获取阿里云的缓存
  - yum makecache

### 6.安装MySQL数据库

```shell
#----------安装MySQL依赖【perl net-tools】
yum install perl net-tools -y
#----------卸载mariadb
rpm -qa | grep mariadb
rpm -e --nodeps mariadb-libs-5.5.68-1.el7.x86_64
#----------安装mysql
tar -xvf mysql-5.7.35-1.el7.x86_64.rpm-bundle.tar

rpm -ivh mysql-community-common-5.7.35-1.el7.x86_64.rpm
rpm -ivh mysql-community-libs-5.7.35-1.el7.x86_64.rpm
rpm -ivh mysql-community-client-5.7.35-1.el7.x86_64.rpm
rpm -ivh mysql-community-server-5.7.35-1.el7.x86_64.rpm

#---------启动mysql
systemctl start mysqld

#--------查找密码并登陆mysql
cat /var/log/mysqld.log | grep password
mysql -u root -p
#--------修改mysql密码
set global validate_password_policy=low;
set global validate_password_length=6;
alter user root@localhost identified by '123456';

#--------修改MySQL链接地址
use mysql;
update user set host='%' where user = 'root';
commit;
exit;

systemctl restart mysqld;
#--------使用Navicat连接MySQL
```

## 十四、Linux的三剑客

### 1.普通剑客

- cut
  - 用指定的规则来切分文本
  - cut -d':' -f1,2,3 passwd | grep mysql
- sort
  - sort abc
    - 对文本中的行进行排序
  - sort -t ' ' -k2 abc
    - 对每一行的数据用' '进行切分，按照第二列进行排序
  - sort -t' ' -k2 -r abc
    - 逆序
  - sort -t' ' -k2 -n abc
    - 按照数值大小进行排序，如果有字母，字母在前
- wc
  - 统计单词的数量
  - wc abc
  - 4 15 79 abc
    - -l  几行 line
    - -w  几个单词 word
    - -c  几个字符 char

### 2.剑客1号：grep

- 可以对文本进行搜索
- 同时搜索多个文件
  - grep 10 passwd abc 在passwd和abc中搜索10这个字符串
- 显示匹配的行号
  - grep -n abc passwd
- 显示不匹配的忽略大小写
  - grep -nvi abc passwd --color=auto 参数加v是显示不匹配的，i是忽略大小写
- 使用正则表达式匹配
  - grep -E "[1-9]+" passwd --color=auto

### 3.剑客2号：sed

- sed是Stream Editor（字符流编辑器）的缩写，简称流编辑器
- sed软件从文件或管道中读取一行，处理一行，输出一行；再读取一行，再处理一行，再输出一行
- 一次一行的设计使得sed软件性能很高
- vi命令打开文件是一次性将文件加载到内存
- 了解即可
  - https://www.cnblogs.com/chensiqiqi/p/6382080.html
- 行的选择模式
  - 10 第十行
  - m,n -->第m行到第n行 [m,n]
  - m,+n-->第m行开始加n行[m,m+n]
  - m~n-->从m行开始，每隔n行处理一次，n是步长
  - m,$ -->从m开始到最后一行
  - /school/ -->匹配到school的行
  - /u1/,/u4/ -->从匹配u1到匹配u4
- 增
  - sed '2a abcd' passwd 实际上文件没改动
  - sed '2i abcd' passwd
    - 打印到控制台
  - sed -i '2a abcd' passwd
    - 直接修改到文件
- 删
  - sed '3,10d' passwd 删除3到10行
- 改
  - 整行替换
    - sed '3,20c abcd' passwd
    - sed '3~1c abcd' passwd
  - 字符替换
    - sed '1,5s/root/abc/g' passwd
    - sed '1,5s#/#-#g' passwd

### 4.剑客3号：awk

- 它不是一个剑客，它是一门语言
- 了解即可
  - https://www.cnblogs.com/chensiqiqi/p/6481647.html
- 模式与动作
  - awk -F ":" 'NR>=2&&NR<=6' /etc/passwd  （NR是行号）
  - awk -F ":" '{print NR,$1}' /etc/passwd
  - awk -F ":" 'NR>=2&&NR<=6 {print NR,$1}' /etc/passwd
  - awk -F ":" 'NR==1 {print NR,$1} NR\==2{print NR,$NF}' /etc/passwd  （NF最后一行）

## 十五、Linux的shell编程

### 1.名词解释

- Kernel
  - Linux内核主要是为了和硬件打交道
- Shell
  - Shell是一个用C语言编写的程序，它是用户使用Linux的桥梁。Shell既是一种命令语言，又是一种程序设计语言。
  - Shell是指一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务。
- Shell环境
  - 只要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器就可以了。
  - Bourne Shell (/usr/bin/sh或/bin/sh)
  - Bourne Again Shell (/bin/bash) --默认
  - C Shell (/usr/bin/csh)
- #!声明
  - 告诉系统其后路径所指定的程序既是解释此脚本文件的Shell程序

### 2.执行Shell的方式

- ./abc.sh
  - 执行的必须是一个可执行文件
  - chmod u+x abc.sh
  - 会开启一个子进程执行脚本
  - 7080 (ssh) --> 12826(./var.sh) --> 12827(ping)
- sh abc.sh
  - 执行的文件可以是一个普通文件
- source abc.sh
  - 直接在当前进程执行脚本
  - 12661（ssh）--> 12797（ping）
  - 当我们使用bash的时候开启一个子进程，当脚本中出现ping的时候又开启了一个子进程

### 3.shell语法

- 变量

  - export：可以将当前进程的变量传递给子进程使用
    - 将来配置profile的时候，所有的变量前必须加export

- ```shell
  #! /bin/bash
  echo -e "\e[1;31m【-------在opt和var创建test文件夹】\e[0m"
  echo -e "\e[1;31m【-------禁用防火墙】\e[0m"
  echo -e "\e[1;32m【-------修改selinux】\e[0m"
  echo -e "\e[1;32m【-------安装wget】\e[0m"
  echo -e "\e[1;33m【-------修改yum源】\e[0m"
  echo -e "\e[1;33m【-------安装常用软件man man-pages ntp vim lrzsz unzip】\e[0m"
  echo -e "\e[1;34m【-------DNS域名配置】\e[0m"
  echo -e "\e[1;34m【-------安装JDK】\e[0m"
  echo -e "\e[1;35m【-------安装Tomcat】\e[0m"
  echo -e "\e[1;35m【-------安装Niginx】\e[0m"
  echo -e "\e[1;36m【-------设置开机启动项】\e[0m"
  echo -e "\e[1;36m【-------删除文件】\e[0m"
  shutdown -h now
  ```

## 十六、Linux的启动流程

### 1.系统启动流程

- 启动计算机的硬件（BIOS）

  - 读取时间
  - 选择对应的启动模式

- 如果是Linux系统，回去找/boot目录。引导这个系统启动

- 计算机系统开始启动，读取初始化配置文件

  - vim /etc/inittab

  - 启动时控制着计算机的运行级别runlevel

  - | 0    | halt（关机）                                                 |
    | ---- | ------------------------------------------------------------ |
    | 1    | Single user mode（单用户模式）                               |
    | 2    | Multiuser，without NFS（多用户模式，但是无网络状态）FS-->FileSystem |
    | 3    | Full multiuser mode（多用户完整版模式）                      |
    | 4    | unused（保留模式）                                           |
    | 5    | X11（用户界面模式）                                          |
    | 6    | reboot（重启模式）                                           |

  - id:3:initdefault:默认runlevel为3

  - 以runlecel=3开始启动对应的服务和组件

- 开始默认引导公共的组件或者服务

  - vim /etc/rc.d/rc.sysinit

- 开始加载对应runlevel的服务

  - vi /etc/rc3.d/
    - K：关机时需要关闭的服务
    - S：启动时需要开启的服务
    - 数字代表了开启或者关闭的顺序
    - 所有的文件都是软连接，链接的地址为/etc/init.d

- 当启动完毕，所有的服务也被加载完成

### 2.系统服务

- 我们可以使用chkconfig命令查看当前虚拟机的服务
- 通过查看可以得知不同的级别对应到每一个服务确定本次开机自动启动
- 开机结束后，我们需要使用service（CentOS6）systemctl（CentOS7）命令控制服务的开启或者关闭

### 3.开机自启动服务

- rc.local

  - 首先创建脚本存放的文件夹
    - mkdir -p /usr/local/scripts
  - 在文件夹中创建脚本文件
    - vim hello.sh
    - 给予执行权限
  - 去/etc/rc.d/rc.local文件中添加脚本的绝对路径
    - 给予rc.local执行权限

- chkconfig

  - 创建开机自启动脚本文件

  - vim autostart.sh

  - ```shell
    #!/bin/bash
    #chkconfig: 2345 88 99
    #description:auto_run
    
    #开机自启动同步时间
    yum info ntp && ntpdate cn.ntp.org.cn
    ```

  - 给其设置执行权限

    - chmod u+x autostart.sh

  - 将脚本拷贝到/etc/init.d目录下

    - cp autostart.sh /etc/init.d

  - 添加到服务

    - chkconfig --add /etc/init.d/autostart.sh

  - 重启服务器

    - reboot

### 4.定时任务

- 在系统服务中心，crond负责周期任务

  - systemctl status crond.service

- 添加任务，编辑当前用户的任务列表

  - crontab -e

- 编辑任务

  - 星 星 星 星 星 command

    分 时 日 月 周 命令

    第1列表示分钟1~59 每分钟用\*或者\*/1表示

    第2列表示小时0~23（0表示0点）

    第3列表示日期1~31

    第4列表示月份1~12

    第5列表示星期0~6（0表示星期天）

    第6列是要运行的命令

    *：表示任意时间都，实际上就是“每”的意思。可以代表00-23小时或者00-12每月或者00-59分

    -：表示区间，是一个范围，00 17-19 * * * cmd，就是每天17，18，19点的整点执行命令

    ,：是分割时段，30 3，19，21 * * * cmd，就是每天3，19，21点的半点时执行命令

    /n：表示分割，可以看成除法，*/5 * * * * cmd，每隔五分钟执行一次

  - ```shell
    30 21 * * * /usr/local/etc/rc.d/lighttpd restart
    上面的例子表示每晚的21:30重启apache。
    
    45 4 1,10,22 * * /usr/local/etc/rc.d/lighttpd restart
    每月的1，10，22号的4：45分重启apache
    
    10 1 * * 6,0 /usr/local/etc/rc.d/lighttpd restart
    每周六、周日的1：10分重启apache
    
    0,30 18-23 * * * /usr/local/etc/rc.d/lighttpd restart
    每天18到23点的每个整点和半点重启apache
    
    0 23 * * 6 /usr/local/etc/rc.d/lighttpd restart
    每周六的23点重启apache
    
    * */2 * * * /usr/local/etc/rc.d/lighttpd restart
    每两个小时重启apache
    
    * 23-7/1 * * * /usr/local/etc/rc.d/lighttpd restart
    每天23点到7点之间每1小时重启apache
    
    0 11 4 * mon-wen /usr/local/etc/rc.d/lighttpd restart
    每月的4号和周一到周三的11点重启apache
    
    0 4 1 jan * /usr/local/etc/rc.d/lighttpd restart
    一月一日的4点重启apache
    ```

- 重启crontab，使配置生效

  - systemctl restart crond.service

- 通过crontab -l

  - 查看当前的定时任务

- 查看任务的历史

  - vim /var/spool/mail/root

- 清除任务

  - crontab -r

## 十七、虚拟机初始化脚本

> ``中的字符串当做命令去执行

```shell
#! /bin/bash
## -bash: ./testinit.sh: /bin/bash^M: bad interpreter: No such file or directory
## vim或者vi的命令模式下，输入命令 set fileformat=unix 即可解决换行问题

echo -e "\e[1;31m【-------在opt和var创建test文件夹】\e[0m"
mkdir -p /opt/test
mkdir -p /var/test
mkdir -p /usr/local/script

echo -e "\e[1;31m【-------禁用防火墙】\e[0m"
systemctl stop firewalld
systemctl disable firewalld
systemctl status firewalld

echo -e "\e[1;32m【-------修改selinux】\e[0m"
sed -i '/^SELINUX=/c SELINUX=disabled' /etc/selinux/config

echo -e "\e[1;32m【-------安装wget】\e[0m"
yum install wget -y

echo -e "\e[1;33m【-------修改yum源】\e[0m"
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache

echo -e "\e[1;33m【-------安装常用软件man man-pages ntp vim lrzsz unzip telnet】\e[0m"
yum install man man-pages ntp vim lrzsz unzip telnet -y

echo -e "\e[1;34m【-------同步时间】\e[0m"
yum info ntp && ntpdate cn.ntp.org.cn

echo -e "\e[1;34m【-------DNS域名配置】\e[0m"
echo "192.168.11.100 centos-test1" >> /etc/hosts
echo "192.168.11.101 test1" >> /etc/hosts
echo "192.168.11.102 test2" >> /etc/hosts
echo "192.168.11.103 test3" >> /etc/hosts

echo -e "\e[1;34m【-------安装JDK】\e[0m"
rpm -ivh jdk-8u301-linux-x64.rpm
echo 'export JAVA_HOME=/usr/java/jdk1.8.0_301-amd64' >> /etc/profile
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> /etc/profile
source /etc/profile

echo -e "\e[1;35m【-------安装Tomcat】\e[0m"
tar -zxf apache-tomcat-8.5.71.tar.gz
mv  apache-tomcat-8.5.71 /opt/test/

echo -e "\e[1;35m【-------安装Niginx】\e[0m"

echo -e "\e[1;35m【-------安装Mysql】\e[0m"
rpm -e --nodeps `rpm -qa | grep mariadb`
yum install perl net-tools -y
tar -xvf mysql-5.7.35-1.el7.x86_64.rpm-bundle.tar

rpm -ivh mysql-community-common-5.7.35-1.el7.x86_64.rpm
rpm -ivh mysql-community-libs-5.7.35-1.el7.x86_64.rpm
rpm -ivh mysql-community-client-5.7.35-1.el7.x86_64.rpm
rpm -ivh mysql-community-server-5.7.35-1.el7.x86_64.rpm

systemctl start mysqld
systemctl enable mysqld

temppasswd=`grep "A temporary password" /var/log/mysqld.log | awk '{ print $NF }'`

mysql -u root -p$temppasswd --connect-expired-password << EOF
set global validate_password_policy=low;
set global validate_password_length=6;
alter user root@localhost identified by '123456';

use mysql;
update user set host='%' where user = 'root';
commit;
quit
EOF

systemctl restart mysqld

echo -e "\e[1;36m【-------设置开机启动项】\e[0m"
touch /usr/local/script/auto_ntpdate.sh
echo '#!/bin/bash' >> /usr/local/script/auto_ntpdate.sh
echo 'yum info ntp && ntpdate cn.ntp.org.cn' >> /usr/local/script/auto_ntpdate.sh
chmod u+x /usr/local/script/auto_ntpdate.sh
echo '/usr/local/script/auto_ntpdate.sh' >> /etc/rc.local
chmod u+x /etc/rc.local

echo -e "\e[1;36m【-------删除文件】\e[0m"
rm -rf apache-tomcat-8.5.71.tar.gz
rm -rf jdk-8u301-linux-x64.rpm
rm -rf mysql*
rm -rf *.sh

echo -e "\e[1;36m【-------关闭计算机，拍快照】\e[0m"
sleep 5
shutdown -h now

```

## 十八、虚拟机相互免密钥

```shell
##三台主机分别生成秘钥
[123] ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
##host验证
[123] vim /etc/ssh/ssh_config
	最后面添加：
	StrictHostKeyChecking no
	UserKnownHostsFile /dev/null
##将秘钥分别拷贝给自己和别人(不输入ip输入hostname的前提，做了上一步并且hosts中有加入该ip)
[123] ssh-copy-id -i ~/.ssh/id_rsa.pub root@test1
[123] 输入密码123456
[123] ssh-copy-id -i ~/.ssh/id_rsa.pub root@test2
[123] 输入密码123456
[123] ssh-copy-id -i ~/.ssh/id_rsa.pub root@test3
[123] 输入密码123456

##关闭主机拍摄快照
shutdown -h now
```

