#!/usr/bin/python


import urllib2
import urllib2
import re


def GetWBDetail():
    url = 'http://weibo.com/u/1302237377?is_all=1'
    #User-Agent in my computer
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    pagecontent = response.read()

    #unicodecontent = pagecontent.decode("utf-8")

    rawItems = re.findall('<div class="WB_detail">.*?<div class="WB_from S_txt2">(.*?)</div>.*?<div class="WB_text W_f14" node-type="feed_list_content">(.*?)</div>',pagecontent,re.S)
    items = []
    for item in rawItems:
        print item[0]
        print item[i]
        print "*****************************"
        items.append([item[0],item[1]])
    return items


htmlItems = GetWBDetail()

f = open('v/index.html', 'w')
for item in htmlItems:
    f.write("".join(item))
#f.write(htmlItems)
f.close()

print "Done..."
print "Done..."
print "Done..."
print "Done..."
