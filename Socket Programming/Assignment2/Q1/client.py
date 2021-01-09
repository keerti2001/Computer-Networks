import socket
IP = '127.0.0.1'
PORT = 8080

try:
    clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Created the socket")
except socket.error as e:
    print(e)

clientsocket.connect((IP,PORT))
clientsocket.send("what's the current date?".encode())
data = clientsocket.recv(10000)
print(data)
clientsocket.close()
