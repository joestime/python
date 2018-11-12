import urllib.request
import re

url = 'https://news.sina.com.cn/'

html = urllib.request.urlopen(url, timeout=15).read()
html = html.decode("utf-8","ignore")

part = 'href="(https://news.sina.com.cn/.*?)"'
'''
links = re.findall(part,html)
'''
links = re.compile(part).findall(html)

for i in range(0, len(links)):
    try:
        thisurl = links[i]
        print(links[i])
        file = "C:/Python files/"+ str(i)+".html"
        urllib.request.urlretrieve(thisurl, file)   #存为文件
    except Exception as e:
        print(e)