# Bucles
"""
for numero in range(10, 30):
    print("Hola", numero)

fruta = "plátano"
frutas = ["manzana", "pera"]
frutas.append(fruta)

#print(frutas[0])
#print(frutas[1])
#print(frutas[2])

for frutaseleccionada in frutas:
    if frutaseleccionada == "pera":
        break
    print(frutaseleccionada)

sumatorio = 0
for numero in range(1,101):
    sumatorio = sumatorio + numero
print(sumatorio)
"""

vida = 100
while vida > 0:
    vida -= 10
    if vida > 30:
        continue
    print("te queda", vida)