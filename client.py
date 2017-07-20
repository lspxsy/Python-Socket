#coding=utf-8

import socket
import threading
import time

def startclient():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    
    while True:
        data = raw_input('please input :')
        s.send(data.encode('utf-8'))
        rev = s.recv(1024).decode('utf-8')
        if rev == 'exit':
            break
        print(rev)
    #for data in [b'Michael', b'Tracy', b'Sarah']:
    #	# 发送数据:
    #	s.send(data)
    #	print()
    #s.send(b'exit')
    s.close()

    
def tcplink(sock):
    print(sock.recv(1024).decode('utf-8'))
    
    