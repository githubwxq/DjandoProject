from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader ,RequestContext,context
from django.test import TestCase
from booktest.models import BookInfo,HeroInfo
from datetime import date
#  接收请求进行处理 与m何t 层交互返回应答 定义视图函数
#  定义视图函数 httprequest

#1定义视图函数
#2进行url配置 简历url地址和视图的对应关系

#http://127.0.0.1:8080/index  处理 进行处理和m和t 进行交互。。

def index(request):
    #进行处理和m和t 进行交互
    # 1加载模板文件

    b=BookInfo()
    b.bittle="天龙八部"
    b.bpub_date=date(1990,1,1);
    b.save()


    temp=loader.get_template('booktest/index.html')
    # 2定义上下文传递数据  ##必须加上单引号
    c = {'foo': 'bar','list':{'orange', 'banana', 'pear', 'apple'}}
    # 3 模板渲染：产生标准的html内容
    res_html= temp.render(c,request)
    # 4 返回给浏览器
    return HttpResponse(res_html);


def index2(request):
    #进行处理和m和t 进行交互
    # return HttpResponse("index2")
    # 1加载模板文件
    temp=loader.get_template('booktest/index.html')
    # 2定义上下文传递数据
    context= RequestContext(request,{})
    # 3 模板渲染：产生标准的html内容
    res_html= temp.render(context)
    # 4 返回给浏览器
    return HttpResponse(res_html);
