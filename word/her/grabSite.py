import httplib
import urllib2
start=1
end=1000
increment =1000
site='http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/TV/2006/{0}-{1}'
print site.format( start, end) 


request  = urlib2.Request(site.format( start, end))
request.add_header('User-Agent', 'grabbing-text/1.0')
request.add_header('Accept-encoding', 'gzip') 

opener = urllib2.build_opener()
feeddata=opener.open(request).read() 
