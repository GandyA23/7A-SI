from Cryptography.Symmetric import Symmetric 
from datetime import date

def inMessage (code):
    return input('Ingresa el mensaje que desea ' + code + ': ')

def saveHistoryInChat(history):
    logs = open('history.txt', 'a')

    for line in history:
        logs.write(line)

crypto = Symmetric()
history = []

if crypto.allItsFine() :
    inp = 'a'
    while inp != 'q':
        print('\n--- Codificador simétrico ---')
        print('Seleccione una opción:')
        print('a.- Codificar un mensaje')
        print('b.- Decodificar un mensaje ')
        print('c.- Guardar las codificaciones y decodificaciones en un archivo')
        print('q.- Salir')
        inp = input('Seleccione una opción: ')
        inp = inp.lower()

        if (inp == 'a'):
            mes = crypto.encode(inMessage('codificar'))
            forPrint = str(date.today()) + ' - Message: ' + mes + '\n'
            history.append(forPrint)
            print(forPrint)
        elif (inp == 'b'):
            mes = crypto.decode(inMessage('decodificar'))
            forPrint = str(date.today()) + ' - Message: ' + mes + '\n'
            history.append(forPrint)
            print(forPrint)
        elif (inp == 'c'):
            saveHistoryInChat(history)
            print('Se ha guardado el historial en el archivo.')
            history = []
        elif (inp == 'q'):
            print('Ha decidido salir del programa.')
        else:
            print('Seleccione una opción válida.')

else: 
    print('Error en la configuración, lee los mensajes de error.')