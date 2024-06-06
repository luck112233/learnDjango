from django.shortcuts import render, HttpResponse, redirect
from Dashboard.models import UserInfo


def user_list(req):
    data_list = UserInfo.objects.all()
    return render(req, "user_list.html", {"data_list": data_list})


def user_delete(req):
    nid = req.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list")


def index(req):
    # 直接返回文本
    # content_str = "内容"
    # return HttpResponse(content_str)

    # 重定向浏览器（让浏览器重新向指定连接发请求）
    # return redirect("https://www.baidu.com")

    # 返回自定义模板
    # 优先找settings.TEMPLATES里的DIRS配置的路径
    # 其次根据app的注册顺序找templates文件夹
    role_list = ["管理员", "员工"]
    user_info_dict = {"name": "v_hlhllu", "age": 30}
    return render(req, "index.html", {"name": "v_hlhllu", "role_list": role_list, "user_info_dict": user_info_dict})


def login(req):
    # url打开是get请求
    if req.method == "GET":
        return render(req, "login.html")
    if req.method == "POST":
        user_name = req.POST.get("user")
        pwd = req.POST.get("pwd")
        age = req.POST.get("age")
        print(user_name, pwd, age)
        return HttpResponse(f"{user_name}登录成功")
        # UserInfo.objects.create(name=user_name, password=pwd, age=age)
        # return redirect("/user/list")

