from lxml import etree
import re

url = 'D:/FDownload/toutiao.html'


html = etree.parse(url, etree.HTMLParser())
result = etree.tostring(html)

tree = etree.HTML(result)
i = 0


#for book in tree.xpath('//div[@id="content"]//div[@class="info"]'):
for book in tree.xpath('//li[@ga_event="feed_item_click"]'):
    i = i+1
    ##title = book.xpath('.//div[@class="title-box"]/a/text()')#存在其他格式的title
    links = book.xpath('.//div[@class="title-box"]/a/@href')
    part ='https://www.toutiao.com/item/(.*?)/'
    results = re.compile(part).findall(links[0])
    link =  'http://www.365yg.com/i'+str(results[0])+'/#mid=1602970284435470'
    bofang = book.xpath('.//div[@class="y-left"]/a[1]/text()')
    shijian = book.xpath('.//div[@class="y-left"]/span/text()')

    #if re.compile('万').findall(bofang[0]) :
        #print(link)
        ##print(i,'--',link,'--',bofang,'---',shijian)
    print(link,',',bofang)
    #print(bofang)



for book in tree.xpath('//li[@class="profile-video-list__card-list__wrapper"]'):
    i = i + 1
    ##title = book.xpath('.//div[@class="title-box"]/a/text()')#存在其他格式的title
    links = book.xpath('.//div[@class="video-info__description"]/a/@href')
    part = 'http://www.365yg.com/item/(.*?)/'
    results = re.compile(part).findall(links[0])
    if results:
        link = 'http://www.365yg.com/i' + str(results[0]) + '/#mid=1602970284435470'
        bofang = book.xpath('.//span[@class="video-footer"]/span[1]/a/span/text()')
        shijian = book.xpath('..//span[@class="video-footer"]/span[2]/text()')
        #if re.compile('万').findall(bofang[0]) :
            #print(link)
            ##print(i,'--',link,'--',bofang,'---',shijian)
        print(link,',',bofang)
        #print(bofang)



for book in tree.xpath('//li[@ga_event="click_feed_word"]'):
    i = i + 1
    ##title = book.xpath('.//div[@class="title-box"]/a/text()')#存在其他格式的title
    links = book.xpath('.//div[@class="y-left lbox"]/a/@href')
    part = 'https://www.toutiao.com/item/(.*?)/'
    results = re.compile(part).findall(links[0])
    if results:
        link = 'http://www.365yg.com/i' + str(results[0]) + '/#mid=1602970284435470'
        bofang = book.xpath('.//div[@class="y-left"]/span[1]/text()')
        #shijian = book.xpath('..//span[@class="video-footer"]/span[2]/text()')
        #if re.compile('万').findall(bofang[0]) :
            #print(link)
            ##print(i,'--',link,'--',bofang,'---',shijian)
        print(link,',',bofang)
        #print(bofang)
