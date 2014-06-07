# stcapusule api document

## User API
- /api/login/

登录接口，用post方法提交登录数据，登录数据只有一个参数：user_id，为客户端通过OAUTH
从新浪微博，腾讯微博获取得到的id号。

返回json格式的数据:

```
{
    "favourites": 0,
    "id": 317970455,
    "receives": 0,
}
```

favourites字段是用户收藏的胶囊数目，receives是用户收到的胶囊数目，user_id是用户的微博id。

** 若id为null则登录出错 **

## Favourites API
- /api/favs/

  + GET方法，获取当前用户的收藏列表，返回json格式数据。可带有start和end参数获取end-start条胶囊
    如/api/favs/?start=0&end=12获取前12条收藏。返回json列表，是每个收藏的信息。如下所示：

    ```
    [
    {
        "active_time": "Sat, 23 May 1970 21:21:18 -0000",
        "author": "3179705582",
        "category": 3,
        "followers": 1,
        "id": "53913dd5809cb80b461b09d5",
        "location": [
            120,
            140
        ],
        "title": "Test"
    },
    {
        "active_time": "Sat, 23 May 1970 21:21:18 -0000",
        "author": "3179705582",
        "category": 2,
        "followers": 1,
        "id": "53912798809cb8082cba3dd4",
        "location": [
            120,
            140
        ],
        "title": "Test"
    }
    ]
    ```
    
  + POST方法，增加一个收藏。POST提交数据包括一个post_id，值为要收藏的胶囊的ID。返回更新后的收藏列表的前10条。数据格式同上。
  + DELETE方法，删除一个收藏。提交数据包括一个post_id,值为要删除的收藏的胶囊ID。返回更新后的收藏列表的前10条，数据格式同上。

## Receive API

- /api/receives/

  + GET方法，获取当前用户收到的胶囊列表，返回json格式数据，可带start,end参数，如/api/receives/?start=0&end=10,将获取前10条。
    数据格式和favourites API返回数据格式相同。

## Post API

- /api/posts/

  + GET方法，获取当前用户可见的胶囊列表，返回Json格式数据。

      /api/posts/?latitude=140&longitude=120
    ```
    [
    {
        "active_time": "Sat, 23 May 1970 21:21:18 -0000",
        "author": "3179705582",
        "category": 2,
        "followers": 0,
        "id": "53912798809cb8082cba3dd4",
        "location": [
            120,
            140
        ],
        "title": "Test"
    },
    {
        "active_time": "Sat, 23 May 1970 21:21:18 -0000",
        "author": "3179705582",
        "category": 3,
        "followers": 0,
        "id": "5391279d809cb8082cba3dd5",
        "location": [
            120,
            140
        ],
        "title": "Test"
    }
    ]
    ```

  + POST方法，当前用户增加一条胶囊纪录，POST参数包括：

    + longitude: 经度，浮点数，由手机传感器获取
    + latitude: 维度，浮点数，由手机传感器获取
    + distance: 距离，指定该胶囊的可见范围，整数，用户由单选框输入，上传值为0,1,2,3四个整数之一，分别代表由近及远的距离。
    + active_time: 胶囊激活时间，unix时间戳
    + category: 胶囊的类型，值为整数0,1,2,3之一，分别代表公开可见，发给好友，私密胶囊，广告彩蛋四大类型。由用户单选框输入。
    + title: 胶囊的标题
    + content: 胶囊内容，用户输入，文本类型
    + imagekey: 图片的唯一标识，可选，使用md5
    + wavekey: 声音的唯一标识，可选，使用md5
    + receivers: 在类型为1时的必填选项，值为发送目标的微博ID

    上面的可选参数表示该参数可以有可以没有，没有的时候即默认的胶囊没有这一属性。

    返回为该新增胶囊的信息，json格式：
    ```
    {
        "active_time": "Sat, 23 May 1970 21:21:18 -0000",
        "author": "3179705582",
        "category": 3,
        "followers": 0,
        "id": "539145d4809cb8116d5d832c",
        "location": [
        120,
        140
        ],
        "title": "Test"
    }
    ```

    具体的增加胶囊的过程为:

    1. 若用户增加图片或者声音属性，则用户每增加一个文件客户端需要访问一次 GET /api/key/，获得一个标识唯一文件的key。
    2. 用户点击提交按钮后，客户端需要首先访问 GET /api/rs/ 获得一个上传凭证uptoken。
    3. 用户上传文件，POST http://http://up.qiniu.com/ 上传文件时必须带有上面获得的uptoken参数和key参数,：
        ```
           <form method="post" action="http://up.qiniu.com/" enctype="multipart/form-data">
                <input name="key" type="hidden" value="<key>">
                <input name="x:<custom_name>" type="hidden" value="<custom_value>">
                <input name="token" type="hidden" value="<uptoken>">
                <input name="file" type="file" />
           </form>
        ```
       上面的x开头的参数是可选的参数，可有可无。注意：每一个文件都需要单独的一个form表单，所以有多个文件时需要构造多个表单       。这些
       表单的key不同，但uptoken可相同。uptoken目前的有效期是1小时。

    4. 文件上传成功后，返回200状态码，以及json格式的数据：{"hash":"Fi8WaVIin41pPc0YGf55rk9WGvYg","key":"123458","x:username":""}
    5. 开始向/api/posts/接口提交数据，数据格式如上文所示。其中imagekey和wavekey分别对应上传文件时使用的key，此外文件上传成功后
       返回的json数据中也有key，和之前的key是一样的。
    6. 创建新的胶囊完成。

- /api/post/\<postid\>/

    + GET方法，获取当前用户可见的某一个胶囊的具体信息，postid为get参数，值为要获取的胶囊
      的ID

    /api/post/53913dd5809cb80b461b09d5/
    ```
    {
        "active_time": "Sat, 23 May 1970 21:21:18 -0000",
        "author": "3179705582",
        "category": 3,
        "content": "test capusuls test capusulstest capusulstest capusulstest capusulstest capusulstest capusuls",
        "followers": 0,
        "id": "53913dd5809cb80b461b09d5",
        "imageurl": "http://www.url1.com",
        "location": [
            120,
            140
        ],
        "title": "Test",
        "waveurl": "http://www.url2.com"
    }
    ```

## Comment API

- /api/comments/\<postid\>/

    + GET方法，获取对应胶囊的评论列表，可附带get参数start和end，标识获取的数目，如/api/comments/53913dd5809cb80b461b09d5/?start=10&end=20
      将获取到该胶囊的第10到20条评论。返回json格式数据。
      ```
      [
        {
            "author": "3179705582",
            "content": "Test comment6",
            "created_at": "Fri, 06 Jun 2014 09:36:19 -0000"
        },
        {
            "author": "3179705582",
            "content": "Test comment7",
            "created_at": "Fri, 06 Jun 2014 09:36:19 -0000"
        },
      ]
      ```

    + POST方法，向对应的postid的胶囊增加一条评论，POST方法需要提交的参数有:
      - content 评论内容，为字符串格式。

      返回json格式，为新的评论列表，默认前10条。格式同上
