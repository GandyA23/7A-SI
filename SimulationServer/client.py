import socket

cliente_socket = socket.socket()
cliente_socket.connect( ('localhost',8000) )
cliente_socket.send("Hola desde el cliente!".encode('UTF-8'))
respuesta = cliente_socket.recv(1024) ##Tamaño del buffer en bytes
print(respuesta)
cliente_socket.close()
print("Pulsa una tecla para terminar...")
input()