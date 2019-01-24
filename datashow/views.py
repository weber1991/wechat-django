# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from datashow.selectWaitingCount import selectWaitingCount
from datashow.selectWaitingCountFang import selectWaitingCountFang
from datashow.selectWaitingCountNoWork import selectWaitingCountNoWork
import datetime
from datashow.UsePymysql0 import dateQuery
import pymssql
import sys
reload(sys)
sys.setdefaultencoding("utf8")

# Create your views here.


def index(req):
    try:
        dateToday = datetime.datetime.now().date().strftime('%Y%m%d')
        dateHour = datetime.datetime.now().hour  # type is int
        status = dateQuery(dateToday)
        if status != '0':  # '0' is working , '1'is weekend, '2' is holiday
            print('this is ' + status + '.')
            dataList = {}
            return render_to_response('indexHoliday.html', {'dataList': dataList})
        elif (dateHour <= 18) and (dateHour >= 8):  # working time is 8:00--18:00
            print('this is working.')
            dataList = selectWaitingCount()
            return render_to_response('indexShowData.html', {'dataList': dataList})
        else:
            print('this is no work.')
            dataList = selectWaitingCountNoWork()
            return render_to_response('indexShowData.html', {'dataList': dataList})
    except Exception, e:
        print e
        dataList = {}
        return render_to_response('indexError.html', {'dataList':dataList})



def person(req):
    tlist ={ }
    return render(req,'person.html',{'tlist': tlist})


def wxjz(req):
    return render(req, 'wxjz_index.html',)


def zhishui(req):
    newList = getZhishui()
    return render(req, 'index_zhishui.html', {'newList': newList},)
	
def detial(req):
	newid = str(req.GET.get('newid'))
	new = getNew(newid)
	return render(req, 'zhishui_detial.html', {'new':new},)


def getZhishui():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='xxb2016',
        db='dl',
        charset='utf8'
    )
    cur = conn.cursor()
    if not cur:
        print 'error'
        raise Exception('error')

    sql = "select * from tblNews where Title like '%治理%'"
    sql1 = "select * from tblNews "
    sql2 = "select NewsId, Title, AddTime from tblNews where 1 = 1 AND Title like '%治理%' AND Title like '%水%' ORDER BY AddTime DESC "
    sql3 = "select NewsId, Title, AddTime from tblNews where 1 = 1 AND Content like '%水污染%' ORDER BY AddTime DESC "

    newList = [ ]

    cur.execute(sql3)
    result = cur.fetchall()
    for temp in result:
        new = { }
        new['NewsId'] = temp[0]
        new['Title'] = temp[1]
        new['AddTime'] = temp[2]
        newList.append(new)

    conn.close()
    return newList
	

def AddStr(str0):
    pos = str0.find("/upload")
    if pos != -1:
        str = str0[:pos] + "http://news.dalang.gov.cn" + str0[pos:]
        return str
    else:
        return str0


def completeContent(dic):
    pos = dic.find("/dalang/")
    if pos != -1:
        temp = dic
        tempStr = temp.replace('/dalang/', 'http://dg.gov.cn/dalang/')
        return tempStr
    else:
        return dic



	

def getNew(id):
    conn = pymysql.connect(
        host='61.145.223.28',
        port=3306,
        user='root',
        password='xxb2016',
        db='dl',
        charset='utf8'
    )
    cur = conn.cursor()
    if not cur:
        print 'error'
        raise Exception('error')

    sql = "select * from tblNews where Title like '%治理%'"
    sql1 = "select * from tblNews "
    sql2 = "select NewsId, Title, Content, AddTime, Source, Author, DvLink from tblNews where 1 = 1 AND NewsId = %s "
    newList = [ ]

    cur.execute(sql2,(id))
    result = cur.fetchall()
    for temp in result:
        new = { }
        new['NewsId'] = temp[0]
        new['Title'] = temp[1]
        if len(temp[0]) > 8:
            new['Content'] = completeContent(temp[2])
        else:
            new['Content'] = AddStr(temp[2])
        new['AddTime'] = temp[3]
        new['Source'] = temp[4]
        new['Author'] = temp[5]
        new['DvLink'] = str(temp[6])
        newList.append(new)

    conn.close()
    return newList