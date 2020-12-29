#!/usr/bin/python
import threading,multiprocessing

def loop():
	x = 0
	while True:
		x = x ^ 1

for i in range(4):
	print multiprocessing.cpu_count()
	t = threading.Thread(target=loop)
	t.start()