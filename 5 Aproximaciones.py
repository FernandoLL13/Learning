numero = int(input('Escoge un numero uwu'))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - numero) >= epsilon and respuesta <= numero:
    respuesta += paso

if abs(respuesta**2 - numero) - numero >= epsilon:
    print(f'No se encontro la raiz cuadrada de {numero} unu')
else:
    print(f'La raiz cuadrada de {numero} es {respuesta} owo')