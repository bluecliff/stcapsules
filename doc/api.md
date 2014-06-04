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

  + POST方法，当前用户增加一条胶囊纪录，POST参数包括：

    + longitude:
    + latitude:
    + distance:
    + active_time:
    + permission:
    + content:
    + imageurl:
    + waveurl:

- /api/post/<postid>/

    + GET方法，获取当前用户可见的某一个胶囊的具体信息，postid为get参数，值为要获取的胶囊
      的ID
