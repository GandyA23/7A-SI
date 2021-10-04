"""
Gandy Esaú Ávila Estrada
7º A
Seguridad Informática
Lunes 04 de octubre de 2021 
"""
while True:
    x = input("Enter a number to count to (enter q or quit to exit): ")

    if x == 'q' or x == 'quit':
        break
    
    x = int(x)
    y = 1

    while True:
        print(y, end=' ')
        y=y+1

        if y>x:
            print()
            break
print()
