import socket

s=socket.socket()
print('Socket created')
port=12345
s=socket.gethostbyname(socket.gethostname())
addr = (s,port)

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(addr)

while True:
    conn,addr = s.accept()
    print("Connection done",addr)