#-*- coding:utf-8 -*-

import requests
from lxml import etree
import time

results = []

for i in range(10):
    url = 'https://book.douban.com/top250?start={}'.format(i*25)
    data = requests.get(url).text
    f = etree.HTML(data)
    books = f.xpath('//*[@id="content"]/div/div[1]/div/table')
    for div in books:
        title = div.xpath('./tr/td[2]/div[1]/a/@title')[0]
        score = div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
        comment = div.xpath('./tr/td[2]/p[2]/span/text()')
        num = div.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip('(').strip().strip(')')
        href = div.xpath('./tr/td[2]/div[1]/a/@href')[0]
        time.sleep(1) #加个睡眠，防止IP被封
     

        if len(comment)>0:
            result = '{}-->{}-->{}-->{}-->{}'.format(title,score,comment[0],num,href)
        else:
            result = '{}-->{}-->{}-->{}'.format(title,score,num,href)

        results.append(result)
   
output = open('top250 books','w')
output.writelines(results)
output.close()