#coding=utf-8

'''Get LiHua Menu'''

import urllib.request
import re

def gethtml(url):
    '''Get Html String.'''
    page = urllib.request.urlopen(url)
    return page.read()

def getmenu(html):
    '''Get Menu String.'''
    #30块钱套餐
    reg = r'<td>精品白领套餐</td>\s*<td>(.*)</td>'
    return re.findall(reg, html.decode("utf-8"))

HTML = gethtml("http://www.lihua.com/index.php?s=/Index/weekOrder.html")

MENU = getmenu(HTML)

SIZE = len(MENU)
if SIZE > 0:
    print(MENU[0].replace("(仅供参考)", "").replace("（仅供参考）", ""))
else:
    print("Not Found")
