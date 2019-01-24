#-*-coding:utf-8-*-
from django.shortcuts import render
from django.shortcuts import render_to_response
import datetime
import random
# Create your views here.
def index_question(req):
    try:
        nowTime = datetime.datetime.now().strftime("%m%d%H%M%S")    #10 bit
        randomNum = random.randint(100, 999)  # 生成的随机整数n，其中100<=n<=999
        wechatId = str(nowTime) + str(randomNum)
        urlQuestion = r'http://wx.dalang.cc/index.php?g=Wap&m=Problem&a=users&token=vyszmt1426060953&wecha_id=' + wechatId + '&id=11'
        #print urlQuestion
    except Exception, e:
        print e
        urlQuestion = r'http://wx.dalang.cc/index.php?g=Wap&m=Problem&a=users&token=vyszmt1426060953&wecha_id=5624562352345&id=10'
    return render_to_response('index_question.html', {'quesUrl': urlQuestion})


def index_guize(req):
    return render(req,'index_guize.html')