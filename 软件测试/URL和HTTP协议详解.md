# URL&HTTP协议详解

- URL：统一资源定位符。这就意味着我们可以通过URL的方式去访问的资源（接口）。
- URI：统一资源标识符。是一种抽象的概念，本身没有具体去实现。

## 一、URL

URL是实现接口访问的第一步，一般来说，一个URL是分为五个部分。
	**protocol、domain、port、path、url parameters**
示例：
	https://www.bilibili.com/video/BV1vM4y1V78M?p=5

- protocol：协议，就是指url中://之前的部分。
  - 协议：是指通信双方对于通信过程中的数据、数据组织格式、规程、含义等等所作的约定。
  - 一般来说，按照TCP/IP模型，不同的层有不同的协议。
  - 接口测试一般来说是从应用层的协议着手去模拟实现接口请求和访问的。
  - 常见的应用层的协议有:
    - http
    - https      http+ssl
    - ssh
    - ftp
    - smtp
    - pop3
    - mysql
    - oracle
    - MS SQL

- domain：域名，是指要访问的服务器的地址。可以是服务器的域名，ip地址，机器名。

- port：端口，是由服务器提供的，用来监听客户端的请求。
  
  - 格式：domain:port。
  
  - 如果服务器所设置的监听端口和其应用所采用的通信协议是默认的对应关系，则用户在通过URL来访问时，可以省略端口。
  - 常见的协议及其默认的通信端口对应关系：
    - http	80
    - https	443 or 8443
    - ftp	21
    - ssh	22
    - smtp	25
    - pop3	110
    - oracle 1521
    - mysql	3306
    - MS SQL	 1433

- path：路径，是要访问的资源在服务器的容器路径下的相对地址。
  - 一般来说，路径是和要访问的接口直接相关。
- URL parameters：URL地址参数，通常是以问号？作为连接符拼接在path之后。
  - 在很多工具中，url地址参数是直接划分在path中的。
  - url地址参数是键值对应的，即key=value的格式，多个键值之间使用&作为连接符。

## 二、HTTP协议

### 2.1HTTP

- http协议详解：http协议叫HypeText Transfer Protocol，超文本传输协议。
- http协议的特点：
  - http协议是一种基于request（请求）和response（响应）的协议。
  - http协议是一种简单、灵活的协议。
  - http协议是一种快速的协议。
    - http1.0及0.9版本，http协议默认是一种面向短连接的协议。
    - http1.1开始，http协议默认是一种面向长连接的协议。
    - 短连接：一个tcp连接上只能建立一个http连接，http结束之后，tcp连接也释放结束。
    - 长连接：一个tcp连接上可以建立多个http连接。
      - 这个是通过信息头：Connection来实现的。keep-alive就表示是长连接。
  - http协议是一种无状态的协议。
- http协议的详细构成：
  - http协议包含两个部分：http request、http response。
    - http request：http请求，影响的是脚本的实现。
    - http response：http响应，影响的是脚本的增强处理

> ​	抓包工具很多，但是从实现接口测试的角度来说，我们去查看所抓取的数据包，建议大家通过raw或者source的视图模式去查看数据。
> ​	不要用抓包工具所提供的各种数据解析视图去看。

### 2.2HTTP Request

- http request：是由三个部分构成:request lin、request headers、 request body。
- request line：请求行，是指请求数据包中的第一行内容，
  	示例：GET /phpwind/ HTTP/1.1
  - 通常包含以下信息：
    	request method、 request path、 protocol/version
  - request method：请求方法，所有的http请求都必须指定请求方法，如果没有指定，则默认使用get方法。
    - 常见的请求方法有：get、post、put、patch、delete、options、header、trace等。
    - 请求方法具体使用哪种，不是测试人员决定的，而是由接口本身决定。
      - 接口文档
      - 抓包
  - request path：请求路径，就是指URL中的path和url地址参数两个部分。
  - protocol/version：协议/版本。
- request headers：请求头，是指从请求数据包中的第二行到第一个空行之前的部分。
  - 请求头是客户端用来和服务器进行通信信息、控制信息等交互的。
  - 一般来说和业务逻辑无关（除了状态类的信息头）。
  - 信息头是键值对应的。
  - 信息头的类型是由协议规定的，不同的信息头具有不同的作用。
  - 对于接口测试而言，一般来说需要重点关注的信息头有：
    - User-Agent：简称UA，是客户端用来告知服务器，客户端的一些配置信息。服务器往往就是通过该信息头来判断“用户”是不是同一个用户。一般作为全局信息头使用。
    - Content-Type：该信息头是客户端用来告知服务器，客户端向服务器所发送的请求body中的数据的数据组织格式。
      - Content-Type的值要求和实际发送的数据格式保持一致。
  - 状态有关的头：
    - token
    - author

- request body：请求主体，是指从请求数据包中的第一个空行之后的所有内容。
  - 一般来说，get方法发送的数据位于url地址参数，反之放在url地址参数中的数据，服务器认为是通过get方法发送的。
  - post方法发送的数据一般是位于请求主体中。
  - 请求主体中的数据组织格式是由接口本身决定的。一旦请求主体有数据，则信息头中一定要指定Content-Type。

### 2.3HTTP Response

- http response：http响应，也是由三个部分构成：response line、response headers、response body

- response line：响应行，是指响应数据包中的第一行内容。
  	示例：HTTP/1.1 200 OK

  - 包含以下信息：
    		protocol/version、response code、response message。

  - response code：响应代码，又叫状态码（Status）。是服务器用来告知客户端，服务器对于请求的处理状态。

    - 响应代码给出的只是通信层面的处理状态。

    - 业务的成功是建立在通信成功的基础之上。

    - 状态码是三位长度的数字，根据首位数字不同，可以分为5类：

      - 1xx：表示连接建立过程中双方的通信控制信息。

      - 2xx：表示服务器处理成功。

      - 3xx：表示重定向。

      - > 一般来说，1xx、2xx、3xx都表示通信是成功的。

      - 4xx：表示客户端错误。

      - 5xx：表示服务器错误。

      - > 对于接口测试脚本而言，一旦出现4xx、5xx都表示脚本不成功。而且绝大多数情况下，都是脚本本身数据组装有误导致。

- response headers：响应头，是服务器返回给客户端的。
  - 可能会有服务器返回的一些状态有关的信息头需要关联处理。

- response body：响应主体，是指响应数据包中的第一个空行之后的所有内容。
  - 响应主体就是服务器对于请求的处理结果。
  - 要去判断请求是否成功，要去进行数据关联，很多时候都是和响应主体。