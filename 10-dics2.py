#Iniciar un diccionario vacio

jugador = {}
print(jugador)

# Se une un jugador
# [""] es la llave y "" es el valor de la llave
jugador["Nombre"] = "Alexis"
jugador["Puntaje"] = "0"
print(jugador)

# Incrementa el puntaje
jugador["Puntaje"] = "100"
print(jugador)


# Acceder a un valor
print(jugador.get("consola", "No existe ese valor"))

# Iterar en el diccionario
# Esto va a imprimir las llaves (nombre y puntaje) con los valores (Alexisy 100) de jugador
for llave, valor in jugador.items():
    print(llave)
    print(valor)

# Eliminar un jugador
del jugador["Nombre"]
del jugador["Puntaje"]
print(jugador)