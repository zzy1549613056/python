#!/usr/bin/python
import socket
def print_info():
   host_name = socket.gethostname()
   #ip = socket.gethostbyname(host_name)
   print "Host name: %s" %host_name
   #print "Ip: %s" %ip

if __name__ == '__main__':
   print "zzy"
   print_info()