from django.http import HttpResponse,JsonResponse,Http404
from .models import User,Diary
from django.shortcuts import render_to_response,render,redirect,reverse,HttpResponseRedirect,get_object_or_404
from django.template import Context,loader
from django.forms.models import model_to_dict
import time

# 接收请求数据返回字符串响应。http://127.0.0.1:8000/app1/
def index(request):
    return HttpResponse("Hello, world")   # 直接返回响应字符串


# insertuser接收网页的post数据并将传入的用户名、密码数据存储到数据库中；
# 这一个函数包含了两个独立的功能。1、返回用户注册页面，2、接收用户post数据，注册用户后重定向到另一个页面
def insertuser(request):
    if request.method == "POST":
        username = request.POST.get("username", None)   # 读取post数据，None为默认值
        password = request.POST.get("password", None)   # 读取post数据，None为默认值
        user = User(username=username, password=password,date=time.strftime('%Y-%m-%d',time.localtime(time.time())))
        user.save()
        # 重定向跳转到所有用户列表页面
        return redirect('/app1/alluser/')  # 硬编码形式
        # return redirect('app1_name:alluserpath')  #URLconf命名空间的形式
        # return redirect('/app1/finduser/?userid=62')  # 传递参数
        # 重定向跳转到个人详情页面
        # urlpath = reverse('app1_name:detail', args=(user.id,)) # 将args传递给app1:detail对应的视图，然后生成网址。因为urls中的网址有时也需要参数才能完整
        # return HttpResponseRedirect(urlpath)  #参数可以是绝对路径跟相对路径,也可以使用get方式传参数
    return render_to_response('app1/insert.html')  # 返回文件响应


# 返回字典或json字符串
def finduser(request):
    try:
        userid = request.GET.get("userid", None)  # 读取数据
        users = User.objects.filter(id=userid)  # 获取一个用户，返回QuerySet
        user = users[0]  # 获取第一个user对象
        user_dict1 = model_to_dict(user)  # 将对象转化为字典
        return JsonResponse(user_dict1)  # 返回前端字典
    except:
        raise Http404("用户不存在")




# findalluser将数据库内存储的数据读出并展示出来。
def findalluser(request):
    allpeople = User.objects.all()  # 查询所有用户
    dict1={
        'people_list':allpeople
    }
    return render_to_response("app1/showuser.html",dict1)  # 返回文件响应，第二个参数必须为字典



# 一个用户的详细信息。网址urls里面写的是包含此userid参数的，因此对应的函数中也就包含此参数。
def detail(request,userid):
    user = get_object_or_404(User, id=userid)  # 合并了404错误的查询方法
    dict1={
        'user': user
    }
    # 全局render函数
    return render(request, 'app1/oneuser.html', dict1)  # 生成HttpResponse对象
    # 模板render函数
    # template = loader.get_template('app1/oneuser.html')  # 加载模板对象
    # return HttpResponse(template.render(dict1, request)) # 渲染视图


