#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a udp server example which send time to client'

import socket, datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1', 9999))
print "Bind UDP on port 9999"
while True:
	#接受数据
	data, addr = s.recvfrom(1024)
	print 'Received from %s:%s.' % addr
	s.sendto('Hello, %s! Time: %s' % (data, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), addr)
