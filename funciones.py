import datetime
def agregar_usuario(
    diccionario:dict
)-> dict:
    nom = input("Ingrese su nombre: ")
    lib =  input("Ingrese su nombre: ")
    estado = input("Estado:")
    fecha_pres =  input("Ingrese su nombre:")
    diccionario_int = {
        "libro":lib,
        "fecha":fecha_pres,
        "estado": estado
    }
    print(diccionario_int)
    if diccionario.get(nom) != None:
        diccionario[nom].append(diccionario_int)
    else:
        diccionario[nom] = [diccionario_int]
    print(diccionario)
