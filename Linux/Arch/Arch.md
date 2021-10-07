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

