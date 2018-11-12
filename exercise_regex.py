import re

string = "i have two hourses, but i have not a lover"
pat1 = 'h[a-z].e'
results = re.search(pat1, string)
print(results)

pat1 = 'h.*e'
results = re.search(pat1, string)
print(results)

pat1 = 'h.*?e'
results = re.search(pat1, string)
print(results)

pat1 = 'h.+?e'
results = re.search(pat1, string)
print(results)

string = '<a href="http://www.baidu.com">baidu</a>'
part = "[a-zA-Z]+://[^\s]*[.com|.cn]"
results = re.compile(part).findall(string)
print(results)


string = "564813535789546135"
part = "[1][2-9]*"
results = re.compile(part).findall(string)
print(results)

part = "[1]\d{9,10}"
results = re.compile(part).findall(string)
print(results)

string = "023-62375888,(023)62547859,02385643354,10086,0731-66558897"
part = "\(0[0-9]{2,3}\)[0-9]{7,8}|0[0-9]{2,3}-[0-9]{7,8}|[0-9]+"
results = re.compile(part).findall(string)
print(results)