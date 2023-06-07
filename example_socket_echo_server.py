import socket

# https://docs.python.org/3.10/library/socket.html
# https://github.com/python/cpython/blob/3.10/Lib/socket.py

HOST = ''
PORT = 25555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print('에코 서버 시작')
    connection, address = server.accept()
    with connection:
        print(f'클라이언트{address}가 접속했습니다: ')
        while True:
            received_data = connection.recv(1024).decode('utf-8')
            print(f'수신한 데이터: {received_data}')
            connection.sendall(f'{address}: {received_data}'.encode('utf-8'))
