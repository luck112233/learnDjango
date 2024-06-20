"""
URL configuration for learnDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Dashboard import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('user/list/', views.user_list),
    path('user/delete/', views.user_delete),
    path('learn_html/', views.learn_html),
    path('learn_css/', views.learn_css),
    path('learn_js/', views.learn_js),
    path('learn_bootstrap/', views.learn_bootstrap),
    # 必须以如下格式 http://127.0.0.1:8000/user/1/editor/
    # path('user/<int:nid>/editor/', views.user_editor),
]
