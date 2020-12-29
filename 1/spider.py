#!/usr/local/bin/python3
import requests,json
from bs4 import BeautifulSoup
from multiprocessing import Pool
import time,re


job = 'python'
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

def MyGet(dic,*args):
    if type(dic) != dict:
        print('传入的不是字典',dic)
        return None
    for i in args:
        dic = dic.get(i)
        if dic == None:
            print('字典没有属性%s'%i)
            break
    return dic        
        


header = {
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1) AppleWebKit/534.48.3 \
    (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
    # "cookie":"SEARCH_ID=c650ee52dd9e484684f9be970701c476; user_trace_token=20180510190715-1d14dcac-9d04-43eb-a8db-20b43d915e5d; _ga=GA1.2.1615720459.1525950437; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525950437,1526005646,1526005663,1526006382; LGUID=20180510190717-4d103d70-5442-11e8-81e3-5254005c3644; _gid=GA1.2.1729612819.1525950440; WEBTJ-ID=20180511102725-1634d06425c229-097126130293d78-4a5268-1296000-1634d06425d37f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1526118636; LGRID=20180512175036-eb7f61c3-55c9-11e8-8228-5254005c3644; JSESSIONID=ABAAABAACEBACDGA417E82E9308B0D410A63729F722FE93; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; X_HTTP_TOKEN=68d861a88fe75eb319bb63d09908e516; LGSID=20180512173502-bee84196-55c7-11e8-8224-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_java%3Fpx%3Ddefault%26city%3D%25E5%258C%2597%25E4%25BA%25AC; _gat=1"
}






def spider(page,job,cookie):
    params={
        'first': 'true',
        'kd': job,
        'pn': page
    }
    temp = []
    s = requests.Session()
    r = s.post(url,data=params,headers=header,cookies=cookie)
    #处理部分返回错误代码
    #try:
    res_dic = MyGet(r.json(),'content','positionResult','result')
    if res_dic == None:
        print(r)
        return []
    for _ in res_dic:
        print(_['positionId'])
        detail = getJobDetail(_['positionId'],cookie)
    
       # b1 = re.match(r'.*?<dd class="job_bt">(.*?)</dd>',r)
        #if b1 == None:
           # print ("$%$%^",r)

        

        #print(_['positionId'])
        temp_dict={
            'companyId':_['companyId'],
            'companyName':_['companyShortName'],
            'positionName':_['positionName'],
            'education':_['education'],
            'city':_['city'],
            'salary':_['salary'],
            'workYear':_['workYear'],
            'detail':detail
            }
        
        temp.append(temp_dict)
# except json.decoder.JSONDecodeError as e:
    #print("#####",r.text)
#finally:
    print (page)
    return temp
##获取职位信息条数
def getCount(job,cookie):
    params={
    'first': 'true',
    'kd': job,
    'pn': 1
    }
    r = requests.post(url,data=params,headers=header,cookies=cookie)
    print(r.text)
    return MyGet(r.json(),'content','positionResult','totalCount')


##获取职位详细信息
def getJobDetail(jobId,cookie):
    url = "https://www.lagou.com/jobs/" + str(jobId) + ".html"
    header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1) AppleWebKit/534.48.3 \
    (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
    }
    r = requests.get(url,headers=header,cookies=cookie)
    bs = BeautifulSoup(r.text,"lxml")
    b = bs.find('dd',class_="job_bt").div.get_text()
 
    tempDict = b.replace('\n','').replace('\xa0','').replace(' ','')
    return tempDict

    #print('#######',jobId)
    #print('$$$$$$$$',b.replace('\n','').replace('\xa0',''))
    #return b.replace('\n','').replace('\xa0','')

cookie={
    '_ga': 'GA1.2.56989985.1530506811',
    '_gid': 'GA1.2.144992989.1530506812',
    'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1530506812',
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1530502624',
    'JSESSIONID':  'ABAAABAAAFCAAEG3EF64351F5F144883880E0019D78C1FB',
    'LGRID':   '20180702124651-efd64ffb-7db2-11e8-bcb7-525400f775ce',
    'LGUID':   '20180702124651-efd6505f-7db2-11e8-bcb7-525400f775ce',
    'SEARCH_ID':   '5208d34503e740caaba9160a0174537f',
    'TG-TRACK-CODE':   'index_search',
    'user_trace_token':    '20180702124650-dab4edad-2ffa-4fca-8ea2-ea3a6abd862f'
}
# cookie = {"JSESSIONID":"ABAAABAAAFCAAEG3EF64351F5F144883880E0019D78C1FB","TG-TRACK-CODE":"index_search","SEARCH_ID":"c64c2febcd54424ab611f61e8d51a51e","user_trace_token":"20180702124650-dab4edad-2ffa-4fca-8ea2-ea3a6abd862f"}

s = requests.Session()
r = s.get('https://www.lagou.com',headers=header)
# cookies = s.cookies.get_dict()
jobCount = getCount(job,cookie)
print("获取工作总数",jobCount)
page = int(jobCount/15) + 1
P = Pool(200)
resPool = []
start = time.time()
for i in range(1,page+1):
    resPool.append(P.apply_async(spider, args=(i,job,cookie)))

P.close()
P.join()
w_dict=[]
for res in resPool:
    w_dict.extend(res.get())
end = time.time()
print('耗时：%s'%(end-start))
with open(job+'职业信息.txt','w') as w:
    w.write(json.dumps(w_dict,ensure_ascii=False))



####拉手网一些问题，
##1.请求Json数据有小概率返回html代码
##2.必须要有cookie,不然会5次请求后出现频繁操作的警告
##3.职位信息totalCount过多的情况下，获取的职位信息会小于总条数（不知道登陆后会不会有改善）
##4.当页数大于一定值，会获取重复json职位信息
##5.获取详细信息页面时，经常性出现cookie问题导致的回到登陆界面，导致程序中断，需要动态cookie


