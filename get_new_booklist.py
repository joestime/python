#coding:utf-8

from lxml import etree
import requests
from chardet import detect

url = 'https://book.douban.com/latest?icn=index-latestbook-all'
resp = requests.get(url, timeout=15)
ecoding = detect(resp.content).get('encoding')
html = resp.content.decode(ecoding)
tree = etree.HTML(html)
i = 0
for book in tree.xpath('//div[@id="content"]//div[@class="detail-frame"]'):
    i = i+1
    title = book.xpath('.//h2/a')[0].text.strip()
    author = book.xpath('.//p[@class="color-gray"]')[0].text.strip()
    print(i, u'《', title, u'》', '\t', '--',author)

