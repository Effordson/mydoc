# git客户端连接服务器的2种方式

git的使用这里不再赘述，此篇文章与代理相关。全文简易干货

git客户端与代码服务器(github、gitlab、Gerrit等)创建连接有2种方式：https和ssh

连接之前需要配置本地账户及邮箱，例如：

```
git config --global user.name "effordson"
git config --global user.email "your-email@qq.com"
```

**https连接**

下载代码示例：

```
git clone https://github.com/Effordson/mydoc.git
```

**ssh连接**

需要使用ssh-keygen先创建密钥对，再上传公钥到代码服务器

下载代码示例：

```
git clone git@github.com:Effordson/mydoc.git
```



## git config配置生效范围

通过命令git config -h可以查看帮助，设置生效范围有：

```
usage: git config [options]

Config file location
    --global              use global config file
    --system              use system config file
    --local               use repository config file
    -f, --file <file>     use given config file
    --blob <blob-id>      read config from given blob object
```

配置含义解释：
global 即是读/写当前用户全局的配置文件(~/.gitconfig 文件，属于某个计算机用户)
system 即是读写系统全局的配置文件(/etc/gitconfig 文件，属于计算机)
local 即是当前 clone 仓库 的配置文件(位于 clone 仓库下 .git/config)。



# 通过代理服务器https连接

目前还没有实现ssh连接，通过代理服务器访问代码仓库，以下是https连接配置代理。

## 配置https代理服务器

**前提：**git下载代码方式是https连接，需要配置squid或者其他的代理服务器

**适用范围：**Windows和Linux

配置https代理，没有身份验证代理：

```
git config --global https.proxy https://139.198.116.112:3128
git config --global http.proxy http://139.198.116.112:3128  # http的不配亦可
```

查看全局配置：~/.gitconfig

```
[root@module ~]#git config --list 
user.name=effordson
user.email=your-email@qq.com
https.proxy=https://139.198.116.112:3128 # 代理服务器IP和端口，当前使用的是squid代理
http.proxy=http://139.198.116.112:3128
```

如果代理服务器是需要身份验证的，需要配置账户密码，配置http/https代理原型：

```
git config --global http.proxy http[s]://userName:password@proxyaddress:port
```

身份验证代理配置实例：

```
[root@module ~]#cat .gitconfig 
[user]
	name = effordson
	email = your-email@qq.com
[https]
	proxy = https://username:password@139.198.116.112:3128
[http]
	proxy = http://username:password@139.198.116.112:3128
```

## 取消https代理设置

直接删除代理配置或者通过命令删除：

```
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## https免密码提交设置

一共有2种方式免密push，一种是在下载仓库的时候设置账号密码，二是添加凭据

### 预设账号密码

1、https方式，指定用户名和密码，git clone时指定：

```
git clone http://user:passwd@x.x.x.x/project.git
```

2、如果早就clone了项目，则重新设置一下remote url，具体命令：

```
git remote -v #可以查看目前的url
git remote set-url origin http://user:passwd@x.x.x.x/project.git
```

默认是添加了凭据的，如果需要删除用户登录认证信息，需要重设url，并删除用户的凭据：

```
# 针对系统
git config --system --unset credential.helper
# 针对当前用户
git config --global --unset credential.helper
# 针对当前仓库
git config --unset credential.helper
```



### 在Windows中添加凭据

目前知道有2种凭据：manager和store

**manager凭据**

配置credential.helper： 
首先简单介绍一下credential.helper这个配置项的含义：这个配置项允许用户自行指定git所使用的凭据管理工具。 
简单粗暴的办法就是直接配置credential.helper的值为manager（注意：当你需要在同一台机器上使用多个git账号这么搞就不行了，因为2个账号必定使用的不同的凭据），**凭据的类型可以在git的配置文件种指定，优先级:仓库git配置>用户git配置>系统git配置**

```
# 如果在仓库种，只针对当前仓库
git config credential.helper manager

# 针对当前的账户(系统用户家目录的配置)
git config --global credential.helper manager
```

再次尝试pull代码的时候会弹出窗口要求输入用户名密码（只需要输入这一次就ok了）：

最后再次pull代码检查一下是否已经可以不用输入用户名密码了。



默认配置了凭据，如果需要删除用户的凭据

```
# 针对系统
git config --system --unset credential.helper
# 针对当前用户
git config --global --unset credential.helper
# 针对当前仓库
git config --unset credential.helper
```



**store凭据**

store凭据默认为：~/.git-credentials，也可以在配置的时候指定文件

添加凭据文件

```
vim ~/.git-credentials

# 保存以下内容 
https://{username}:{passwd}@github.com/Effordson/mydoc.git
```

为仓库设置凭据

```
# 只设置当前仓库
git config credential.helper store
# 全局配置
git config --global credential.helper store
```

以上是默认文件位置的，也可以指定文件

```
git config credential.helper store --file .git/.my-credentials
```



# 通过https端口创建ssh连接github服务器

**Linux和Windows都可以使用此方法**

**ssh客户端配置文件**
全局配置文件：/etc/ssh/ssh_config
用户配置文件：~/.ssh/config ，默认没有需手动创建

## 在 HTTPS 端口使用 SSH

**来自GitHub官方文档：**https://docs.github.com/cn/github/authenticating-to-github/troubleshooting-ssh/using-ssh-over-the-https-port

有时，防火墙会完全拒绝允许 SSH 连接。 如果无法选择使用具有凭据缓存的 HTTPS 克隆，您可以尝试使用通过 HTTPS 端口建立的 SSH 连接克隆。 大多数防火墙规则应允许此操作，但代理服务器可能会干扰。

GitHub Enterprise Server 用户：目前不支持经 SSH 通过 HTTPS 端口访问 GitHub Enterprise Server。

要测试通过 HTTPS 端口的 SSH 是否可行，请运行以下 SSH 命令：

```
$ ssh -T -p 443 git@ssh.github.com

Hi username! You've successfully authenticated, but GitHub does not
provide shell access.
```

如果这样有效，万事大吉！ 如果无效，您可能需要遵循我们的故障排除指南。

**故障排除指南：**https://docs.github.com/cn/github/authenticating-to-github/troubleshooting-ssh/error-permission-denied-publickey



**启用通过 HTTPS 的 SSH 连接**
如果您能在端口 443 上通过 SSH 连接到 git@ssh.github.com，则可以覆盖您的 SSH 设置以强制与 GitHub 的任何连接均通过该服务器和端口运行。

要在您的 ssh 配置中设置此项，编辑位于 ~/.ssh/config 的文件，添加以下部分：

```
Host github.com
  Hostname ssh.github.com
  Port 443
  User git
```


您可以通过再次连接到 GitHub 测试此项是否有效：

```
$ ssh -T git@github.com

Hi username! You've successfully authenticated, but GitHub does not
provide shell access.
```

没有以上配置数据包格式：github.com的IP+{ssh数据包+22端口}

使用以上配置后数据包格式：ssh.github.com的IP+{ssh数据包+443端口}



## 使用SSH下载代码仓库

```
git clone git@github.com:Effordson/mydoc.git
```

查看网络连接：

```
[root@module t2]#netstat -ant 
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN     
tcp        0     52 192.168.31.200:22       192.168.31.54:50280     ESTABLISHED
tcp        0      0 192.168.31.200:22       192.168.31.54:55125     ESTABLISHED
tcp        0      0 192.168.31.200:42812    18.141.90.153:443       TIME_WAIT
最后一条即为刚才连接GitHub仓库的网络连接
```







