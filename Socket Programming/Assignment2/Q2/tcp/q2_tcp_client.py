import socket
import sys

def main():
    IP = '127.0.0.1'
    PORT = 3001

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    while True:
        check = input('Do you want to send a mesage? [Y/N] ')

        if check.lower() == 'n':
                break

        client_socket.send(str(input('Enter message for server')).encode())
        reply = client_socket.recv(2048)
        print(reply)

    client_socket.close()

if __name__ == "__main__":
    main()
