import requests
from lxml import etree
from chardet import detect

url = 'https://market.m.taobao.com/apps/abs/10/363/f89efd?spm=a212er.steins1370018.134456.18.4510yHtbyHtb4o&wh_weex=true&data_prefetch=true&wx_navbar_transparent=true&psId=1368036'

resp = requests.get(url, timeout=15)
ecoding = detect(resp.content).get('encoding')
html = resp.content.decode(ecoding)
tree = etree.HTML(html)


for imgs in tree.xpath('//div[@class="main-img-box"]'):
    pic = imgs.xpath('.//img/@src')[0]
    print(pic)
    print(1)
#又是js代码，抓不到图片