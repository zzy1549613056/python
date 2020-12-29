#!/usr/local/bin/python3
from tkinter import *
from tkinter import ttk
import re,json
from urllib import parse,request

class Application(Frame):
    #src_price = StringVar()
    
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.src_price = StringVar()
        self.message = StringVar()
        self.createView()

    def  createView(self):
        self.priceInput = Entry(self,textvariable = self.src_price)
        self.src_price.set('100')
        self.srcBox = ttk.Combobox(self)
        self.srcBox['values'] = ('美元USD','人名币CNY','欧元EUR','英镑GBP','韩元KRW','港币HKD','日元JPY')
        self.srcBox.current(0)
        self.tarBox = ttk.Combobox(self)
        self.tarBox['values'] = ('美元USD','人名币CNY','欧元EUR','英镑GBP','韩元KRW','港币HKD','日元JPY')
        self.tarBox.current(1)
        self.button = Button(self,text='确认',command=self.fun1)
        self.msg = Message(self,textvariable = self.message,width=300)
        self.priceInput.grid(row=0,column=0)
        self.srcBox.grid(row=0,column=1)
        self.tarBox.grid(row=1,column=1)
        self.button.grid(columnspan=2)
        self.msg.grid(columnspan=2)

    def fun1(self):
        srcEn = re.match(r'\W+(\w+)',self.srcBox.get(),re.A).group(1)
        srcCn = re.match(r'(\W+)\w+',self.srcBox.get(),re.A).group(1)
        tarEn = re.match(r'\W+(\w+)',self.tarBox.get(),re.A).group(1)
        tarCn = re.match(r'(\W+)\w+',self.tarBox.get(),re.A).group(1)
        price = float(self.priceInput.get())
        exchange = float(self.exchange(srcEn,tarEn))
        resPrice = round(price*exchange,2)
        if resPrice >0:
            self.message.set("%s %s = %s %s"%(price,srcCn,resPrice,tarCn))
        else:
            self.message.set("查询失败")

    @staticmethod
    def exchange(src,tar):
        key = 'd5176afd66beeca2af2a355129241ec3'
        url = "http://op.juhe.cn/onebox/exchange/currency"
        params ={
            'key': key,
            'from': src,
            'to': tar
        }
        data = parse.urlencode(params)
        req = request.Request(url)
        with request.urlopen(req,data.encode()) as f:
            res_json = f.read().decode()
        res = json.loads(res_json)
        #print (res)
        if res:
            if res['reason'] == '查询成功!':
                print ('%s to %s :%s'%(src,tar,res['result'][0]['exchange']))
                return res['result'][0]['exchange']
            else:
                print("%s:%s"%(res['error_code'],res['reason']))
                return -1
        else:
            print('查询接口失败')
            return -2

app = Application()
app.master.title('汇率查询py3 1.0')
app.mainloop()