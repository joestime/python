# coding:utf-8

import requests
from lxml import etree
from chardet import detect
import csv

url = 'http://top.baidu.com/buzz?b=1&fr=20811'
resp = requests.get(url, timeout=15)
encoing = detect(resp.content).get('encoding')
html = resp.content.decode(encoing,'ignore')
## UnicodeDecodeError: 'gb2312' codec can't decode byte 0x86 in position 20164: illegal multibyte sequence
## 网页有 非法字符你需要加上ignore

tree = etree.HTML(html)

for hot in tree.xpath('//table[@class="list-table"]//td[@class="keyword"]'):
    title = hot.xpath('.//a[@class="list-title"]')[0].text.strip()
    href = hot.xpath('.//a/@href')[0]
    print(str(title)+"  "+str(href))

print("--------")

csv_file = open('baidu_hotspot.csv', 'a', encoding='utf-8', newline='')
csv_wr = csv.writer(csv_file)
for hot in tree.xpath('//table[@class="list-table"]//tr'):
    try:
        title = hot.xpath('.//td[@class="keyword"]//a[@class="list-title"]')[0].text.strip()
        count = hot.xpath('.//td[@class="last"]//span[1]')[0].text.strip()#第一个span元素
        #href = hot.xpath('.//a/@href')[0]
        #print(str(title)+":"+str(count)+":"+str(href))
        all = [str(title),str(count)]
        csv_wr.writerow(all)
    except Exception as er:
        print(er)
