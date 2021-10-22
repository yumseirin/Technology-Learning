# Fiddler抓包工具

## 一、下载安装

### 1.下载

官网链接：https://www.telerik.com/

![image-20211001024806747](Fiddler抓包.assets/image-20211001024806747.png)

Fiddler Classic（经典版），这个版本是**免费**的，不过只能在Windows上使用。

Fiddler Everywhere可以在所有平台使用，并且相当于Fiddler Classic+postman，但是是**收费**的。

如果只作为抓包工具经典版就够用了，可以直接点击下方链接前往下载页面。

下载链接：https://www.telerik.com/download/fiddler

![image-20211001030349465](Fiddler抓包.assets/image-20211001030349465.png)

填好信息之后勾选这两项，点击**下载**。

### 2.安装

点击同意后选择安装路径安装。

## 二、抓包

### 1.基础操作

#### 1.1抓取请求

- 界面左侧Web Sessions会话列表中的是HTTP数据包。

- 界面右侧Inspectors用于查看会话的内容，上边是Request请求信息，下边是Response响应信息。

- 左下角空白处点击变成Capturing会开始抓包

  - ALL Processes抓取所有包
  - Web Browsers只抓取PC中浏览器的包
  - Non-Browser抓取非浏览器的包
  - Hide All隐藏所有代理
    - 代理手机时，Capturing无论是否点击，都会自动抓包，抓取想要的包后，可点此隐藏其他抓包

- **字段说明**

  - | **名称**                                                     | **含义**                                                   |
    | :----------------------------------------------------------- | :--------------------------------------------------------- |
    | #                                                            | 抓取HTTP Request的顺序，从1开始，以此递增                  |
    | Result                                                       | HTTP状态码                                                 |
    | Protocol                                                     | 请求使用的协议，如HTTP/HTTPS/FTP等                         |
    | Host                                                         | 请求地址的主机名                                           |
    | URL                                                          | 请求资源的位置                                             |
    | Body                                                         | 该请求的大小                                               |
    | Caching                                                      | 请求的缓存过期时间或者缓存控制值                           |
    | Content-Type                                                 | 请求响应的类型                                             |
    | Process                                                      | 发送此请求的进程：进程ID                                   |
    | Comments                                                     | 允许用户为此回话添加备注                                   |
    | Custom                                                       | 允许用户设置自定义值                                       |
    | 图标                                                         | 含义                                                       |
    | ![请求发往服务器](Fiddler抓包.assets/请求发往服务器.png)  | 请求已经发往服务器                                         |
    | ![从服务器下载响应结果](Fiddler抓包.assets/从服务器下载响应结果.png) | 已从服务器下载响应结果                                     |
    | ![请求断点暂停](Fiddler抓包.assets/请求断点暂停.png)     | 请求从断点处暂停                                           |
    | ![响应断点暂停](Fiddler抓包.assets/响应断点暂停.png)     | 响应从断点处暂停                                           |
    | ![请求HEAD方法](Fiddler抓包.assets/请求HEAD方法.png)     | 请求使用 HTTP 的 HEAD 方法，即响应没有内容（Body）         |
    | ![请求POST方法](Fiddler抓包.assets/请求POST方法.png)     | 请求使用 HTTP 的 POST 方法                                 |
    | ![请求CONNECT方法](Fiddler抓包.assets/请求CONNECT方法.png)  | 请求使用 HTTP 的 CONNECT 方法，使用 HTTPS 协议建立连接隧道 |
    | ![响应HTML](Fiddler抓包.assets/响应HTML.png)         | 响应是 HTML 格式                                           |
    | ![响应图片](Fiddler抓包.assets/响应图片.png)         | 响应是一张图片                                             |
    | ![响应脚本](Fiddler抓包.assets/响应脚本.png)         | 响应是脚本格式                                             |
    | ![响应CSS](Fiddler抓包.assets/响应CSS.png)          | 响应是 CSS 格式                                            |
    | ![响应XML](Fiddler抓包.assets/响应XML.png)          | 响应是 XML 格式                                            |
    | ![响应JSON](Fiddler抓包.assets/响应JSON.png)         | 响应是 JSON 格式                                           |
    | ![响应音频](Fiddler抓包.assets/响应音频.png)         | 响应是一个音频文件                                         |
    | ![响应视频](Fiddler抓包.assets/响应视频.png)         | 响应是一个视频文件                                         |
    | ![响应SilverLight](Fiddler抓包.assets/响应SilverLight.png)  | 响应是一个 SilverLight                                     |
    | ![响应FLASH](Fiddler抓包.assets/响应FLASH.png)        | 响应是一个 FLASH                                           |
    | ![响应字体](Fiddler抓包.assets/响应字体.png)         | 响应是一个字体                                             |
    | ![普通响应成功](Fiddler抓包.assets/普通响应成功.png)     | 普通响应成功                                               |
    | ![响应HTTP重定向](Fiddler抓包.assets/响应HTTP重定向.png)   | 响应是 HTTP/300、301、302、303 或 307 重定向               |
    | ![响应HTTP304](Fiddler抓包.assets/响应HTTP304.png)      | 响应是 HTTP/304（无变更）：使用缓存文件                    |
    | ![响应需客户端证书验证](Fiddler抓包.assets/响应需客户端证书验证.png) | 响应需要客户端证书验证                                     |
    | ![服务端错误](Fiddler抓包.assets/服务端错误.png)       | 服务端错误                                                 |
    | ![会话被终止](Fiddler抓包.assets/会话被终止.png)         | 会话被客户端、Fiddler 或者服务端终止                       |

