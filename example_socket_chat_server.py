import socket
import threading
from queue import Queue

# https://docs.python.org/3.10/library/socket.html
# https://github.com/python/cpython/blob/3.10/Lib/socket.py
# https://docs.python.org/3.10/library/threading.html
# https://docs.python.org/3.10/library/queue.html

HOST = ''
PORT = 25555

message_queue = Queue()
connections = list()

def send():
    #print("발신 스레드를 시작합니다.")
    while True:
        try:
            message = message_queue.get()
            data = f'클라이언트{message[1]}:' + message[0]
            print(data)

            for conn in connections:
                conn.sendall(data.encode('utf-8'))

        except:
            pass

def receive(p_connection):
    print(f'클라이언트{p_connection} 메시지 수신 스레드 시작')
    while True:
        message = connection.recv(1024).decode('utf-8')
        #print(f'수신한 데이터: {message}')
        message_queue.put([message, connection])

if __name__ == '__main__':
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((HOST, PORT))
    server_sock.listen()

    thread1 = threading.Thread(target=send, args=())
    thread1.start()

    while True:
        connection, address = server_sock.accept()
        connections.append(connection)
        print(f'클라이언트{address}가 접속했습니다: ')

        thread2 = threading.Thread(target=receive, args=(connection,))
        thread2.start()
