"""
Gandy Esau Avila Estrada
7° A
Cliente
"""
import socket
import time
import sys

sys.path.append('../CifradoSimetrico')

from Cryptography.Symmetric import Symmetric

# Para cifrar los mensajes
crypto = Symmetric()

print('..: Cliente :..\n')

if crypto.allItsFine() :
    time.sleep(1)
    cliente_socket = socket.socket()
    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    print(host, '({})'.format(ip))

    nombre_usuario = input("Indique su nombre de usuario: ")
    ip_host = input("¿A qué IP se conectará?: ")
    puerto = input("¿A qué puerto se conectará?: ")

    time.sleep(1)
    cliente_socket.connect((str(ip_host), int(puerto)))
    print("¡Conexión establecida! Inicia la comunicación.\n")

    cliente_socket.send(nombre_usuario.encode())
    server_name = cliente_socket.recv(1024)
    server_name = server_name.decode()

    print('Escriba salir para finalizar comunicación.')
    while True:
        mensajeCifrado = cliente_socket.recv(1024)
        mensajeCifrado = mensajeCifrado.decode()
        mensaje = crypto.decode(mensajeCifrado)
        print(server_name," dice: ", mensajeCifrado, " > ", mensaje)
        mensaje = input(str("Yo: "))
        if mensaje == "salir":
            mensaje = "se desconectó."
            cliente_socket.send(mensaje.encode())
            print("\n")
            break

        ## Cifra el mensaje del cliente 
        mensaje = crypto.encode(mensaje)
        
        cliente_socket.send(mensaje.encode())
else:
    print('Error en la configuración, lee los mensajes de error')
