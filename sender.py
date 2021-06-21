import socket
#importing socket module/library
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#what is my receiver addresss
recv_addr=("127.0.0.1",9999)
#now i want to send message
user_data= input("enter your message:-")
#converting data into ascci code
newdata=user_data.encode('ascii')
#now you can send data
s.sendto(newdata, recv_addr)
print("your message has been sent")