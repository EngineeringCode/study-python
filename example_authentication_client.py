import socket

# https://docs.python.org/3.10/library/socket.html
# https://github.com/python/cpython/blob/3.10/Lib/socket.py

HOST = '127.0.0.1'
PORT = 25555

'''
0       20        40    1023
| 아이디 | 패스워드  | 예약 |
'''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    input_id = input("아이디 입력: ")
    input_pw = input("패스워드 입력: ")
    input_data = input_id[0:20].rjust(20, ' ') + input_pw[0:20].rjust(20, ' ')
    print(input_data)
    client.sendall(input_data.encode('utf-8'))
    received_data = client.recv(1024).decode('utf-8')
    print(f'{received_data}')
