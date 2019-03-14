from django.contrib import admin
from booktest.models import BookInfo
# 网站后台管理页面文件  注册模型类（图书 英雄）

admin.site.register(BookInfo)
