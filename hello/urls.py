"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include,url  # Django1.11中的语法
from django.urls import path,include  #Django2中的语法
from django.contrib import admin

urlpatterns = [
    # url是一个函数。regex和view为必填参数。regex就是用户输入的内容，view就是对应的视图生成函数
    url(r'^vip/', admin.site.urls),  # Django自带的超级管理员后台地址。不要用台随意的网址
    url(r'^app1/', include('app1.urls')),  # 映射到下级路由
    # path(r'^app2/', include('app2.urls')),  # 映射到下级路由
]
