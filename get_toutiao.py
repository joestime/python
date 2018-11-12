import urllib.request
import re

url = "https://www.toutiao.com/"

data = urllib.request.urlopen(url, timeout=15).read() #动态js抓不到内容
data = data.decode("utf-8")

part = '<a href="[^\s]*" target="[^\s]*" class="[^\s]*">(.*?)</a>'

results = re.compile(part).findall(data)

print(results)
