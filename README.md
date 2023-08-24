# dailyview-api

專案介紹：
- 環境建置使用 docker-compose
- 此專案包含對熱門文章進行 CRUD 的 APIs
- 使用 JWT 認證

專案需求：
- Django 3.2
- djangorestframework 3.12.4,< 3.13
- psycopg2-binary >= 2.9 ,< 2.9.3
- drf-spectacular >= 0.15.1 ,< 0.16
- drf-jwt
- pillow

<h4><b>運行步驟</b></h4>

複製專案：
```
git clone git@github.com:billybboy/dailyview-api.git
```
建立 docker image：
```
docker-compose build
```
執行專案：
```
docker-compose up
```
<h4><b>專案畫面</b></h4>

![](https://upload.cc/i1/2023/08/24/3bdO2Y.jpg)
