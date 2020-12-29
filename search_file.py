#!/usr/bin/python
import os 

current_dir = os.path.abspath('.')

def match_name(dir,name):
	if name in os.path.splitext(dir)[0]:
		return True
	else:
		return False

def search(dir,name):
	for x in os.listdir(dir):
		new_dir = os.path.join(dir,x)
		if os.path.isdir(new_dir):
			search(new_dir,name)
		else:
			if match_name(new_dir,name):
				print new_dir

if __name__ == "__main__":
	search(current_dir,'spider')