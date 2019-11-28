import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8888))

s.listen(5)

while True:
    print('Server online...')
    (cli_socket, addr) = s.accept()
    with cli_socket:
        print(addr, 'has conneted to the server.')
        while True:
            data = cli_socket.recv(1024)
            if not data:
                break
            print(addr, 'said', repr(data))

        cli_socket.sendall(b'Msg recived')

s.close()