''' Función que calcula la media del curso '''
def mediacurso(nota1a, nota2a, nota3a):
    media = nota1a*0.5 + nota2a*0.3 + nota3a*0.2
    return media

''' Función que dice si apruebo el curso o no '''
def apruebacurso(notamediacurso):
    if(notamediacurso >= 5):
        print("¡Enorabuena! Has aprobado el curso")
    else:
        print("Deberás recuperar en septiembre")

''' Función que me dice la nota de la 3a que necesito pra aprobar '''
def quenecesitoparaaprobar(nota1a, nota2a):
    notaquenecesito = 15 - nota1a - nota2a
    print("Necesitas de la 3a sacar un: ", notaquenecesito)

nota1a = int(input("Dime la nota de la 1a ev.: "))
nota2a = int(input("Dime la nota de la 2a ev.: "))

quenecesitoparaaprobar(nota1a, nota2a)
