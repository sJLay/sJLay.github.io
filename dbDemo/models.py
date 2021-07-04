from django.db import models

class DbDemo(models.Model):
    '''
    数据库实例化
    '''
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    # id = models.AutoField(primary_key=True)




# Create your models here.
