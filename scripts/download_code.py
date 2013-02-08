from xml.dom import minidom
import urllib2

xmldoc = minidom.parse('download_code.xml')
itemlist = xmldoc.getElementsByTagName('item') 
for s in itemlist :
    url = s.firstChild.nodeValue
    response = urllib2.urlopen(url).read()
    print "Downloaing..."
    print url
    f = open('../source/downloads/code/'+s.attributes['name'].value,'w')
    f.write(response)
print 'end downloading source code'
