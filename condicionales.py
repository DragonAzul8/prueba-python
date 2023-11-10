# Login usuario

print("Acceso al sistema")
usuario = input("Nombre de usuario: ")
password = input("Contraseña: ")

if usuario == "Anibal":
    print("Usuario correcto")
    if password == "1234":
        print("Bienvenido, Anibal")
else:
    print("Usuario incorrecto")