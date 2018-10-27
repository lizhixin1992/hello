from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
from . import views
from django.views.generic import RedirectView

app_name = 'app1_name'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^$', views.index, name='index'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^insert/', views.insertuser,name='inserpath'),  # 直接映射到函数
    url(r'^alluser/', views.findalluser,name='alluserpath'),  # 直接映射到函数
    url(r'^finduser/', views.finduser),  # 直接映射到函数
    # url通过(?P<name>pattern)来接收参数。因此(?P<userid>[0-9]+)就是一个参数。重定向到这个url时需要传递这个参数，url才能完整生成。
    # ex:reverse('app1_name:detail', args=11) 生成网址/app1/11/detail/
    url(r'^(?P<userid>[0-9]+)/detail/$', views.detail, name='detail'),
    path('userid/<int:userid>/', views.detail),
    # 重定向
    # url(r'^$', RedirectView.as_view(url='/'),permanent=True)
]