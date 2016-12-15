#!/usr/bin/python
# -*- coding: <utf-8> -*-

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

    #encode的作用是将unicode编码转换成其他编码的字符串
    #decode的作用是将其他编码的字符串转换成unicode编码
    #unicodecontent = pagecontent.decode("utf-8")

    #找出所有class="WB_detail"的div标记
    #re.S是任意匹配模式，也就是.可以匹配换行符
    rawItems = re.findall('<div class="WB_detail">.*?<div class="WB_from S_txt2">(.*?)</div>.*?<div class="WB_text W_f14" node-type="feed_list_content">(.*?)</div>',pagecontent,re.S)
    items = []
    for item in rawItems:
        # item 中第一个是div的标题，也就是时间
        # item 中第二个是div的内容，也就是内容
        items.append([item[0],item[1])
    return items




htmlItems = GetWBDetail()

f = open('v/index.html', 'w')
f.write(htmlItems)
f.close()

print "Done..."
