#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a scoket example which send echo message to server'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1', 9999))
#接受欢迎信息
print s.recv(1024)
for data in ['lisi', 'zhangsan', 'wangwu']:
	#发送数据
	s.send(data)
	print s.recv(1024)
s.send('exit')
#关闭连接
s.close()
