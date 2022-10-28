from socket import *

def MusicServer():
    server_socket = socket(AF_INET, SOCK_STREAM)
    listen_address = ('', 12345)
    server_socket.bind(listen_address)
    server_socket.listen()
    while True:
        client, request_address = server_socket.accept()
        


if __name__ == '__main__':
    MusicServer()