#!/usr/local/bin/python3
import socket
import sys

def reuse_socket():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	sock.bind(('',8282))
	sock.listen(1)
	print ("listen on port:8282")
	while True:
		try:
			con,addr = sock.accept()
			print ("Connected by %s:%s" %(addr[0],addr[1]))
		except KeyboardInterrupt:
			break
		except socket.error as e:
			print ("%s" %e)

if __name__ == '__main__':
	reuse_socket()