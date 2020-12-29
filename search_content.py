#!/usr/bin/python
import os 

current_dir = os.path.abspath('.')

def match_content(dir,name):
	with open(dir,'r') as f:
		content = f.readlines()
		for x in content:
			if name in x:
				return True
	return False

def search(dir,name):
	for x in os.listdir(dir):
		new_dir = os.path.join(dir,x)
		if os.path.isdir(new_dir):
			search(new_dir,name)
		else:
			if match_content(new_dir,name):
				print new_dir

if __name__ == "__main__":
	search(current_dir,'cookie')