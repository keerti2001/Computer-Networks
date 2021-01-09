import socket
from datetime import date
IP = '127.0.0.1'
PORT = 8080

try:
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Created the socket")
except socket.error as e:
    print(e)

serversocket.bind((IP,PORT))
serversocket.listen(100)
while True:
    connection,adress = serversocket.accept()
    data = connection.recv(100000)
    print(data)
    connection.send(str(date.today()).encode())
    connection.close()
