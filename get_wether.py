#coding:utf-8
import re
import urllib.request

url = 'http://www.nmc.cn'
html = urllib.request.urlopen(url).read()
html = html.decode('utf-8')
links = re.findall('<a class="other" target="_blank" href="(.+?)" title', html)
titles = re.findall('<a class="other" target="_blank" .+? title="">(.+?)<span>', html)
hours = re.findall('<a class="other" target="_blank" .+? title="">.+?<span>(.+?)<', html)
for link, title, hour in zip(links, titles, hours):
    print(hour, title, url+link)

