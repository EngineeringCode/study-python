import socket
import threading

# https://docs.python.org/3.10/library/socket.html
# https://github.com/python/cpython/blob/3.10/Lib/socket.py

HOST = '127.0.0.1'
PORT = 25555

def send():
    while True:
        input_data = input("메시지 입력: ").encode('utf-8')
        client.sendall(input_data)

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