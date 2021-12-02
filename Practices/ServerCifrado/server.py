"""
Gandy Esau Avila Estrada
7° A
Servidor 
"""

import socket
import time
import sys

sys.path.append('../CifradoSimetrico')

from Cryptography.Symmetric import Symmetric

time.sleep(1)

crypto = Symmetric()

if crypto.allItsFine() :
    print("..: Servidor activo :..\n")
    socket_server = socket.socket()
    socket_server.bind(('localhost', 8000))

    nombre_servidor = input("Ingrese el nombre del servidor: ")
    socket_server.listen(1)

    print("Esperando conexiones")
    connection, addr = socket_server.accept()

    print("Conexión recibida de ", addr[0], "(", addr[1], ")\n")
    print("Conexión establecida. conectado de: {}, ({})".format(addr[0], addr[0]))

    cliente = connection.recv(1024)
    cliente = cliente.decode()
    print(cliente + " se conectó.")

    print("Teclee salir para desconectarse")
    connection.send(nombre_servidor.encode())

    while True:
        mensaje = input('Yo: ')
        
        if mensaje == 'salir':
            mensaje = 'Cerrando conexión.'
            connection.send(mensaje.encode())
            print("\n")
            break

        ## Cifra el mensaje del servidor 
        mensaje = crypto.encode(mensaje)

        connection.send(mensaje.encode())

        mensajeCifrado = connection.recv(1024)
        mensajeCifrado = mensajeCifrado.decode()
        mensaje = crypto.decode(mensajeCifrado)
        print(cliente, ' dice :', mensajeCifrado, " > ", mensaje)
else:
    print('Error en la configuración, lee los mensajes de error')