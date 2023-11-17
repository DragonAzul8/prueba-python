# Funciones
def saludar

def calcular_iva(tipo, precio):
    #IVA libros: 4%
    #IVA turrones: 10%
    #IVA coches: 21%
    if tipo == "libros":
        iva = 4/100*precio
        return iva
    if tipo == "turrones":
        iva = 10/100*precio
        return iva
    if tipo == "coches":
        iva = 21/100*precio
        return iva

# Pedir productos al usuario
numero_libros = int(input("¿Cuántos libros quieres?: "))
numero_turrones = int(input("¿Cuántos turrones quieres?: "))
numero_coches = int(input("¿Cuántos coches quieres?: "))


# Calcular precio e iva
precio_libros = numero_libros*30
iva_libros = calcular_iva("libros", precio_libros)

precio_turrones = numero_turrones*5
iva_turrones = calcular_iva("turrones", precio_turrones)

precio_coches = numero_coches*20000
iva_coches = calcular_iva("coches", precio_coches)

# Sumar precio más iva
total_libros = precio_libros + iva_libros
total_turrones = precio_turrones + iva_turrones
total_coches = precio_coches + iva_coches

# Calcular total
total = total_libros + total_turrones + total_coches
print(total, "euros")