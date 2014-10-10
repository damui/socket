#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a client example which send message to server'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['lisi', 'zhang', 'wang']:
	#发送数据
	s.sendto(data, ('127.0.0.1', 9999))
	#接受数据
	print s.recv(1024)
#关闭连接
s.close() 
