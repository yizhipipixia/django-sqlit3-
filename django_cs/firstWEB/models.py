from __future__ import unicode_literals
from django.db import models
# Create your models here.db.sqlite3

#这里类似于表的描述文件,下面这个类
class cal(models.Model):
    value_a = models.CharField(max_length= 10) #这个字符串存储的数据量为10
    value_b = models.FloatField(max_length= 10) #浮点数的长度
    result = models.CharField(max_length= 10)