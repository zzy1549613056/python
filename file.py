#!/usr/bin/python 

# with open('./spider.py') as f:
# 	while True:
# 		line = f.read(12)
# 		if line:
# 			print line
# 		else:
# 			break 
list = []
with open('./spider.py','r') as f:
	for line in f.readlines():
		line = line.strip()
		if len(line) and not line.startswith('#') :
			list.append(line)

with open('file_write.txt','w') as w:
	w.write('%s'%'\n'.join(list))
	w.write("hello ,zz")