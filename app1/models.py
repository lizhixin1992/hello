from django.db import models
# 设置对象结构（对应数据库的结构）
class User(models.Model):
    username = models.CharField(max_length=200)  # 字符串类型字段
    password = models.CharField(max_length=200,null=True)  # 字符串类型字段,null=True允许为空
    age = models.IntegerField(default=0)  # 整数类型字段
    date = models.DateTimeField('date registered',auto_now=True)  # 时间类型字段，参数为人类可读的字段名

    # 模型的元数据Meta
    class Meta:  # 注意，是模型的子类，要缩进！
        db_table = 'user'

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 外键。
    content = models.TextField()  # 文本类型字段

    # 模型的元数据Meta
    class Meta:  # 注意，是模型的子类，要缩进！
        db_table = 'diary'