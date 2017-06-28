#coding=utf-8
import urllib.request
import re
#py抓取页面图片并保存到本地

#获取页面信息
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
#通过正则获取图片
def getImg(html):
    reg = r'src="(.+?\.jpg)" size'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html.decode("utf-8"))
    return imglist
html = getHtml("https://tieba.baidu.com/p/5010750920")

imgs = getImg(html)

x = 0
for imgurl in imgs:
    urllib.request.urlretrieve(imgurl, 'D:\\imgsssss\%s.jpg' %x)
    x+=1

print(len(imgs))
