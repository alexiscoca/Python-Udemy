# Funcion con parametros dentro del parentesis
from cmath import inf


def informacion(nombre, puesto = "Desconocido"):
    print(f"Soy {nombre} y soy {puesto}")

# Imprimimos con los parametros que querramos
informacion("Pedro", "Programador")
informacion("Alexis", "chef")
informacion("Luis", "Obrero")
informacion("Memo", "MVZ")