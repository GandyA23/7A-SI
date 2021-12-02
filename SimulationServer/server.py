import socket
import time 

print(".: Server is on :.\n")

# Wait a second for continue
time.sleep(1)

server_socket = socket.socket()
server_socket.bind( ('127.0.0.1',8000) )
server_socket.listen(5)

print("### Servidor de sockets activo ###")

while True:
    conexion, addr = server_socket.accept()
    print("Nueva conexión establecida!")
    print(addr)
    conexion.send("Hola, te saludo desde el servidor!".encode('UTF-8'))

conexion.close()