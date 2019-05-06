#coding:utf8


import requests
from lxml import etree
import time #倒入时间模块

url = 'https://movie.douban.com/subject/26942674/'
data = requests.get(url).text
s = etree.HTML(data)

film_name = s.xpath('//*[@id="content"]/h1/span[1]/text()') #film name
director = s.xpath('//*[@id="info"]/span[1]/span[1]/text()') #director name
actor=s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')#主演
movie_time=s.xpath('//*[@id="info"]/span[13]/text()')#片长

#由于导演有时候不止一个人，所以我这里以列表的形式输出
ds = []
for d in director:
	ds.append(d)

#由于演员不止一个人，所以我这里以列表的形式输出
atr = []
for a in actor:
	atr.append(a)

print ('Film name:', film_name)
print ('director:', ds)
print ('staring:', atr)
print ('Time length:', movie_time)
