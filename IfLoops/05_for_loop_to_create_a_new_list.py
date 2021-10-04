"""
Gandy Esaú Ávila Estrada
7º A
Seguridad Informática
Lunes 04 de octubre de 2021 
"""
devices = ["R1", "R2", "R3", "S1", "S2"]
switches = []

# Only add to switches the devices that contain a "S"
for device in devices:
    if "S" in device:
        switches.append(device)

print(switches)

# Other example
x = range(5, 50, 2)
for n in x:
    print(n, end = '-')
print()
