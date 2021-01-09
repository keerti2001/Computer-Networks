import socket
import sys

def main():
    IP = '127.0.0.1'
    PORT = 3001

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        expr = input('Enter an expression')
        client_socket.sendto(expr.encode(), (IP, PORT))
        ans, address = client_socket.recvfrom(2048)
        print(ans)

if __name__ == "__main__":
    main()
