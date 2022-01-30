from django.conf.urls import url
from . import views

app_name = 'app2_name'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}
urlpatterns = [
    url(r'^$', views.index, name='index'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app2/
]