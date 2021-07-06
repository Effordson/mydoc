# **安装VS Code**

0. 简介

微软开发的，免费开源的通用的集成开发环境（IDE），属于图形界面的IDE，运行于Windows、MacOS、Linux操作系统，可以安装相关的插件，用于各种语言的开发，例如：C、C++、JAVA、Python、Go等等。

1. 下载安装

官网地址：https://code.visualstudio.com

2. 基本配置

所有的配置都可以通过快捷键：Ctrl+Shift+P修改，通过搜索相关的配置做修改。

1）设置中文界面

Ctrl+Shift+P，搜索language，安装中文语言包，重启生效；



# **几个基本概念**

1. 工作空间：workspace

可以把一个工程或者几个工程放到一个工作空间，拥有相同的配置，即一个虚拟环境

2. 设置：settings(用户、工作区)

可以配置相关的环境

可以通过文件-》首选项-》设置、文件图标、键盘映射、颜色主题等修改相关配置

注意：

进入设置会有两块：用户、工作区

用户是针对当前Windows用户所有的工作区生效

工作区是针对当前工作区（文件夹）有效。对工作区进行配置修改，会在工作区下面生成一个配置文件

![img](http://images.local168.com/img/clipboard.png)

工作区：

默认一个文件夹（一个项目）相当于一个工作区，如果想把多个文件夹加入一个工作区，可以通过 文件-》将文件夹加入工作区，然后保存工作区，以后就可以通过打开工作区来打开当前加入工作区的多个文件夹，一次性只能打开一个工作区

3. 插件：plugins

即用于程序开发的扩展插件，便于快速开发，所有的扩展插件都是安装在用户目录下的隐藏文件夹.vscode中

![image-20210707020254122](http://images.local168.com/img/image-20210707020254122.png)

**注意：**

安装的插件虽然在用户目录下，但是你可以根据你的工作需求启用或者禁用插件，一方面可以减少内存消耗，还可以针对不同编程语言做个性化设置。



# **安装Python扩展插件**

Ctrl+Shift+P，搜索 欢迎 ，即可进入欢迎页面，点击安装Python插件(Python开发大礼包)：包括Linting, Debugging (multi-threaded, remote), Intellisense, Jupyter Notebooks, code formatting, refactoring, unit tests, snippets, and more.

![image-20210707020339264](http://images.local168.com/img/image-20210707020339264.png)

Tips：扩展插件属于VS Code的插件，与Python的模块区分开来。



# **配置pip镜像源**

1. 安装一个Python模块

1）Python -m pip install 模块名（卸载uninstall）

2）pip install 模块名（pip可执行命名需要添加到path环境变量中）

2. 指定镜像源安装

pip install -i http://mirrors.aliyun.com/pypi/simple/ 模块名

3. 配置默认镜像源

Linux系统：

```
a. 找到下列文件
~/.pip/pip.conf

b. 在上述文件中添加或修改:
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```

Windows系统：

```
a. 新建文件夹
C:\Users\star\pip

b. 添加文件：pip.ini
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
```

4. pip查看

查看已安装的包：pip list 

查看默认的镜像源：pip config list 

命令行修改默认源：

修改前建议更新pip版本到最新，pip install --upgrade pip -i + 临时源

pip config set global.index-url + 源地址



# **Python快速编程插件**

0）好用的主题插件：One Dark Pro、Brackets Light Pro

1）安装了扩展插件之后，会有补全提示，扩展插件中搜索Python

2）鼠标放在函数上面会有函数的使用介绍

3）函数，右键转到定义处，可以看到源函数的定义。

​	Python有的函数是调用c库中的二进制函数，看不到源代码，如果是Python写的就能看到

4）变量，右键也可以转到变量的定义处

5）多窗口显示，水平拆分右上角左键点击，垂直拆分Alt+左键

6）安装python扩展包tabout,使用tab键跳出引号或括号

7）安装扩展包rope，在代码编辑框中选中多行可以提取出来变成一个函数

8）重命名符号(即变量名、方法名、类名等等)，代码重构特别实用：修改这个项目中所有的这个符号名称。很智能好用，会修改所有文件调用处和定义处的名称

![image-20210707020428299](http://images.local168.com/img/image-20210707020428299.png)

9）使用shippet(代码片段)：默认有很多代码片段，例如：for、while、class、try...except、def

用户代码片段存放文件：C:\Users\star\AppData\Roaming\Code\User\snippets\python.json

1. 文件-》首选项-》用户片段，可以新建全局、工作空间、Python语言代码片段

2. Ctrl+Shift+P，搜索用户片段

参考示例：

![image-20210707020507558](http://images.local168.com/img/image-20210707020507558.png)

10）快速修改多行：

Alt + 鼠标左键，可以分开点选多行

Ctrl+Alt+上下键选择多行编辑

11）Markdown文件中显示网络图片方法：Ctrl+Shitf+P--》更改预览安全设置--》允许不安全的本地内容，网络图片可以通过PicGo上传到七牛云获取网络链接，然后粘贴到Markdown文件中

![image-20210707020533353](http://images.local168.com/img/image-20210707020533353.png)

​	如果是本地图片，需要在设置为相对路径。可以在项目下找到文件，右键快速复制路径



# **调试：断点、内存变量、堆栈、单步**

可以调试Python文件、模块、web框架（Django、Flask）、调用远程debug服务器等。

运行->启动调试，或者F5执行调试开始

调试5个功能键：

![image-20210707020556990](http://images.local168.com/img/image-20210707020556990.png)

6个小点：用于移动调试按键的位置

调试：执行到下一个断点

单步跳过：如果断点是函数，不会进入函数内部

单步调试：如果断点是函数，进入函数内部

单步跳出：跳出函数

停止：退出调试模式

![image-20210707020633262](http://images.local168.com/img/image-20210707020633262.png)

**变量：**可以查看所有的特殊变量（整个Python文件有效的，如：__name__ __doc__ __file__)、全局变量（变量、函数、类等）、函数局部变量（函数内部的变量、内部函数、特殊变量）

**监视：**可以添加监视的变量，会实时根据程序运行变化，这个变量是当前堆栈的，如上面的i，如果跳出game函数，i就无效了。可以监视全局变量、局部变量（game的i值），还可以对变量使用函数功能（如字符串.split)查看结果。

**调用堆栈**：可以查看堆栈的情况，目前进入game函数内部，module被压入栈，如果game还有内部函数，那么game也会被压入栈。

**断点：**可以查看当前工作空间内的所有断点。可以新增、删除、停用。



# **配置虚拟环境**

管理多个Python环境、给不用的项目使用不同的环境

有哪些虚拟环境：virtualenv，pyenv，venv

在终端中运行配置命令：python -m venv venv_vs1,则在项目下会生成虚拟环境文件夹，项目下D:\VScode_work\vs1\.vscode\settings.json文件也会修改python环境变量：

"python.pythonPath": "venv_vs1\\Scripts\\python.exe"

![image-20210707020743308](http://images.local168.com/img/image-20210707020743308.png)



# **更多扩展插件**

1. better comments

```
多种注释颜色
# ? 注释颜色 --蓝色
# ! 注释颜色 --红色
# * 注释颜色 --浅蓝色
# 注释颜色 --灰色
# TODO 注释颜色 --黄色
对于使用3引号的多行注释同样有效，行前需添加？ ！ *等
```

​	对于使用3引号的多行注释同样有效，行前需添加？ ！ *等

2. vscode-icons:图标颜色

3. python indent:更加完美好看的代码缩进

4. markdown shortcuts:非常好用的插件，很多快捷键，插件介绍有说明，除了插入图片，啥都行。

![image-20210707020812524](http://images.local168.com/img/image-20210707020812524.png)

5. Markdown Snippets：可以快速的插入表格、任务列表等

![image-20210707020832245](http://images.local168.com/img/image-20210707020832245.png)

6. Snippets Ranger：查看代码片段工具，能查看所有代码片段，python、JAVA、Markdown等等，使用方法Ctrl+shift+P，搜索Snippets Ranger，就可以选择查看你想看的语言代码片段

![image-20210707020857115](http://images.local168.com/img/image-20210707020857115.png)

7. indent-rainbow:多个缩进以不同颜色进行高亮显示

8. Bracket Pair Colorizer:括号高亮的效果，尤其是多组嵌套括号。

9. Drawio：http://draw.io是一个支持在线绘图的网站工具，在 VSCode 中已经包含此插件

**vscode-drawio**可以编辑，**Draw.io Integration**可以编辑或导出流程图为图片、svg、drawio格式

10. TODO Tree：某块代码需要修改或标记，后续可以快速定位

11. Markdown Editor：安装后创建md文件，右键文件选择此软件打开，使用还比较方便







