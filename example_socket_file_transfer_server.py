from socket import *
import os
import sys
import datetime

# https://docs.python.org/3.10/library/socket.html
# https://github.com/python/cpython/blob/3.10/Lib/socket.py

HOST = ''
PORT = 25555

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f'서버 시작')

connection, address = server.accept()

print(f'클라이언트{address}가 접속했습니다: ')

filename = connection.recv(1024).decode('utf-8')
filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + filename

print(f'파일 {filename} 수신 시작.')

current_directory = os.getcwd()

data_size = 0

with open(current_directory + "\\" + filename, 'wb') as file:
    try:
        data = connection.recv(1024)
        while data:
            file.write(data)
            data_size += len(data)
            data = connection.recv(1024)
        print(f'파일 {filename} 수신 완료. 수신량: {data_size}')
    except Exception as error:
        print(error)
