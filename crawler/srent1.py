#-*- coding:utf-8 -*-
import requests
from lxml import etree
import time

for i in range(1,6):
    url3 = 'http://sz.xiaozhu.com/search-duanzufang-p{}-0/'.format(i)
    data3 = requests.get(url3).text
    h = etree.HTML(data3)
    home = h.xpath('//*[@id="page_list"]/ul/li')
    time.sleep(2)#注意，小猪在发爬虫方面做得比较好，防止被封IP就加个睡眠吧
    for div in home:
        title = div.xpath('./div[2]/div/a/span/text()')[0] #标题
        price = div.xpath('./div[2]/span[1]/i/text()')[0]#价格
        describle = div.xpath('./div[2]/div/em/text()')[0].strip()#描述
        photo = div.xpath('./a/img/@lazy_src/')[0]
        time.sleep(2)
        print ("{}-->{}-->{}\n{}".format(title,price,describle,photo))

