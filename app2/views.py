# from __future__ import unicode_literals
from django.http import HttpResponse,JsonResponse,Http404
from app2 import models
from django.shortcuts import render_to_response,render,redirect,reverse,HttpResponseRedirect,get_object_or_404
from django.template import Context,loader
from django.core import serializers
from django.forms.models import model_to_dict
import time
import json

# 接收请求数据返回字符串响应
def index(request):
    return HttpResponse("接收数据成功")   # 直接返回响应字符串
