import urllib.request
import re


def use_proxy(url, proxy_addr):
    proxy = urllib.request.ProxyHandler({"http":proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    return data

proxy_addr = ["119.183.220.224:8888", ""]
url = "https://www.baidu.com"
data = use_proxy(url, proxy_addr)

print(data)
print("--------")


import requests
from chardet import detect
from lxml import etree

url = 'https://blog.csdn.net/'

resp = requests.get(url, timeout=15)
encoing = detect(resp.content).get('encoding')
html = resp.content.decode(encoing, 'ignore')

tree = etree.HTML(html)

for blog in tree.xpath('//li[@class="clearfix"]'):
    blog_name = blog.xpath('.//div[@class="title"]/h2/a')[0].text.strip()
    print(str(blog_name))
