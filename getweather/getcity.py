import urllib2
url1 = 'http://m.weather.com.cn/data3/city.xml'
content1 = urllib2.urlopen(url1).read()
print content1 [:3]
provinces = content1.split(',')
result = 'city = {\n'
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
	p_code = p.split('|')[0]
	url2 = url % p_code
	content2 = urllib2.urlopen(url2).read()
	print content2 [:3]
	cities = content2.split(',')
	for c in cities:
		c_code = c.split('|')[0]
		url3 = url % c_code
		content3 = urllib2.urlopen(url3).read()
		districts = content3.split(',')
		print content3[:3]
		for d in districts:
			d_pair = d.split('|')
			d_code = d_pair[0]
			name = d_pair[1]
			url4 = url % d_code
			content4 = urllib2.urlopen(url4).read()
			code = content4.split('|')[1]
			line = " '%s': '%s', \n" % (name,code)
			result += line
			print name + ':' + code
result += '}'
f = file('cityy.py','w')
f.write(result)
f.close()