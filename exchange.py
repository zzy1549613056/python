#!/usr/bin/python3
# coding:utf-8
import urllib,json
from tkinter import *
import ttk
import re

def exchange(src,tar):
	key = 'd5176afd66beeca2af2a355129241ec3'
	url = "http://op.juhe.cn/onebox/exchange/currency"
	params = {
		'key' : key,
		'from':src,
		'to':tar
	}

	data = urllib.urlencode(params)
	res_json = urllib.urlopen("%s?%s" %(url,data)).read()
	res = json.loads(res_json)
	if res:
		if res['error_code'] == 0:
			print ("%s to %s %s"%(src,tar,res['result'][0]['result']))
			return res['result'][0]['result']
		else:
			print ('%s:%s' %(res['error_code'],res['reason']))
			return -1
	else:
		print ('查询接口失败')
		return -2

def EX():
	src_en = re.match(r'\W+(\w+)',src_box.get()).group(1)
	src_cn = re.match(r'(\W+)\w+',src_box.get()).group(1)
	tar_en = re.match(r'\W+(\w+)',tar_box.get()).group(1)
	tar_cn = re.match(r'(\W+)\w+',tar_box.get()).group(1)
	num = float(e1.get())
	exchang = float(exchange(src_en,tar_en))
	res = exchang * num
	print(exchang,res)
	if res > 0:
		message.set("%s %s = %s %s"%(num,src_cn,res,tar_cn))
	else:
		message.set("error")

root = Tk()
root.title("汇率查询1.1")
src_num = StringVar()
message = StringVar()
src_num.set("100")
e1 = Entry(root,textvariable=src_num)
src_box = ttk.Combobox(root)
src_box['values'] = ('美元USD','人名币CNY','欧元EUR','英镑GBP','韩元KRW','港币HKD','日元JPY')
src_box.current(0)
tar_box = ttk.Combobox(root)
tar_box['values'] = ('美元USD','人名币CNY','欧元EUR','英镑GBP','韩元KRW','港币HKD','日元JPY')
tar_box.current(1)
button = Button(root,text="确认",command=EX)
msg = Message(root,textvariable=message,width=300)

e1.grid(row=0,column=0)
src_box.grid(row=0,column=1)
tar_box.grid(row=1,column=1)
button.grid(row=2,column=0)
msg.grid(columnspan=2)
root.mainloop()



