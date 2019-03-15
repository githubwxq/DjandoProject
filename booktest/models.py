from django.db import models

# 写和数据库相关的内容
class BookInfo(models.Model):
    bittle=models.CharField(max_length=20)
    bpub_date=models.DateField

    def __str__(self):
        return self.bittle




class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField(default=False)
    hcomment=models.CharField(max_length=128)

    #关系属性
    hbook=models.ForeignKey("BookInfo",on_delete=models.CASCADE,default="")

