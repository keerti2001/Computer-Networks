import socket
import sys

def main():
    IP = '127.0.0.1'
    PORT = 3001

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        client_socket.sendto(input('Enter your message for server ').encode(), (IP, PORT))
        reply, address = client_socket.recvfrom(2048)
        print(reply)

if __name__ == "__main__":
    main()
