from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django_redis import cache
from markdown import logger
from t8.my_util import get_random_str

# Create your views here.
import logging
logging=logging.getLogger('django')


def index(req):
    return HttpResponse("6")

def send_my_email(req):
        title = "磊磊加油哇"
        msg = "恭喜帅磊磊喜提高铁一辆"
        email_from = settings.DEFAULT_FROM_EMAIL
        reciever = [
            '1820440070@qq.com',
        ]
        send_mail(title, msg, email_from, reciever)
        return HttpResponse("ok")
def send_my_email_v1(req):
    title = "磊磊加油哇"
    msg = ""
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '1820440070@qq.com',
    ]
    #加载模板
    template=loader.get_template('templates/t8/email.html')
   #渲染模板
    html_str=template.render({'msg':"   qaq     "})
    print((html_str))
    send_mail(title, msg, email_from, reciever,html_message=html_str)
    return HttpResponse("ok")
#邮箱验证码
#生成随机字符串-拼接激活链接url-数据保存到缓存-创建激活页面-发给某个账号-完成验证
def verify(req):
    if req.method=="GET":
        return render(req,'templates/t8/verify.html')
    else:
        params=req.POST
        email= params.get("email")
        #生成随机字符
        random_str=get_random_str()
        #拼接
        url="127.0.0.1:8000/t8/active"+random_str
        #加载激活模板
        tem=loader.get_template("templates/t8/active.html")
        #渲染模板
        html_str=tem.render({'url':url})
        title = "磊磊加油哇"
        msg = ""
        email_from = settings.DEFAULT_FROM_EMAIL
        reciever = [
            '1820440070@qq.com',
        ]
        #增加缓存
        send_mail(title, msg, email_from, reciever, html_message=html_str)
        cache.get(random_str,email,120)
        return HttpResponse("ok")
#激活
def active(req,random_str):
    res=cache.get(random_str)
    if res:
        return HttpResponse(res+"successful")
    else:
        return HttpResponse("failed")
#多份邮件
def send_many_email(req):
    title = "加油"
    content1 = "恭喜帅磊磊喜提高铁一辆"
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever1 = [
        '1820440070@qq.com',
        '554468924@qq.com'
    ]
    content2="皮一下，超好玩的"
    #邮件1&2
    msg1 = (title, content1, email_from, reciever1)
    msg2 = ("小哥哥", content2, email_from,
          ['1820440070@qq.com','2476583603@qq.com'])
    #使用send_mass_mail
    send_mass_mail((msg1, msg2), fail_silently=True)
    return HttpResponse("ok 666")
# 日志log
# def test_log(req):
#     logger.info("下课了")
#     return HttpResponse("嗨森")
