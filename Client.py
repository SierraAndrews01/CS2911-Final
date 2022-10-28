from socket import *

# TCP Port
TCP_Port = 12345

# Address of the 'other' ('server') host that should be connected to for 'send' operations.
# When connecting on one system, use 'localhost'
# When 'sending' to another system, use its IP address (or DNS name if it has one)
# OTHER_HOST = '155.92.x.x'
OTHER_HOST = "localhost"

def tcp_send(server_host, server_port):
    print()

if __name__ == "__main__":
    tcp_send(OTHER_HOST, TCP_Port)