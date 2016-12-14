import urllib2
import os.path
import shutil


url = 'http://baike.baidu.com/item/ubuntu'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
html = response.read()

file_object = open('v/index.html', 'w')
file_object.write(html)
file_object.close()
