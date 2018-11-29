# coding:utf-8

import requests
from lxml import etree
from chardet import detect
import csv
import time
url = 'http://top.baidu.com/buzz?b=1&fr=20811'

while 1 == 1:
    resp = requests.get(url, timeout=15)
    encoing = detect(resp.content).get('encoding')
    html = resp.content.decode(encoing,'ignore')
## UnicodeDecodeError: 'gb2312' codec can't decode byte 0x86 in position 20164: illegal multibyte sequence
## 网页有 非法字符你需要加上ignore
    tree = etree.HTML(html)
    tm = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    csv_file = open('baidu_hotspot.csv', 'a', encoding='utf-8', newline='')
    csv_wr = csv.writer(csv_file)
    for hot in tree.xpath('//table[@class="list-table"]//tr'):
        try:
            title = hot.xpath('.//td[@class="keyword"]//a[@class="list-title"]')[0].text.strip()
            count = hot.xpath('.//td[@class="last"]//span[1]')[0].text.strip()#第一个span元素
            #href = hot.xpath('.//a/@href')[0]
            #print(str(title)+":"+str(count)+":"+str(href))
            new = hot.xpath('.//td[@class="keyword"]/span/@class')
            if new:
                new = 'NEW'
            else:
                new = ''
            all = [str(tm),str(title),str(count),str(new)]
            csv_wr.writerow(all)
        except Exception as er:
            print(er)
            continue
    time.sleep(900)