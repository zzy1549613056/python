#!/usr/bin/python
# coding:utf-8
#哈哈
import re
t = '9:42:07'
e = 'bill.ga _tes@microsoft.com'
mail_name = "<Tom Paris> tom@voyager.org"
re_time = re.compile(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:([0-5][0-9])\:([0-5][0-9])$')
re_mail = re.compile(r'^([a-zA-Z0-9\_\-\.\s]+)(\@[a-zA-Z0-9\_\-\.]+)(\.[a-z]{1,3})$')
re_mail_name = re.compile(r'^<([a-zA-Z0-9\_\-\.\s]+)>([a-zA-Z0-9\_\-\.\s]+)(\@[a-zA-Z0-9\_\-\.]+)(\.[a-z]{1,3})$')
m = re_time.match(t)
name = re_mail_name.match(mail_name).group(1)
m1 = re_mail.match(e)
print m.groups()
print m1.groups()
print name
