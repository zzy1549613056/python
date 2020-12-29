#!/usr/local/bin/python3

import socket
import sys
import argparse

host = 'localhost'

def echo_client(port,message):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_addr = (host,port)
	sock.connect(server_addr)

	try:
		
		sock.sendall(message.encode())
		data = sock.recv(1028).decode()
		print ("received:%s"%data)
	except socket.error as e:
		print ("error:%s"%e)
	print ("closing connection")
	sock.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Server Example')
	parser.add_argument('--port',action='store',dest='port',type=int)
	parser.add_argument('--data',action="store",dest='data',type=str)
	args = parser.parse_args()
	port = args.port
	data = args.data
	echo_client(port,data)
