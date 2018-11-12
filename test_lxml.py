from lxml import etree

text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''
html = etree.HTML(text) #初始化生成一个XPath解析对象
result=etree.tostring(html,encoding='utf-8')   #解析对象输出代码
print(type(html))
print(type(result))
print(result.decode('utf-8'))


try:
    for result in html.xpath('//li'):   # 查找li标签的内容
        print(result.xpath('.//@class')[0]) # 在当前标签下，继续查找a后面的href标签的内容
        print(result.xpath('.//a/@href')[0]) # 在当前标签下，继续查找a后面的href标签的内容
        print(result.xpath('.//a[@href="link1.html"]')[0].text.strip())
except Exception as er:
    print("ERROR:"+str(er))

print("----------------")


for result in html.xpath('//li'):   # 查找li标签的内容
    try:
        print(result.xpath('.//@class')[0]) # 在当前标签下，继续查找a后面的href标签的内容
        print(result.xpath('.//a/@href')[0]) # 在当前标签下，继续查找a后面的href标签的内容
        print(result.xpath('.//a[@href="link2.html"]')[0].text.strip())
    except Exception as er:
        print("ERROR:"+str(er))
        continue
