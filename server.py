#coding=utf-8

import socket
import threading
import time


def startserver():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('Waiting for connection...')
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            sock.send(('exit').encode('utf-8'))
            break
        print('Get a message from %s:%s : %s' % (addr[0],addr[1],data.decode('utf-8')))
        sock.send(('I get it, Has anything?').encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)