from django.contrib import admin
from booktest.models import BookInfo,HeroInfo
# 网站后台管理页面文件  注册模型类（图书 英雄）
#
# class BookInfoAdmin(admin.ModelAdmin):
#     list_display= ["id","btitle","bpub_date"]




admin.site.register(BookInfo)
admin.site.register(HeroInfo)
