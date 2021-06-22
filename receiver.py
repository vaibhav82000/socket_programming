import socket
#importing socket module/library
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#                ipv4, UDP type
s.bind(('127.0.0.1',9999))
#creating udp socket ipv4, port
# so now writing code to receive data
while True:
 data_recv=s.recvfrom(100)
print(data_recv)
#sending response
reply="thanks for connecting.."
s.sendto(reply.encode('ascii'),data_recv[1])
