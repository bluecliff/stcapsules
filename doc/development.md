# 需求分析

私密社交的兴起，不同于微博的社交方式。


# 概要设计

时空胶囊主要包括两个部分，android客户端和服务器端。android客户端是用户直接接触的部分，实现用户浏览，发表，评论胶囊的功能。
服务器端主要为客户端提供数据支持，用户从客户端提交的数据最终由服务器端进行处理后保存在数据库中，同时服务器端也为客户端
提供处理后的数据浏览支持，查询支持。

客户端包括浏览胶囊，发表胶囊，评论胶囊三个模块。其中浏览包括各种条件的查询组合浏览等。

服务器端包括三大模块：View模块，完成为前端提供restful API的功能;Controller模块,处理业务逻辑，数据处理功能;Model模块，完成
数据库存储功能。

通信设计，采用http协议通信，使用restful接口技术设计通信接口。

# 详细设计

## 客户端设计

### 技术方案

phonegap4.1。。。。

### 功能模块

浏览，地图模式，文本模式。。。
查询。。。
发表。。。相机，录音。。(设计方案大胆写)
评论。。。
通信模块：与后端的通信

### UI设计

。。。。

## 服务端设计

### 技术方案

采用python Flask框架作为web开发框架，采用Mongodb作为数据库。python使用cpython 2.7版本，Flask使用最新的0.10版,mongodb使用最新的
2.6.3版。

### 功能模块

- view模块，对Flask开发框架提供的viewmethod类进行封装，实现权限验证，身份鉴别，重载POST,GET,PUT,DELETE方法。对应API模块进行view
    函数设计
- model模块，数据库交互模块采用mongoengine这一ORC方案，确保安全。数据模型包括User,Post,Comment三个模块，分别对应用户，胶囊，评论。
- contorller模式，完成数据处理，增删改查数据库，为view函数提供数据操作，隔离view和model的直接耦合。
- Test模块，完成单元测试，测试每个view函数，每个数据库读写函数。
- API模块，对应的符合restful设计最佳实践的api对应到相应的view函数上。包括以下API:
    + '/api/login/'     登录接口
    + '/api/post/<string:post_id>/'     获取胶囊接口
    + '/api/posts/'                     获取胶囊列表，发表胶囊接口
    + '/api/comments/<string:post_id>/' 获取评论，发表评论接口
    + '/api/favs/'                      获取用户收藏胶囊列表
    + '/api/receives/'                  获取用户收到的定向胶囊接口
    + '/api/rs/'                        获取资源上传权限token
    + '/api/key/'                       获取资源ID接口

# 部署说明

服务器端程序以web应用的形式部署在百度云BAE平台上，数据库使用BAE提供的mongodb作为生产用数据库。服务器选用1G内存，单核版本，初期
满足需求，后期根据服务器压力做调整。

资源存储服务器选择使用七牛云存储，永久存储图片，录音等静态资源。

部署过程如下：
1 创建BAE web应用，获取到BAE应用的name和key，在代码中的config.py中配置这两个属性。
2 创建BAE mongodb数据库，获取到数据库名和密码，接口，主机地址等，在代码中的config.py中做配置。
3 创建七牛云存储仓库，获取到name和key，在代码中的config.py中做好配置。
4 获取bae web应用的代码仓库的地址，用git上传代码仓库到bae应用下。
5 点击BAE应用的发布按钮。
6 按照BAE文档给新建BAE映射绑定自己的域名。
7 测试。
