#coding:utf-8

from lxml import etree
import requests
from chardet import detect

url = 'https://book.douban.com/'
resp = requests.get(url, timeout=15)
ecoding = detect(resp.content).get('encoding')
html = resp.content.decode(ecoding)
tree = etree.HTML(html)
i = 0
#for book in tree.xpath('//div[@id="content"]//div[@class="info"]'):
for book in tree.xpath('//div[@id="content"]/descendant::div[@class="info"]'):
    i = i+1
    title = book.xpath('.//h4[@class="title"]')[0].text.strip()#存在其他格式的title
    author = book.xpath('.//span[@class="author"]')[0].text.strip()
    print(i, u'《', title, u'》', '\t', '--',author)