#### 1.2删除请求

- 方法1：点击工具栏中的×，删除请求。
- 方法2：session列表下的黑框QuickExec中输入cls或clear删除请求。
- 快捷键Ctrl+x

#### 1.3过滤请求

- 点击右侧选项卡中的Filters
- 勾选User Filters
- Host Filter选择Show only the following Hosts
- 在下方框中填入想要过滤查看的主机地址，以“;”分隔。
- 点击Actions，选择Run filterset now

#### 1.4抓取HTTPS

默认只抓取HTTP协议的网页，想抓取HTTPS则需要：

- 打开Tools--Options--HTTPS选项卡
- 勾选Capture HTTPS CONNECTs
- 勾选Decrypt HTTPS traffic
- 勾选Ignore server certificate errors(unsafe)忽略证书（如果不安装fiddler证书就如此）

### 2.HTTP请求与响应

![image-20211004021645713](Fiddler抓包.assets/image-20211004021645713.png)

### 3.移动端抓包

- 手机和电脑必须在同一个局域网：
  		1.手机和电脑连同一个WiFi
    		2.手机连WiFi，电脑用网线连接开启这个WiFi的无线路由
    		3.电脑开热点，手机连热点
- 开启fiddler代理，Tools-Options-Connections ， 勾选 Allow remote computers to connect（尽量能勾选的都勾上）， 点击OK
- 查看自己网卡IP
- 在移动端连接wifi，并且设置代理IP（电脑端网卡IP）与端口（8888）
- 移动端访问网页输入代理IP和端口，点击FiddlerRoot certificate下载Fiddler的证书
- 安装证书（安装方式不同设备会有区别，可以自己试探或者上网找教程，如果不能安装显示不能读取证书可以试试去设置里搜索CA证书，验证密码后安装）
- 安装证书成功后，可以用手机访问应用，就可以看到截取到的数据包

### 4.Fiddler内置命令与断点

FIddler断点功能就是将请求截获下来，但是不发送，此时可以做一些更改操作。

- QuickExec命令

