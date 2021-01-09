import socket
import sys

def main():
    IP = '127.0.0.1' # localhost
    PORT = 3001

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    while True:
        message = input('Enter your message\n')

        client_socket.send(message.encode())
        data = client_socket.recv(2048)

        print(data)
        if str(data) == "test":
            break

    client_socket.close()

if __name__ == "__main__":
    main()
