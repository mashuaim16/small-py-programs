#-*- coding:utf-8 -*-

import requests
from lxml import etree
import time

for i in range(1,5):

	url1 = 'http://sz.xiaozhu.com/search-duanzufang-p%d-0/'%i
	data1 = requests.get(url1).text
	r = etree.HTML(data1)
	titles = r.xpath('//*[@id="page_list"]/ul/li/div[2]/div/a/span/text()')
	time.sleep(2)



	rent = r.xpath('//*[@id="page_list"]/ul/li')
	for div in rent:
		title = div.xpath('./div[2]/div/a/span/text()')[0]
	#print ('租房标题：'，title)
		price = div.xpath('./div[2]/span[1]/i/text()')[0]
		describle = div.xpath('./div[2]/div/em/text()')[0].strip()
		photo = div.xpath('./a/img/@lazy_src/')[0]

		print ("{}-->{}-->{}\n{}".format(title,price,describle,photo))



    


