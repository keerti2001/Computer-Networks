import socket
import sys

IP = '127.0.0.1'
PORT = 3001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(0.5)
client_socket.sendto('Hello '.encode(), (IP, PORT))

while True:
    message = input('Enter your message. Enter -1 to sync messages\n')

    if message != '-1':
        client_socket.sendto(message.encode(), (IP, PORT))

    while True:
        try:
            reply, address = client_socket.recvfrom(2048)
            print(str(reply))
        except socket.timeout:
            break

if __name__ == "__main__":
    main()
