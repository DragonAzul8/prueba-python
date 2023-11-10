# Pregunta productos
producto = int(input("¿Cuántos tomates quires?: "))
if producto >= 0:
    print("Son: (tomates * producto) euros")
else: 
    producto2 = int(input("¿Cuántos pepinos quires?: "))
        if producto2 >= 0:
            print("Son: (pepinos * producto2) euros")
        else: 
            producto3 = int(input("¿Cuántos pimientos quires?: "))
                if producto3 >= 0:
                    print("Son: (pimientos * producto3) euros")
                else: 
                    print("Pués estos eran los productos que tenemos disponibles.")