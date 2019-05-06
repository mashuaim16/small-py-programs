# -*- coding: utf-8 -*-
import urllib2
import json
from city import city

cityname = raw_input ('你想要查哪个城市的天气？\n')
citycode = city.get(cityname)
if citycode:
	try:
		url = ('http://www.weather.com.cn/data/cityinfo/%s.html'% citycode)
		content = urllib2.urlopen(url).read().decode('utf-8')
		data = json.loads(content)
		result = data['weatherinfo']
		str_temp = ('%s\n%s ~ %s') % (
		result['weather'],
		result['temp1'],
		result['temp2'],
		)
		print (str_temp)
	except:
		print 'Request Failed'
else:
	print 'The city is not found'