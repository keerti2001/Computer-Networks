import socket
IP = '127.0.0.1'
PORT = 12345

try:
    clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print "Connected"
except socket.error as e:
    print "Could not connect"
    print e

a = ["axrs","sses","serwt","dfgeetg","xnsiw"]
print "The initial list is:-",a
a = str(a)
a = a.encode()
clientsocket.sendto(a,(IP,PORT))
data,address = clientsocket.recvfrom(10000)
data = data.decode('utf-8')
data = eval(data)
print "After:- ",data
