from xml.dom import minidom
import urllib2
import urllib

xmldoc = minidom.parse('scripts/data/download_code.xml')
itemlist = xmldoc.getElementsByTagName('item') 
for s in itemlist :
    url = s.firstChild.nodeValue
    try:
    	req = urllib2.Request(url)
    	print "Downloaing..."
    	print url
    	response = urllib2.urlopen(req).read()
    except urllib2.HTTPError, e:
    	print "Error downloading " + url
    f = open('source/downloads/code/'+s.attributes['name'].value,'wb')
    f.write(response)
print 'End downloading source code'
