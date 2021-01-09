import socket
import sys
import time

def main():
    IP = '127.0.0.1' # localhost
    PORT = 3001

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(5)

    while True:
        client_socket,adress = server_socket.accept()

        while True:
            data = client_socket.recv(2048)
            print(data)
            if data == b"test":
                client_socket.send("test".encode())
                break

            client_socket.send(data.upper())

        client_socket.close()

if __name__ == "__main__":
    main()
