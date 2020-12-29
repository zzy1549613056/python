#!/usr/local/bin/python3

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import ssl 
ssl._create_default_https_context=ssl._create_unverified_context

class MyHTMLParser(HTMLParser):

    event_flag = 0
    time_flag = 0
    local_flag = 0


    @staticmethod
    def _attr(attrlist,attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
            return None

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and self._attr(attrs,'class') == 'event-title':
            self.event_flag = 1
            print('***************')
        if tag == 'span' and self._attr(attrs,'class') == 'event-location':
            self.local_flag = 1
        if tag == 'time':
            self.time_flag = 1

    def handle_endtag(self, tag):
        self.event_flag = 0
        self.local_flag = 0
        self.time_flag = 0
        #self.time_flag2 = 0

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self.event_flag == 1: 
            print("会议：%s"%data)
        if self.local_flag == 1: 
            print("地点：%s"%data) 
        if self.time_flag == 1 and self.lasttag == 'time':
            print("时间：%s"%data,end=' ') 
        if self.time_flag == 1 and self.lasttag == 'span':
            print("%s"%data) 

        

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

if __name__ == '__main__':
    with request.urlopen("https://www.python.org/events/python-events/") as f:
        data = f.read().decode()
    parser = MyHTMLParser()
    parser.feed(data)