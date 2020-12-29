#!/usr/local/bin/python3

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(post):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	server_addr = (host,post)
	sock.bind(server_addr)
	sock.listen(backlog)
	while True:
		print ("Waiting for receive message from client")
		client,addr = sock.accept()
		data = client.recv(data_payload).decode()
		print (data)
		if data:
			print ("DATA is %s"%data)
			client.send(data.encode())
			print ("sent %s back to %s"%(data,addr))
		client.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Server Example')
	parser.add_argument('--port',action='store',dest='port',type=int)
	args = parser.parse_args()
	port = args.port
	echo_server(port)