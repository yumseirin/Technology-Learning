# Arch Linux

> Arch社区：https://archlinux.org/
>
> Arch中文论坛：https://bbs.archlinuxcn.org/

## 一、安装前准备

### 1.下载

下载网址：https://archlinux.org/download/

下载ISO文件和GnuPG签名放在同一路径下。

archlinux-2021.10.01-x86_64.iso和archlinux-2021.10.01-x86_64.iso.sig

### 2.验证签名

#### 2.1Windows验证

- 下载安装GnuPG
  - 下载链接https://www.gnupg.org/download/
  - 下载windows版gpg4win.exe
  - 安装GPG

- 打开CMD窗口，输入gpg --version验证是否安装成功（显示版本号）

- 命令行cd进入iso和GnuPG签名的路径

- 输入gpg --keyserver-options auto-key-retrieve --verify archlinux-version-x86_64.iso.sig

  - version替换成下载iso的版本号，如2021.10.01

  - ```powershell
    gpg --keyserver-options auto-key-retrieve --verify archlinux-2021.10.01-x86_64.iso.sig
    
    gpg: assuming signed data in 'archlinux-2021.10.01-x86_64.iso'
    gpg: Signature made 2021/10/2 1:03:20 й׼ʱ
    gpg:                using RSA key 4AA4767BBC9C4B1D18AE28B77F2D434B9741E8AC
    gpg:                issuer "pierre@archlinux.de"
    gpg: Can't check signature: No public key
    ```

  - 应该会出错，因为缺少公钥，无法验证，但得到了钥匙号（下载iso的页面其实能找到）。

  - 输入命令导入公钥。

  - ```powershell
    gpg --recv-keys --keyserver keyserver.ubuntu.com --recv 4AA4767BBC9C4B1D18AE28B77F2D434B9741E8AC
    gpg: key 7F2D434B9741E8AC: public key "Pierre Schmitz <pierre@archlinux.de>" imported
    gpg: Total number processed: 1
    gpg:               imported: 1
    ```

  - 再输入一遍验证的命令。

  - ```powershell
    gpg --keyserver-options auto-key-retrieve --verify archlinux-2021.10.01-x86_64.iso.sig
    
    gpg: assuming signed data in 'archlinux-2021.10.01-x86_64.iso'
    gpg: Signature made 2021/10/2 1:03:20 й׼ʱ
    gpg:                using RSA key 4AA4767BBC9C4B1D18AE28B77F2D434B9741E8AC
    gpg:                issuer "pierre@archlinux.de"
    gpg: Good signature from "Pierre Schmitz <pierre@archlinux.de>" [unknown]
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: 4AA4 767B BC9C 4B1D 18AE  28B7 7F2D 434B 9741 E8AC
    ```

  - 可以无视后边的警告，这句Good signature from "Pierre Schmitz <pierre@archlinux.de>"就代表着验证通过了，ios文件并没有被更改过。

#### 2.2Linux验证

- 所有安装GnuPG的系统

  - 如果没安装，请安装一个，可以参考https://wiki.archlinux.org/index.php/GnuPG

  - ```shell
    gpg --keyserver-options auto-key-retrieve --verify archlinux-version-x86_64.iso.sig
    ```

- Arch Linux系统

  - ```shell
    pacman-key -v archlinux-version-x86_64.iso.sig
    ```

- 如果不想安装可以验证MD5和SHA1

  - ```shell
    $ md5sum archlinux-2021.10.01-x86_64.iso
    c76867784b21d6f70cb156d9d1f113db archlinux-2021.10.01-x86_64.iso
    
    $ sha1sum archlinux-2021.10.01-x86_64.iso
    77a20dcd9d838398cebb2c7c15f46946bdc3855e archlinux-2021.10.01-x86_64.iso
    ```

### 3.创建虚拟机

*如果用虚拟机安装*

- 创建一个虚拟机，视情况给配置

  - Linux版本选其他Linux或更高版本内核64位（不重要，选哪个没差）
  - CD/DVD选Arch的ISO文件
  - 网络选择NAT
  - 处理器和内存硬盘视情况给
  - 其他基本默认就好

