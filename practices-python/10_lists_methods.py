"""
Gandy Esaú Ávila Estrada
7º A    
Seguridad Informática
Miércoles 29 de septiembre de 2021 
"""

lista = [1, 2.5, 'cadena', [5,6], 4]

# Append
# Ingresa un elemento al fondo de la lista
print('Append')
lista.append(10) # [1, 2.5, 'cadena', [5,6], 4, 10]
lista.append([2, 5]) # [1, 2.5, 'cadena', [5,6], 4, 10, [2, 5]]

print(lista) 
print()

# Extend
# Permite agregar elementos dentro de la lista.
# Al agregar una lista, cada elemento de ésta nueva lista se agrega como un elemento individual.

print('Extend')
lista = [1, 2.5, 'cadena', [5,6], 4]
lista.extend([88, 99]) # [1, 2.5, 'cadena', [5,6], 4, 10, 88, 99]
print(lista)
print()

# Insert
# Inserta un elemento en la posición asignada en el primer parámetro
print('Insert')
lista = [1, 2.5, 'cadena', [5,6], 4]
lista.insert(2, 'Z')    # [1, 2.5, 'Z','cadena', [5,6], 4]
print(lista)
print()

# Remove
# El método remove quita de la lista el elemento (valor) que se le indique como parámetro.
print('Remove')
lista = [1, 2.5, 'cadena', [5,6], 4]
lista.remove('cadena')  # [1, 2.5, [5,6], 4]
print(lista)
print()

# Index
# Index devuelve el índice del primer elemento que le pasemos como parámetro.
print('Index')
lista = [1, 2.5, 'cadena', [5,6], 4]
print(lista.index('cadena'))    # 2
print()

# Count
# Muestra cuántes veces se repite un elemento dentro de la lista. 
print('Count')
lista = [7, 3, 2.5, 'cadena', 7, [5,6], 4, 7]
print(lista.count(7))    # 3
print()

# Copy
# Copia el contenido de una lista en otra.
print('Copy')
lista = [7, 3, 2.5, 'cadena', 7, [5,6], 4, 7]
otra_lista = lista.copy()
print(otra_lista)    # [7, 3, 2.5, 'cadena', 7, [5,6], 4, 7]
print()

# Reverse
# Invierte el orden de los elementos de una lista. No devuelve valores.
print('Reverse')
lista = [7, 3, 2.5, 'cadena', 7, [5,6], 4, 7]
lista.reverse() # [7, 4, [5, 6], 7, 'cadena', 2.5, 3, 7]
print(lista)    
print()

# Sort
# Ordena ascendentemente a > z. No retorna valores.
print('Sort')
lista = [7, 40, 10, 3, 5, 60, 32]
lista.sort() # [3, 5, 6, 10, 32, 40, 60]
print(lista)
lista.sort(reverse=True) # [60, 40, 32, 10, 7, 5, 3]
print(lista)    
print()

# min(lista) y max(lista)
# Obtiene los valores máximos y minimos de una lista
print('min(lista) y max(lista)')
lista = [7, 40, 10, 3, 5, 60, 32]
print(max(lista))   # 60
print(min(lista))   # 3