| **命令** | **对应请求项** | **介绍**                                                     | **示例**       |
| :------- | :------------- | :----------------------------------------------------------- | :------------- |
| ?        | All            | 问号后边跟一个字符串，可以匹配出包含这个字符串的请求         | ?google        |
| >        | Body           | 大于号后面跟一个数字，可以匹配出请求大小，大于这个数字请求   | >1000          |
| <        | Body           | 小于号跟大于号相反，匹配出请求大小，小于这个数字的请求       | <100           |
| =        | Result         | 等于号后面跟数字，可以匹配HTTP返回码                         | =200           |
| @        | Host           | @后面跟Host，可以匹配域名                                    | @www.baidu.com |
| select   | Content-Type   | select后面跟响应类型，可以匹配到相关的类型                   | select image   |
| cls      | All            | 清空当前所有请求                                             | cls            |
| dump     | All            | 将所有请求打包成saz压缩包，保存到“我的文档\Fiddler2\Captures”目录下 | dump           |
| start    | All            | 开始监听请求                                                 | start          |
| stop     | All            | 停止监听请求                                                 | stop           |

- 断点命令

| **断点命令** |          |                                                         |                                      |
| :----------: | -------- | ------------------------------------------------------- | ------------------------------------ |
|   bpafter    | All      | bpafter后边跟一个字符串，表示中断所有包含该字符串的请求 | bpafter baidu（输入bpafter解除断点） |
|     bpu      | All      | 跟bpafter差不多，只不过这个是收到请求了，中断响应       | bpu baidu（输入bpu解除断点）         |
|     bps      | Result   | 后面跟状态吗，表示中断所有是这个状态码的请求            | bps 200（输入bps解除断点）           |
|  bpv / bpm   | HTTP方法 | 只中断HTTP方法的命令，HTTP方法如POST、GET               | bpv get（输入bpv解除断点）           |
|    g / go    | All      | 放行所有中断下来的请求                                  | g                                    |

### 5.典型应用

- web网页、手机APP抓包

- 修改服务请求与响应

- 前端性能分析及优化

- 模拟弱网测试

## 三、应用场景

- 通过抓包工具截取观察网站的请求信息，更深入了解网站
- 通过用抓包工具截取、观察网站的请求与返回信息，帮助我们进行BUG的定位于描述
- 通过抓包工具拦截修改请求信息，绕过界面的限制，测试服务端的功能

### 1.辅助定位bug

- 抓到HTTP数据包
- 检查请求方式与接口地址是否有误
- 检查返回的响应状态是否正常
- 点击请求的WebForms，检查接口传递参数
- 点击响应的JOSN检查接口返回的响应数据

### 2.构建模拟测试场景

- 模拟发送请求，进行接口测试
  - 应用场景1：需求文档中说明，某个接口限制同一个账号只能请求一次，同一个设备只能请求一次
  - 应用场景2：存在页面输入限制，需要模拟特殊情况请求（例如特殊字符，空格等参数），测试程序处理机制
- Mock接口返回数据，测试程序
  - 应用场景1：需要验证接口数据能否正常处理，但程序处于开发过程中，后台无法对发送请求给出响应
  - 应用场景2：需要验证程序针对404，500，502等不同状态的处理机制

#### 2.1模拟发送请求

- Composer允许自定义请求发送到服务器，可以手动创建一个新的请求，也可以在会话表中，拖拽一个现有的请求
- 点击Composer
- 设置请求方法，请求地址、协议
- 设置请求header
- 设置请求body
- 发送请求
- 查看响应

#### 2.2模拟返回相应数据

- AutoResponder允许拦截指定规则的请求，并返回本地资源或Fiddler资源，从而代替服务器响应。
- 点击AutoResponder
- 选择请求，点击Add Rule添加规则
- Rule Editor中选择响应方式
- Save
- 勾选三个选项
  - Enable rules
  - Unmatched requests passthrough
  - Enable Latency

### 3.模拟弱网环境操作

> 进地铁、上公交、进电梯等，如果app没有对各种网络异常进行兼容处理，那么用户可能在日常生活中遇到APP闪退、ANR、数据丢失等问题。

- 启动模拟调制解调器速度来模拟弱网

  - Rules--Performance--Simulate Modem Speeds

