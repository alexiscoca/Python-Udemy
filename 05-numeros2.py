# Funcion suma con parametros
def suma(a = 0, b = 0):
    print(a + b)
# La funcion va a hacer la suma de 2 parametros "a" y "b"
# le pasamos los valores que querramos a la funcion
suma(2, 3)      # Imprime 5
suma(2, 5)      # Imprime 7
suma(10)        # Imprime 10 (10 + 0 = 10)

# Funcion resta con 2 parametros
def resta(a = 0, b = 0):
    print(a - b)

resta(5 - 2)        # Imprime 3
resta(10 -10)       # Imprime 0
resta(7)            # Imprime 7 (7 - 0 = 7)