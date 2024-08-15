import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

cantidad = int(input("Insertar el numero de caracteres para su contraseña:"))

password = ""

for i in range (cantidad):
    password = password + random.choice(caracteres)

print("Contraseña generada:", password)
