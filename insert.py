#!/usr/bin/python
# coding=utf-8
import re
import MySQLdb
db = MySQLdb.connect('localhost','root','242501','test',charset='utf8')
cur = db.cursor()
sql = """CREATE TABLE coinlist(
         name CHAR(30) NOT NULL,
         code CHAR(10) unique)"""
try:
	cur.execute(sql)
except:
	db.rollback()

with open('list.txt','r')as f:
	line = f.readlines()
	for i in range(0,len(line)):
		line[i] = line[i].strip()
		if re.match(r'^\"name\"\:\s\"(.+)\"',line[i]):
			name = re.match(r'^\"name\"\:\s\"(.+)\"',line[i]).group(1)
			code = re.match(r'^\"code\"\:\s\"(.+)\"',line[i+1].strip()).group(1)
			print name,code
			try:
				cur.execute('INSERT INTO coinlist(name,code) VALUES("%s","%s")'%\
				(name,code))
				db.commit()
			except:
				db.rollback()
db.close()
