# Saludo
print("Hola bienvenido a Comestibles Python")
nombre = input("¿Cómo te llamas?: ")

# Productos
tomates = 1
pepinos = 2
pimientos = 3

bolsas = 0.20

# Pregunta productos
tomates_cantidad = int(input("Cantidad de tomates que quires comprar: "))
pepinos_cantidad = int(input("Cantidad de pepinos que quires comprar: "))
pimientos_cantidad = int(input("Cantidad de pimientos que quires comprar: "))

# Bolsas
bolsa = input("Vas a querer una bolsita: "))
if bolsas == "Si":
    bolsas_cantidad = int(input("Cantidad de bolsas que quires: "))
else:
    print("De acuerdo")

# Calcular el precio total
precio_total = (tomates_cantidad * tomates) + (pepinos_cantidad * pepinos) + (pimientos_cantidad * pimientos) + (precio_bolsas * bolsas_cantiad)

# Indicar el precio total
print(f"El precio total son: {precio_total} euros")

# Despedida
print(f"Hasta la próxima {nombre}")
