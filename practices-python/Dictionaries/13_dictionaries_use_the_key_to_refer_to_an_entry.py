"""
Gandy Esaú Ávila Estrada
7º A
Seguridad Informática
Lunes 27 de septiembre de 2021 
"""
ipAddress = {"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
print(type(ipAddress))
print(ipAddress)
print(ipAddress['R1'])

# Añade o actualiza un valor de la siguiente manera
ipAddress["S1"]="10.1.1.10"

print(ipAddress)

# Boolean, verifica si la llave R3 existe en el diccionario
print("R3" in ipAddress)
