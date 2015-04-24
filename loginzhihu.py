# -*- coding:utf-8 -*-
import urllib,urllib2,re,cookielib

email=raw_input('email:')
password=raw_input('password:')
url="http://www.zhihu.com/"
data1=urllib2.urlopen(url).read().decode('utf-8')
_xsrf=re.findall(r'<input type="hidden" name="_xsrf" value="(.*?)"/>',data1)
print _xsrf[0]
values={
        '_xsrf':_xsrf,
        'email': email,
        'password':password,
        'rememberme':'y'
}
data2=urllib.urlencode(values)
headers={
        'Accept':'*/*',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',		
		'Host':'www.zhihu.com'
}
cookie=cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handler)
url=url+'login'
request=urllib2.Request(url,data2,headers)
data3=opener.open(request).read()
print data3