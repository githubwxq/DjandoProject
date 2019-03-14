from django.test import TestCase
from booktest.models import BookInfo,HeroInfo
from datetime import date
# 写测试代码
if __name__ == '__main__':
    b=BookInfo()
    b.bittle="天龙八部"
    b.bpub_date=date(1990,1,1);
    b.save()

    h=HeroInfo()
    h.hname="wxq"
    h.hgender=True
    h.hbook=b
    h.save()
    h.objects.all()
