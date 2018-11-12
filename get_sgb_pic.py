import requests
from chardet import detect
from lxml import etree
import urllib.request

for m in range(10, 500):
    url = 'https://bbs.shuiguobang.com/forum-357-'+ str(m)+ '1.html'

    resp = requests.get(url, timeout=15)
    encoing = detect(resp.content).get('encoding')
    html = resp.content.decode(encoing, 'ignore')

    tree = etree.HTML(html)
    for bodys in tree.xpath('//tbody[contains(@id, "normalthread")]'):
        body = bodys.xpath('.//tr/th/a[2]/@href')  # get 帖子 links
        name = bodys.xpath('./tr/th/a[2]')[0].text.strip()  # get 帖子主题
        sub_url = 'https://bbs.shuiguobang.com/' + str(body[0])  # 组装帖子link

        # 访问帖子内容
        resp = requests.get(sub_url, timeout=15)
        encoing = detect(resp.content).get('encoding')
        html = resp.content.decode(encoing, 'ignore')
        sub_tree = etree.HTML(html)
        print(sub_url)

        j = 0
        for posts in sub_tree.xpath('//*[@id="postlist"]//div[contains(@id, "post")]'):
            pic = posts.xpath('.//*//img[contains(@id, "aimg")]/@file')
            if pic:  # 不为空list
                j = j + 1
                for i in range(0, len(pic)):
                    try:
                        thisurl = pic[i]
                        file = "C:/Python files/" + name +str(m)+ str(j) + str(i) + ".jpg"
                        urllib.request.urlretrieve(thisurl, file)  # 存为文件
                    except Exception as e:
                        print(e)



#2.查询所有Blog节点值中带有 cn 字符串并且属性ID值中有01的Person节点
#Xpath表达式：/Root//Person[contains(Blog,'cn') and contains(@ID,'01')]