- **更改固件类型为UEFI**

  - 虚拟机设置--选项--高级--固件类型--勾选UEFI

  - 强烈建议更改成UEFI，虽然BIOS也可以，但是有些落后，实体机也基本上都是UEFI了，教程也是UEFI居多。

  - > 安装archlinux BIOS 启动 和 UEFI 启动有哪些不同 ?
    >
    > ### 在创建启动分区时
    >
    > BIOS模式建立：mkdir /mnt/boot
    > UEFI模式建立：mkdir -p /mnt/boot/EFI
    >
    > ### 挂载时
    >
    > BIOS模式挂载：mount /dev/sda2 /mnt/boot
    > UEFI模式挂载：mount /dev/sda2 /mnt/boot/EFI
    >
    > ### 安装grub引导系统启动时
    >
    > 所以我们使用这个引导器。在单系统并且BIOS启动时，只需要grub就够了。UEFI启动还需要安装efibootmgr
    >
    > ```sh
    > pacman -S grub efibootmgr
    > ```
    >
    > 简而言之就是BIOS启动时安装 grub 即可
    > 如果时UEFI启动时，grub 和 efibootmgr 都需要安装

## 二、安装

### 1.启动虚拟机（或实体机）

- 更改屏幕显示大小*（可略，就是为了安装的时候看着方便点）*
  - 开机后直接按E，输入下方命令*（记得空格分隔）*
  - nomodeset video=800x450
- 光标选在第一行（开启后默认的那个，不动就可以），回车
- 设置字体（可略，找个方便看大点的字体）
  - setfont /usr/share/kbd/consolefonts/LatGrkCyr-12x12.psfu.gz

### 2.联网

- 虚拟机NAT连接和实体机直插网线应该直接就可以联网，ping一下百度试试就知道了

- 如果不能联网，比如需要连接WiFi

- ip link     查看网络接口

- ```sh
  ip link set wlan0 up  #启用wlan0，这是一个无线网络接口的名，可能会不同
  ```

- 开启无线网络接口后，查询附近可连接WiFi的名

- ```sh
  iwlist wlan0 scan | grep ESSID
  ```

- wpa_passphrase 检索出来的网络名 密码 > 文件名

  - 如 wpa_passphrase SR_Wifi 123456 > internet.conf

- ```sh
  wpa_supplicant -c internet.conf -i wlan0 & #通过这个配置文件连接网络
  ```

- ```sh
  dhcpcd &  #动态分配ip
  ```

### 3.同步系统时间

- ```sh
  timedatectl set-ntp true
  ```

### 4.硬盘分区

- 查看磁盘信息

  - ```sh
    fdisk -l
    ```

- 使用fdisk工具分区

  - ```sh
    fdisk /dev/sda  #这是被分区磁盘的位置，磁盘名会有不同
    ```

  - Command（m for help）

    - 输入m得到帮助信息
    - 输入p输出所有分区信息
    - 输入g创建一个空的GPT分区（也就是清空该磁盘所有数据）

  - 创建引导分区

    - 输入n添加分区
    - Partition number：分区号直接回车，默认1号
    - First sector：从磁盘哪里开始，直接默认回车
    - Last sector：问磁盘到哪里，就是分多大，输入+512M回车

  - 创建SWAP

    - 输入n
    - Partition number：输入3
    - First sector：直接默认回车，他会从上一个分配的磁盘尾部开始
    - Last sector：输入+2G回车（swap视情况给，我给的内存超过2G所以swap也给了2G，内存不到2G可以给内存同等量）

  - 创建主分区（/根目录）

    - 输入n
    - Partition number：默认2回车
    - First sector：直接默认回车
    - Last sector：直接默认回车，会将剩余所有磁盘空间都分配给主分区

  - 输入p确认分区内容（此时并没有真的对磁盘分区做改变）

  - 输入w保存分区

- 格式化分区

  - 格式化引导分区
    - mkfs.fat -F32 /dev/sda1
    - /dev/sda1是引导分区，引导分区必须是fat32格式
  - 格式化主分区
    - mkfs.ext4 /dev/sda2
  - 格式化swap
    - mkswap /dev/sda3   #制作swap
    - swapon /dev/sda3   #激活打开swap

