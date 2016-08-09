from socket import *
import sys

host = 'localhost'
port = 777
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)


filename = input('имя файла: ')
if not filename: 
    tcp_socket.close() 
    sys.exit(1)
sock.send( open(filename, "rb").read() )

data = tcp_socket.recv(1024)
print(data)


tcp_socket.close()
