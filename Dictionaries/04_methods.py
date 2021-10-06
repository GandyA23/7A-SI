"""
Gandy Esaú Ávila Estrada
7º A
Seguridad Informática
Lunes 27 de septiembre de 2021 
"""

diccionario = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

print("Keys")
# Obtiene los nombres de las llaves
keys = diccionario.keys()
print(keys)
print()

print("Valores")
# Obtiene los valores dentro de las llaves
valores = diccionario.keys()
print(valores)
print()

print("Clear")
diccionarioAux = diccionario
# Elimina todos los elementos del diccionario
diccionarioAux.clear()
print(diccionarioAux)
print()

print("Get")
# Devuelve el valor de la clave
print(diccionario.get('b'))
print()

print("setDefault")
diccionarioAux = diccionario

# Opera de dos formas. La primera como un get()
print(diccionarioAux.setdefault('b'))
print()

# Agrega un nuevo elemento al diccionario
diccionarioAux.setdefault('e', 5)
print(diccionario)
print()

print("Update")

"""
Recibe como parámetro otro diccionario. Si tiene claves iguales, 
actualiza el valor de la clave; si no si tiene la clave, el par clave-valor
es agregado al diccionario
"""
diccionario2 = {'c' : 6, 'b' : 7, 'e' : 8, 'f' : 12}
diccionarioAux = diccionario

diccionarioAux.update(diccionario2)

print(diccionarioAux)
print()


