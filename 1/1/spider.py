#!/usr/bin/python
import urllib
import urllib2
import cookielib

cj=cookielib.CookieJar() 
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 

#values = {"Username":"admin","checkEn":"0","Password":"13851518462"}
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
#data = urllib.urlencode(values)
url = "https://www.douban.com/"
header = {'User-Agent' : user_agent}
req = urllib2.Request(url,headers=header)
response = urllib2.urlopen(req)
print response.read()
print "cookie:%s" %cj._cookies.values()