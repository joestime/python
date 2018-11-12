# ecoding:utf-8

from lxml import etree
import requests
from chardet import detect
import json

urls = ['https://list.jd.com/list.html?cat=1319,1525,7057&ev=exbrand_8067&sort=sort_rank_asc&trans=1&JL=3_%E5%93%81%E7%89%8C_%E5%A5%BD%E5%A5%87%EF%BC%88Huggies%EF%BC%89#J_crumbsBar',
       'https://list.jd.com/list.html?cat=1319,1525,7057&ev=exbrand_8454&sort=sort_rank_asc&trans=1&JL=2_1_0#J_crumbsBar']
for url in urls:
    resp = requests.get(url, timeout=15)
    encoing = detect(resp.content).get('encoding')
    html = resp.content.decode(encoing)
    tree = etree.HTML(html)
    for goods in tree.xpath('//*[@id="plist"]//li[@class="gl-item"]'):
        shop = goods.xpath('.//div[@class="p-shop"]/span/a')
        name = goods.xpath('.//div[@class="p-name"]//em/text()')
        sku = goods.xpath('.//div/@data-sku')[0]
        price_url = "https://p.3.cn/prices/mgets?skuIds=J_" + sku

        resps = requests.get(price_url)
        content = resps.content
        result = json.loads(content)

        j_price = result[0]["p"]
        print(str(name)+":"+str(j_price)+":"+str(sku)+":"+str(shop))
