import urllib2
import os.path
import shutil


url = 'http://weibo.com/u/1302237377?is_all=1'
req = urllib2.Request(url)
response = ulrlib2.urlopen(req)
html = response.read()

file_object = open('index.html', 'w')
file_object.write(html)
file_object.close()
