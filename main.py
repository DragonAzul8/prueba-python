print("Hola mundo!!")
print("Hola mundo 1!!")

# Soy un cometario
print("Hola mundo 2!!")

"""
Texto que no se va a interpretar
Texto que no se va a interpretar
Texto que no se va a interpretar
"""

# Variables
texto = "Prueba de Python"
nombre = "Anibal"
altura = "184cm"
year = 2023

print(f"{texto} - {nombre} - {altura} - {str(year)}")
print(texto + " - " + nombre + " - " + altura + " - " + str(year))

# Entrada
#sitioweb = input("¿Cuál es tu página web?: ")
#print("El sitio web del usuario es: " + sitioweb)

# Condiciones
altura = int(input("¿Cuál es tu altura?: "))

if altura >= 180:
    print("Eres una persona alta")
else: 
    print("Eres bajito")