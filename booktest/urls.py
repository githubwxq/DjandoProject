from django.conf.urls import  url
from booktest import views

urlpatterns=[
    #通过url函数设置url路由的配置项

    url(r'^index2$',views.index2),
    url(r'^index$',views.index),
    url(r'^delete$',views.delete),






]