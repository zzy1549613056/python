#对爬虫做了多进程处理

#!/usr/local/bin/python3
import re 
import requests
from math import ceil
from multiprocessing import Process,Pool

idList = []
count = 0
url_index = 'http://www.hzbb315.com/news/index.html'
url_news = 'http://www.hzbb315.com/news/index/p/'
url_detail = 'http://www.hzbb315.com/news/detail/id/'

r = requests.get(url_index).text

page_match = re.search(r'共 (\d+) 条记录',r).group(1)
if page_match:
    pages = ceil(int(page_match)/20)
else:
    print('获取页数失败') 
    pages = 0
print('共有'+str(pages)+'页')   

def getId(url):
    news_res = requests.get(url).text
    new_id_List = re.findall(r'\<a href=\"\/news\/detail\/id\/(.*?)\"',news_res)
    return new_id_List

def callback1(res):
    global idList
    idList += res

def getHtml(url):
    detail_res = requests.get(url).text
    content_match = re.search(r'\<div class\=\"contentdetail\"\>(.*)\<p.*\<\/p\>\s*\<\/div\>',detail_res,flags=re.S)
    title_match = re.search(r'\<div class\=\"pname\"\>(.*?)\<\/div\>',detail_res,flags=re.S)
    if content_match:
        with open('news.txt', 'a') as f:
            f.write(title_match.group(1))
            f.write(content_match.group(1))
            f.write('\r\n')
        return True
    else:
        print('该页面为空')  
        return False   

def callback2(res):
    global count
    if res:
        count += 1
            


p1 = Pool(8)
p2 = Pool(20)

for page in range(pages):
    url = url_news + str(page+1) + '.html'
    p1.apply_async(getId,args=(url,),callback=callback1)

p1.close()
p1.join()    
print(len(idList))




for id in idList:
    url = url_detail + id
    p2.apply_async(getHtml,args=(url,),callback=callback2)
p2.close()
p2.join()   

print(count)             




