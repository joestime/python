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


http://review.qunar.com/api/h/hotelMultiTitles?seq=dali_4010,dali_2002,dali_2008,dali_2009,dali_2033,dali_2158,dali_2173,dali_2193,dali_2198,dali_2227,dali_2243,dali_2251,dali_2279,dali_2282,dali_2284&requestTime=1542002624707&__jscallback=jQuery183024834412922514804_1542002624125&_=1542002624707
https://qta.qunar.com/user/order/data/www/price/query?wrapperId=hta100nl01j&hotelSeq=dali_4010&productId=14950592660_1588566&checkInDate=2018-11-14&checkOutDate=2018-11-15&QHFP=KZB_B3200D09&bd_ssid=&bd_sign=&cityUrl=dali&price=186&productType=1&from=kezhan&priceCut=0&cashback=0&reduce=0&taxes=0&inventoryType=1&bkts=1542001461&bksign=34dbcc225f14d46ccdd1db0d920f957c82a741db&productUniqKey=WEBSITE_MS_hta10c5vo3a_PTNjM1ODM5OTA0&sleepTask=&ex_track=null&_=1542001463550