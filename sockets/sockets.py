import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crear objeto - direccion IP y puerto
s.connect(('localhost', 12345))


