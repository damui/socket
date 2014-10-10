#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a socket example which get html data from www.sina.com.cn'

import socket

#创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn', 80))
#发送数据
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接受数据
buffer = []
while True:
	#最多接受1k数据
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = ''.join(buffer)
#关闭连接
s.close()

header, html = data.split('\r\n\r\n', 1)
print header
#把接受到的数据写入文件
with open('sina.html', 'wb') as f:
	f.write(html)
