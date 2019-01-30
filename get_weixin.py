import re
import urllib.request
import time
import urllib.error
import random


#自定义函数，通过代理爬一个网址

def user_proxy(proxy_adr, url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77')
        proxy =urllib.request.ProxyHandler({'http':proxy_adr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(req).read()
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(random.randint(2, 5))
    except Exception as e:
        print("exception:"+ str(e))
        time.sleep(random.randint(1, 3))

key = "python"

proxy = "127.0.0.1:8888"

for i in range(0, 10):
    key = urllib.request.quote(key)
    thispageurl = "http://weixin.sogou.com/weixin?type=2&query="+key+"&page="+str(i)
    thispagedata = user_proxy(proxy, thispageurl)
    print(len(str(thispagedata)))
    pat1 = '<a href="(.*?)"'
    rs1 = re.compile(pat1, re.S).findall(str(thispagedata))
    if (len(rs1) == 0):
        print("此次（"+str(i) + "页）没有成功")
        continue
    for j in range(0, len(rs1)):
        thisurl = rs1[j]
        thisurl = thisurl.replace("amp:","")
        file = "C:/Python files/weixin/第"+str(i)+"页第"+str(j)+"篇文章.html"
        thisdata = user_proxy(proxy, thisurl)
        try:
            fh = open(file, "wb")
            fh.write(thisdata)
            fh.close()
            print("第"+str(i)+"页第"+str(j)+"篇文章成功")
        except Exception as  e:
            print(e)
            print("第" + str(i) + "页第" + str(j) + "篇文章失败")