import socket
import threading

# https://docs.python.org/3.10/library/socket.html
# https://github.com/python/cpython/blob/3.10/Lib/socket.py
# https://docs.python.org/3.10/library/threading.html

HOST = '127.0.0.1'
PORT = 25555

def send():
    while True:
        input_data = input("메시지 입력: ")
        if input_data[0:1] == '귓':
            print(f'귓속말 전송 시작! 수신대상:{input_data[1:6]}')
            client.sendall(input_data.encode('utf-8'))
        else:
            client.sendall(f'X00000{input_data}'.encode('utf-8'))

def receive():
    while True:
        received_data = client.recv(1024).decode('utf-8')
        print(f'{received_data}')

#TCP Client
if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    thread1 = threading.Thread(target=send, args=())
    thread1.start()

    thread2 = threading.Thread(target=receive, args=())
    thread2.start()
