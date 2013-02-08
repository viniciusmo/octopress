from xml.dom import minidom
import urllib2

xmldoc = minidom.parse('scripts/data/download_code.xml')
itemlist = xmldoc.getElementsByTagName('item') 
for s in itemlist :
    url = s.firstChild.nodeValue
    try:
    	urllib.urlcleanup();
    	response = urllib2.urlopen(url).read()
    	print "Downloaing..."
    except urllib2.HTTPError, e:
    	print e.code
    	print e.msg
    	print e.headers

    print url
    f = open('source/downloads/code/'+s.attributes['name'].value,'w')
    f.write(response)
print 'end downloading source code'
