'''
Author: Gtylcara.
Date: 2021-04-26 14:10:32
LastEditors: Gtylcara.
LastEditTime: 2021-04-26 22:09:39
'''


from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

import json
import time


def login(request):
    username = request.GET["username"]
    password = request.GET["pwd"]

    conn = connection.cursor()
    
    conn.execute(
        f"select * from garbage_userdb where username='{username}'")
    res = conn.fetchone()
    # id username password openId score auth face openId2

    #  id: data.PlayerId,
    #  username: data.Mobile,
    #  mobile: data.Mobile,
    #  nickname: data.NickName,
    #  imgurl: data.ImgUrl | | "../../images/defuser.jpg",
    #  signature: data.SelfdomSign,

    code = 0 # 0是密码不同
    data = {"id": res[0], "username": res[1], "mobile": 0, "auth": 1}
    if res[2] == password:
        code = 1
    


    retval = {"code": code, "data": data}

    retval = json.dumps(retval)
    return HttpResponse(retval)


# 检查SMS
# mobile: 手机号
# verifycode: SMScode
def checkSMS(request):

    retval = {"code": 1, "data": 0}
    retval = json.dumps(retval)
    return HttpResponse(retval)


# 获取sms码
# mobile：手机号
# type: SMS1001
def getSMS(request):

    retval = {"code": 1, "data": 0}
    retval = json.dumps(retval)
    return HttpResponse(retval)

# 注册
# mobile: 手机号,
# pwd: 密码,
# username: 用户名,
def register(request):
    
    mobile = request.GET["mobile"]
    password = request.GET["pwd"]
    username = request.GET["username"]

    conn = connection.cursor()
    conn.execute(
        f"select * from garbage_userdb where username={username}")
    res = conn.fetchone()
    print(res)
    code = 100
    if (res != None):
        code = 100
    else:
        code = 1
        sql = f'INSERT INTO garbage_userdb(username, password, score, auth) VALUES(\'{username}\', \'{password}\', 0, 0) '

        conn.execute(sql)
        conn.connection.commit()
    conn.close()

    retval = {"code": code, "data": 0}
    retval = json.dumps(retval)
    return HttpResponse(retval)

def thirdParty(request):
    openId = request.GET["OpenId"]
    thirdPartyId = request.GET["ThirdPartyId"]

    conn = connection.cursor()
    if (thirdPartyId == 1):
        third = ""
    else:
        third = "2"
    conn.execute(f"select * from garbage_userdb where openId{third}='{openId}'")
    res = conn.fetchone()
    conn.close()
    code = 0
    if res == None:
        code = 1
    retval = {"code": code}
    # code == 0 存在账号 code == 1 不存在
    retval = json.dumps(retval)
    return HttpResponse(retval)
