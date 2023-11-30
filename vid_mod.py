import random
import time
import statistics

listatiempos = []

print("Elige el número más pequeño: ")
numerominimo = int(input())
print("Elige el número más grande: ")
numeromaximo = int(input())
print("Elige el número de operaciones: ")
operaciones = int(input())

for i in range(operaciones):
    
    a = random.randint(numerominimo,numeromaximo)
    b = random.randint(numerominimo,numeromaximo)
    c = a*b

    t1 = time.time()

    print("Calcula cuanto es ", a, "x", b)
    resultado = int(input())

    t2 = time.time()
    tiempo = t2-t1
    listatiempos.append(tiempo)

    if (resultado == c):
        print("¡Correcto!")
    else:
        print("¡Incorrecto!")
    print("Has tardado", tiempo, "segundos")

mediatiempos = statistics.mean(listatiempos)    
print ("El juego ha terminado")
print ("Has tardado de media", mediatiempos, "segundos")

"""
while True:

    a = random.randint(1,10)
    b = random.randint(1,10)
    c = a*b

    t1 = time.time()

    print("Calcula cuanto es ", a, "x", b)
    resultado = int(input())

    t2 = time.time()
    tiempo = t2-t1

    if (resultado == c):
        print("¡Correcto!")
    else:
        print("¡Incorrecto!")
    print("Has tardado", tiempo, "segundos")
    """