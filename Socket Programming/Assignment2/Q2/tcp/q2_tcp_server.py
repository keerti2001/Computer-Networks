import socket
import sys

def main():
    IP = '127.0.0.1'
    PORT = 3001

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(5)

    while True:
        client_socket, address = server_socket.accept()
        print("Client connected from ", address)

        while True:
            message = client_socket.recv(2048)
            print(message)

            check = input("Do you want to send a message? [Y/N] ")
            if check.lower() == 'n':
                break
            mesage = input('Enter message for client')
            client_socket.send(str(message).encode())
        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    main()
