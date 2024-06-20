# learnDjango

## 创建项目

- 本地安装django：python -m pip install django
- 安装后本地目录格式如下
c:\Python311

- python.exe
- Script
  - pip.exe
  - flask.exe
  - django-admin.exe(创建django的工具)
  - ...
- Lib
  - 内置模块
  - site-packages(第三方模块)
    - flask
    - django(框架源码)
    - ...
- ...

### 方式一（命令行）

- 进入目录使用命令行创建
![Alt text](/Dashboard/static/img/Django/django安装1.png)

### 方式二（Pycharm）

- 选择Django项目并使用本地解释器
- 删掉templates目录和红框中的内容
![Alt text](/Dashboard/static/img/Django/django安装3.png)

### 创建APP

- 一个项目可有多个app，比如网站，后台管理，API，每个APP有独立的表结构，函数，模板，CSS
- 终端:python manage.py startapp Dashboard

```{.py}
# 目录结构
learn_django
- Dashboard
    - migrations（记录对数据的修改）不要动
        - __init__.py
    - static（图片，css，js）
      - css
      - img
      - js
      - plugins
    - __init__.py
    - admin.py（django提供的admin后台管理）不要动
    - apps.py（app启动类）不要动
    - models.py（对数据操作）经常改动
    - tests.py（单元测试）不用动
    - views.py（函数，与urls.py关联）经常改动
- manage.py（启动项目，创建app，数据库管理）不要动
- learn_django
    - __init__.py
    - asgi.py（异步网络请求）不要动
    - settings.py（配置文件）经常改动
    - urls.py（页面和函数的对应关系）经常改动
    - wsgi.py（同步网络请求）不要动
```

- 注册app（setting.py）
![Alt text](/Dashboard/static/img/Django/django安装4.png)
- 编写URL和view（视图）的对应关系（urls.py）
![Alt text](/Dashboard/static/img/Django/django安装5.png)
- 编写视图函数（views.py）
![Alt text](/Dashboard/static/img/Django/django安装6.png)
- 命令行启动：python manage.py runserver
- pycharm启动和调试
![Alt text](/Dashboard/static/img/Django/django安装7.png)
- 设置全局模板位置
- 优先找settings.TEMPLATES里的DIRS配置的路径
- 其次根据app的注册顺序找templates文件夹

![Alt text](/Dashboard/static/img/Django/django安装8.png)

### 模板语法

- url.py ---> views.py ---> templates
- 读取含有模板语法的HTML文件
- 内部渲染（模板语法执行并替换数据）
- 将只包含HTML标签的字符串返还给浏览器
- 参考index.html

### MySql

- 修改默认数据库
![Alt text](/Dashboard/static/img/Django/django安装10.png)
- 删掉db.sqlite3
![Alt text](/Dashboard/static/img/Django/django安装11.png)
- 内部提供了ORM框架，可以增删改查，但不能创建数据库
- pip install mysqlclient（旧版用pymysql，新版用mysqlclient）或者下载whell包[mysqlclient](https://pypi.org/project/mysqlclient/#files)
![Alt text](/Dashboard/static/img/Django/django安装9.png)
- 注释下面语句，否则会失败（django.db.utils.NotSupportedError: MySQL 8.0.11 or later is required (found 5.7.31).）
![Alt text](/Dashboard/static/img/Django/django安装12.png)

- 在models.py里新建数据表，执行以下语句创建数表

```{.py}
python manage.py makemigrations
python manage.py migrate
```

- 删除表或者某一列只需要把注释掉并执行命令即可
- 如果新建一列需要有默认值

## [Bootstrap](https://v3.bootcss.com/)

- 定义: 别人写好的css
- 下载安装
![Alt text](/Dashboard/static/img/Bootstrap/Bootstrap安装1.png)
![Alt text](/Dashboard/static/img/Bootstrap/Bootstrap安装2.png)
![Alt text](/Dashboard/static/img/Bootstrap/Bootstrap安装3.png)
![Alt text](/Dashboard/static/img/Bootstrap/Bootstrap安装4.png)

## [fontawesome](https://fontawesome.dashgame.com/)

- 定义: 是一个专门的图标网站
- 下载安装
![Alt text](/Dashboard/static/img/Bootstrap/Bootstrap安装5.png)
![Alt text](/Dashboard/static/img/Bootstrap/Bootstrap安装6.png)

## [jQuery](https://jquery.com/)

- 定义：Bootstrap依赖jQuery，动态效果
- 下载安装
![Alt text](/Dashboard/static/img/Bootstrap/Bootstrap安装7.png)
![Alt text](/Dashboard/static/img/Bootstrap/Bootstrap安装8.png)
