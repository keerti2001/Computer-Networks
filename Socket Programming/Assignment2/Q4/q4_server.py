import socket
import sys

def main():
    IP = '127.0.0.1'
    PORT = 3001

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind((IP,PORT))

    while True:
        data, address = server_socket.recvfrom(2048)
        print(data)

        ans = str(eval(data))
        print(ans)

        server_socket.sendto(ans.encode(), address)

if __name__ == "__main__":
    main()
