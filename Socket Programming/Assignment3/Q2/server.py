import socket
IP = '127.0.0.1'
PORT = 12345

try:
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print "Connected"
except socket.error as e:
    print "Could not connect"
    print e

serversocket.bind((IP,PORT))

while True:
    data,address = serversocket.recvfrom(100)
    data = data.decode('utf-8')
    data = eval(data)
    data.sort()
    print data
    data = str(data)
    data = data.encode()
    serversocket.sendto(data,address)