- Customize Rules（Ctrl+R）自定义规则

  - ```js
    if (m_SimulateModem) {
                // Delay sends by 300ms per KB uploaded.
                oSession["request-trickle-delay"] = "300"; 
                // Delay receives by 150ms per KB downloaded.
                oSession["response-trickle-delay"] = "150"; 
            }
    ```
    
  - 在上述函数中用Math.random()方法可以模拟波动的网络

  - ```js
    if (m_SimulateModem) {
        		var t = int(Math.random()*500)
                // Delay sends by 300ms per KB uploaded.
                oSession["request-trickle-delay"] = ""+ ( 2 * t ); 
                // Delay receives by 150ms per KB downloaded.
                oSession["response-trickle-delay"] = "" + t; 
            }
    ```

- 延迟参数

  - | 网络环境                       | 上/下行带宽（kbps） | 上/下行丢包率（%） | 上/下行延迟（ms） | DNS延迟（ms） |          备注          |
    | ------------------------------ | ------------------- | ------------------ | ----------------- | ------------- | :--------------------: |
    | 2G                             | 20/50               | 0/0                | 500/400           | 0             |                        |
    | 3G                             | 330/2000            | 0/0                | 100/100           | 0             |                        |
    | 4G                             | 40000/80000         | 0/0                | 15/10             | 0             |                        |
    | wifi                           | 33000/40000         | 0/0                | 1/1               | 0             |                        |
    | 带宽有限环境                   | 32/32               | 0/0                | 200/100           | 0             |                        |
    | 低丢包率、低时延的环境（上行） | 33000/40000         | 10/0               | 100/100           | 200           | WiFi环境下即可设置测试 |
    | 低丢包率、高时延的环境（上行） | 33000/40000         | 10/0               | 350/350           | 350           |         、、、         |
    | 低丢包率、低时延的环境（下行） | 33000/40000         | 0/10               | 100/100           | 200           |         、、、         |
    | 低丢包率、高时延的环境（下行） | 33000/40000         | 0/10               | 350/350           | 350           |         、、、         |
    | 低丢包率、低时延的环境         | 33000/40000         | 10/10              | 100/100           | 200           |         、、、         |
    | 低丢包率、高时延的环境         | 33000/40000         | 10/10              | 350/350           | 350           |         、、、         |
    | 高丢包率的环境（上行）         | 33000/40000         | 90/0               | 100/100           | 200           |         、、、         |
    | 高丢包率的环境（下行）         | 33000/40000         | 0/90               | 100/100           | 200           |         、、、         |
    | 高丢包率的环境                 | 33000/40000         | 90/90              | 100/100           | 200           |         、、、         |
    | 网络超时（响应）               | 33000/40000         | 0/100              | 100/100           | 200           |         、、、         |
    | 网络超时（请求）               | 33000/40000         | 100/0              | 100/100           | 200           |         、、、         |
    | 网络超时（完全丢包）           | 33000/40000         | 100/100            | 100/100           | 200           |         、、、         |
    | 无网（飞行模式或关闭网络）     |                     |                    |                   |               |                        |

### 4.前端性能分析及优化

- 选中想查看的session列表
- 点击Statistics进行请求的性能数据分析
- 点击Collapse Chart即可查看所用语言的所占比
- 点击Timeline即可查看页面各个元素的加载时间和顺序





## 问题解决

### Q1.Fiddler启动后Chrome浏览器无法浏览网页？

1. 打开Tools--Options--HTTPS选项卡；
2. 点击Actions下拉选择Trust Root Certificate，弹框选yes，弹框选是（到这一步可能就解决了）；
3. 点击Actions下拉选择Export Root Certificate to Desktop，将fiddler证书导出到桌面；
4. 打开谷歌浏览器，设置--高级--安全--管理证书；
5. 导入证书
6. 重启浏览器与fiddler。

### Q2.如何屏蔽抓取特定端口？

在Fiddler中使用它，用Ctrl+R打开自定义规则，然后添加到OnBeforeRequest。

```js
if (oSession.host=="localhost:9090"){
    oSession["ui-hide"] = "true";
}
```

