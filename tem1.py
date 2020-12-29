#!/usr/bin/python

from multiprocessing import Process, Queue,Pool
import os,time,random,threading

class MyThread(threading.Thread):

	def __init__(self,func,args=()):
		super().__init__(target=func,args=args)


	def run(self):
		try:
		    if self._target:
		        self._result = self._target(*self._args, **self._kwargs)
		finally:
		    del self._target, self._args, self._kwargs

	@property
	def result(self):
		return self._result

def long_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    return name			

def run_thread():
	for i in range(10):
		time.sleep(1)
		print(i)
	return 12




if __name__ == "__main__":
	# resPool =[]
	# arr = []
	# p = Pool(50)
	# for i in range(100):
	# 	resPool.append(p.apply_async(long_task,args=(i,)))
	# print('Waiting for all subprocesses done...')
	# p.close()
	# p.join()
	# for res in resPool:
	# 	arr.append(res.get())
	# print('All subprocesses done.')	
	# print(arr)
	t1 = MyThread(func=run_thread)
	t2 = MyThread(func=run_thread)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print('$$$$$$$',t1.result)



