import socket

HOST = '127.0.0.1'
PORT = 25555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    while True:
        input_data = input("메시지 입력: ")
        client.sendall(input_data.encode('utf-8'))
        received_data = client.recv(1024).decode('utf-8')
        print(f'{received_data}')
