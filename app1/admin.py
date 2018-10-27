from django.contrib import admin
from .models import User,Diary

# 注册数据模型才能在admin站点中处理数据
admin.site.register(User)
admin.site.register(Diary)


# # 自定义admin表单提交
# class UserAdmin(admin.ModelAdmin):
#     fields = [ 'password','username']  # 设置表单要提交的内容和顺序。我们可以将用户名和密码翻转了一下
#
# # 自定义admin表单提交
# class DiaryAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['user']}),    # 设置表单要提交 的分组显示。在有很多个字段时需要填写的内容会分组显示。
#         ('Date information', {'fields': ['content']}),
#     ]
#
# admin.site.register(User, UserAdmin)  # admin默认会要求选择时间，自定义方式不需要提交时间。
# admin.site.register(Diary, DiaryAdmin)  # 提交内容分组显示