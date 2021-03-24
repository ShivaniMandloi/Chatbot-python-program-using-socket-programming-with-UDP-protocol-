import threading
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = "192.168.43.77"
port = 4444
s.bind((ip,port))

b = input("Enter ip of b: ")
b_port = 1111
        
def receive():
    while True:
        message = s.recvfrom(1024) 
        print("\t\t\t\t\t\t\t"+message[0].decode())

def send():
    while True:
        message = input()
        s.sendto(message.encode(),(b,b_port))

thread1 = threading.Thread(target=receive)
thread2 = threading.Thread(target=send)

thread1.start()
thread2.start()
