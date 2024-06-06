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
![Alt text](/Dashboard/static/img/Django/django安装8.png)

### 模板语法

- url.py ---> views.py ---> templates
- 读取含有模板语法的HTML文件
- 内部渲染（模板语法执行并替换数据）
- 将只包含HTML标签的字符串返还给浏览器

```{.py}
{#settings.py里的STATIC_URL配置路径#}
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}">
</head>
<body>
{#使用变量#}
{#<h1>{{ name }}</h1>#}
{#<div>{{ role_list.0 }}</div>#}
{#<div>{{ role_list.1 }}</div>#}
{#<div>{{ user_info_dict.name }}</div>#}
{#<div>{{ user_info_dict.age }}</div>#}

{#循环列表#}
{#<div>#}
{#    {% for item in role_list %}#}
{#        <span>{{ item }}</span>#}
{#    {% endfor %}#}
{#</div>#}

{#循环字典#}
{#<div>#}
{#    {% for item in user_info_dict.keys %}#}
{#        <span>{{ item }}</span>#}
{#    {% endfor %}#}
{#</div>#}
{#<div>#}
{#    {% for item in user_info_dict.values %}#}
{#        <span>{{ item }}</span>#}
{#    {% endfor %}#}
{#</div>#}
{#<div>#}
{#    {% for k, v in user_info_dict.items %}#}
{#        <span>{{ k }}={{ v }}</span>#}
{#    {% endfor %}#}
{#</div>#}

{#条件语句#}
{#<div>#}
{#    {% if name == "v_hlhllu" %}#}
{#        <h1>英文名1 {{ name }}</h1>#}
{#    {% elif name == "luck" %}#}
{#        <h1>英文名2 {{ name }}</h1>#}
{#    {% else %}#}
{#        <h1>英文名3 {{ name }}</h1>#}
{#    {% endif %}#}
{#</div>#}

<h1>用户登录</h1>
<form method="post" action="/index/">
    {# django提供的校验，必须带上 #}
    {% csrf_token %}
    <input type="text" name="user" placeholder="用户名">
    <input type="password" name="pwd" placeholder="密码">
    <input type="text" name="age" placeholder="年龄">
    <input type="submit" value="提交">
    <span style="color: red;">{{ error_msg }}</span>
</form>

{#模板继承，只需要继承它的模板重新content即可#}
<div>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</div>

{#模板继承#}
{% extends 'index.html' %}
{% block content %}
        <h1>重新的内容</h1>
{% endblock %}

<script src="{% static 'js/jquery-3.7.1.min.js' %}"></script>
<script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.js' %}"></script>
</body>
</html>
```

```{.html}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<a href="/index">添加</a>
<table >
    <thead>
        <tr>
            <th>ID</th>
            <th>姓名</th>
            <th>密码</th>
            <th>年龄</th>
            <th>删除</th>
        </tr>
    </thead>
    <tbody>
        {% for obj in data_list %}
            <tr>
                <td>{{ obj.id }}</td>
                <td>{{ obj.name }}</td>
                <td>{{ obj.password }}</td>
                <td>{{ obj.age }}</td>
                <td>
                    <a href="/user/delete/?nid={{ obj.id }}">删除</a>
                </td>
            </tr>
        {% endfor %}
    </tbody>
</table>
</body>
</html>
```

```{.py}
from django.contrib import admin
from django.urls import path
from Dashboard import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # www.xxx.com/index/ -> 函数
    path('index/', views.index),
    path('user/list/', views.user_list),
    path('user/delete/', views.user_delete),
    # 必须以如下格式 http://127.0.0.1:8000/user/1/editor/
    # path('user/<int:nid>/editor/', views.user_editor),
]
```

### MySql

- 修改默认数据库
![Alt text](/Dashboard/static/img/Django/django安装10.png)
- 删掉db.sqlite3
![Alt text](/Dashboard/static/img/Django/django安装11.png)
- 内部提供了ORM框架，可以增删改查，但不能创建数据库
- pip install mysqlclient（旧版用pymysql，新版用mysqlclient）或者下载whell包[mysqlclient](https://pypi.org/project/mysqlclient/#files)
![Alt text](/Dashboard/static/img/Django/django安装9.png)

- 在models.py里新建数据表

```{.py}
from django.db import models


# 自动生成sql语句
# app名_类名小写
"""
create table dashboard_userinfo(
    id bigint auto_increment primary key,
    name varchar(32),
    password varchar(64),
    age int
)
"""


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

    # class Department(models.Model):
    #     title = models.CharField(verbose_name="标题", max_length=32)
    # 无约束的
    # depart_id = models.BigIntegerField(verbose_name="部门ID")
    # 有约束的, -to:与哪张表关联，-to_filed:与表中的哪一列关联
    # 写的字段名是depart数据库中是depart_id
    # depart_id字段的值只能是Department已有的id
    # 级联删除：Department表删除某个部门，depart指定部门也会被删除
    # depart = models.ForeignKey(to="Department", to_fields="id", on_delete=models.CASCADE())
    # 置空
    # depart = models.ForeignKey(to="Department", to_fields="id", null=True, blank=True, on_delete=models.SET_NULL())

    # 在django中做的约束
    # 只能1或者2
    # gender_choices = (
    #     (1, "男"),
    #     (2, "女"),
    # )
    # gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

# 新建数据
# UserInfo.objects.create(name="v_hlhllu", password="123456", age="30")

# 删除数据
# row_obj = UserInfo.objects.filter(id=1).first()
# print(row_obj.id, row_obj.name)
# row_obj.delete()
# data_list = UserInfo.objects.all()
# for data in data_list:
#     print(data.id, data.name, data.password, data.age)
# data_list.delete()

# 更新数据
# UserInfo.objects.all().update(age=18)
# UserInfo.objects.filter(name="v_hlhllu").update(age=18)

```

- 注释下面语句，否则会失败（django.db.utils.NotSupportedError: MySQL 8.0.11 or later is required (found 5.7.31).）
![Alt text](/Dashboard/static/img/Django/django安装12.png)

- 执行以下语句创建数表

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