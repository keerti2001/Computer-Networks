import socket
import sys

def main():
    IP = '127.0.0.1'
    PORT = 3001

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((IP, PORT))

    clients = []

    while True:
        data, address = server_socket.recvfrom(2048)
        
        if address not in clients:
            clients = clients + [address]
        else:
            for client in clients:
                if client != address:
                    server_socket.sendto((str(address)+ ' : ' + str(data)).encode(), tuple(client))

if __name__ == "__main__":
    main()
