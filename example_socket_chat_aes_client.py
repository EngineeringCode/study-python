import socket
import threading
import util_aes

# https://docs.python.org/3.10/library/socket.html
# https://github.com/python/cpython/blob/3.10/Lib/socket.py
# https://docs.python.org/3.10/library/threading.html

HOST = '127.0.0.1'
PORT = 25555

KEY = '0123456789012345'

def send():
    while True:
        input_data = util_aes.Cipher(bytes(KEY, encoding='utf8')).encrypt(input("메시지 입력: "))
        client.sendall(input_data)

def receive():
    while True:
        received_data = util_aes.Cipher(bytes(KEY, encoding='utf8')).decrypt(client.recv(1024))
        print(f'{received_data}')

#TCP Client
if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    thread1 = threading.Thread(target=send, args=())
    thread1.start()

    thread2 = threading.Thread(target=receive, args=())
    thread2.start()
