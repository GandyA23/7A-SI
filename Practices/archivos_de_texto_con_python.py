"""
Avila Estrada Gandy Esau
Viernes 8 de septiembre de 2021
Archivos de texto con python
7º "A"
"""

linea = ''

# Solicitar al usuario un nombre de archivo.
filename = input('Ingresa el nombre del archivo: ')

# Crea el archivo de texto
file = open(filename + '.txt', "a")

while True:
    linea = input("Ingrese cualquiera de sus datos importantes (Q ó QUIET ó SALIR para salir del programa): ")
    
    # strip() = trim()
    lineaUpper = linea.strip().upper()
    linea = linea.strip()

    if lineaUpper == 'Q' or lineaUpper == 'QUIT' or lineaUpper == 'SALIR':
        print('Has decidido salir del programa.\n')
        break

    file.write(linea + '\n')

    print('Se ha ingresado el texto al archivo.\n')


file = open(filename + '.txt', "r")

# Imprime la información 
print('Contenido del archivo: \n')
flag = 1
for linea in file:
    flag = flag % 2 
    # Línea 1: Mayúscula
    if flag == 1:
        linea = linea.upper()
    else:
    # Línea 2: Minúsculas
        linea = linea.lower()

    print(linea, end = '')
    flag = flag + 1

# Cierra el archivo
file.close()


