#coding=utf-8

'''For BBS, Upload Image File Interface Test'''

import http.client
import base64
import sys
import os
import urllib

if len(sys.argv) != 3:
    print("参数有误")
    sys.exit()

FILEPATH = sys.argv[2]

FILE = open(FILEPATH, 'rb')
BASE64_FILE = base64.b64encode(FILE.read())
FILE.close()

CONN = http.client.HTTPConnection("url________Path")  # 添加接口地址

BODY = {
    'RelevantId': sys.argv[1],
    'Extension': os.path.splitext(FILEPATH)[1],
    'Data': str(BASE64_FILE, encoding="utf-8")
}

HEADERS = {
    'content-type': "application/x-www-form-urlencoded",
    'authorization': "Basic Base64", # 添加Auth字符串
    'cache-control': "no-cache"
    }

CONN.request("POST", "/api/Upload", urllib.parse.urlencode(BODY), HEADERS)

RES = CONN.getresponse()

print(RES.read().decode("utf-8"))
