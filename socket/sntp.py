#!/usr/local/bin/python3
import socket
import struct
import sys
import time

NTP_SERVER = "pool.ntp.org"
TIME1970 = 2208988800

def sntp_client():
	clinet = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	data = '\x1b' + 47 * '\0'
	clinet.sendto(data.encode(),(NTP_SERVER,123))
	data,address = clinet.recvfrom(1024)
	if data:
		print ("receive from:",address)
	t = struct.unpack('!12I',data)[10]
	t -= TIME1970
	print('TIME=%s'%time.ctime(t))

if __name__ == "__main__":
	sntp_client()