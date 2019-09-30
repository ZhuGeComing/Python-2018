from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

sendAddr = ('192.168.154.1',8080)

#发送信息
udpSocket.sendto(b'this is test.',sendAddr)

receiveData = udpSocket.recvfrom(1024)

print(receiveData)

udpSocket.close()