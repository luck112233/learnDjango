from django.shortcuts import render, HttpResponse, redirect
from Dashboard.models import UserInfo


def index(req):
    # return HttpResponse("直接返回文本")
    # 重定向浏览器（让浏览器重新向指定连接发请求）
    # return redirect("https://www.baidu.com")
    # 返回自定义模板
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
        UserInfo.objects.create(name=user_name, password=pwd, age=age)
        return redirect("/user/list")


def user_list(req):
    # 获取所有数据
    data_list = UserInfo.objects.all()
    # 获取第一条数据
    # data_obj = UserInfo.objects.filter(id=1).first()
    return render(req, "user_list.html", {"data_list": data_list})


def user_delete(req):
    nid = req.GET.get("nid")
    # 删除指定数据
    UserInfo.objects.filter(id=nid).delete()
    # 删除所有数据
    # UserInfo.objects.all().delete()
    return redirect("/user/list")


def user_change(req):
    nid = req.GET.get("nid")
    # 修改指定数据
    UserInfo.objects.filter(id=nid).update(age=100)
    # 修改所有数据
    # UserInfo.objects.all().update(age=100)
    return redirect("/user/list")


def learn_html(req):
    return render(req, "LearnHtml.html")


def learn_css(req):
    return render(req, "LearnCSS.html")


def learn_js(req):
    return render(req, "LearnJS.html")


def learn_bootstrap(req):
    return render(req, "learnBootstrap.html")
