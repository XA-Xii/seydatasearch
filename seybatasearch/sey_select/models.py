from __future__ import unicode_literals

from django.db import models

# Create your models here.

class seymaterial(models.Model):
      objects = models.Manager() #默认管理器
      mno = models.IntegerField(unique=True, primary_key=True)
      mname = models.CharField(max_length=10, null= True)

class seyvalue(models.Model):
      vno = models.IntegerField(unique=True, primary_key=True)
      vinp = models.IntegerField(null = True)
      vsey = models.FloatField(null= True)
      vposi = models.FloatField(null = True)
      vnega = models.FloatField(null= True)
      manum = models.ForeignKey(to='seymaterial', to_field='mno', on_delete=models.CASCADE)
      objects = models.Manager() #默认管理器

class Seytext(models.Model):
      textnum = models.ForeignKey(to='seymaterial', to_field='mno', on_delete=models.CASCADE)
      content = models.TextField(u'二次电子发射系数')
      upload_data = models.DateTimeField(u'上传时间',auto_now_add=True,editable=True)
      update_time = models.DateTimeField(u'更新时间', auto_now=True, null= True)
      objects = models.Manager()