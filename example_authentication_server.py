import socket

# https://docs.python.org/3.10/library/socket.html
# https://github.com/python/cpython/blob/3.10/Lib/socket.py

HOST = ''
PORT = 25555

'''
0       20        40    1023
| 아이디 | 패스워드  | 예약 |
'''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print('인증 서버 시작')
    while True:
        connection, address = server.accept()
        with connection:
            print(f'클라이언트{address}가 접속했습니다: ')
            received_data = connection.recv(1024).decode('utf-8')
            input_id = received_data[0:20].replace(' ', '')
            input_pw = received_data[20:40].replace(' ', '')
            print(f'수신한 아이디: {input_id}')
            print(f'수신한 패스워드: {input_pw}')
            if input_id == 'abc' and input_pw == '123':
                connection.sendall(f'인증되었습니다.'.encode('utf-8'))
            else:
                connection.sendall(f'인증정보가 유효하지 않습니다.'.encode('utf-8'))
