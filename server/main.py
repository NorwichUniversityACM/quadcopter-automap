#!/usr/bin/env python

import socket

print "This is the HELLO WORLD ip communication"
tcp_ip = '10.0.0.1'
tcp_port = 666
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print "received data:", data
	conn.send(data) #echo
conn.close()