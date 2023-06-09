from socket import *
import os
import sys

# https://docs.python.org/3.10/library/socket.html
# https://github.com/python/cpython/blob/3.10/Lib/socket.py
# https://docs.python.org/3.10/library/os.html
# https://docs.python.org/3.10/library/sys.html

HOST = '127.0.0.1'
PORT = 25555

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

print('서버에 연결되었습니다.')

filename = 'cat.jpg'

with open(filename, 'rb') as file:
    client.sendall(filename.encode('utf-8'))
    data_size = 0
    print(f'파일 {filename} 전송 시작.')
    try:
        data = file.read(1024)
        while data:
            data_size += client.send(data)
            data = file.read(1024)
        print(f'파일 {filename} 전송 완료. 전송량: {data_size}')
    except Exception as error:
        print(error)
