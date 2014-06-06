# stcapusule apc document

## User API
- /api/login/

登录接口，用post方法提交登录数据，登录数据只有一个参数：user_id，为客户端通过OAUTH
从新浪微博，腾讯微博获取得到的id号。

返回json格式的数据:

```
{
    "favourites": 0,
    "id": "538e94d5809cb81362fb4b93",
    "user_id": "12345673"
}
```

favourites字段是用户收藏的胶囊数目，id是用户的唯一标识，user_id是用户的微博id。

## Favourites API
- /api/favs/

  + GET方法，获取当前用户的收藏列表，返回json格式数据。
  + POST方法，增加一个收藏。POST提交数据包括一个post_id，值为要收藏的胶囊的ID。
  + DELETE方法，删除一个收藏。提交数据包括一个post_id,值为要删除的收藏的胶囊ID。

## Post API

- /api/posts/

  + GET方法，获取当前用户可见的胶囊列表，返回Json个数数据。

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
    + imageurl: 图片链接，可选，形式待定
    + waveurl: 声音链接，可选，形式待定
    + receivers: 在类型为1时的必填选项，值为发送目标的微博ID

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
