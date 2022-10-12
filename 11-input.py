# nombre = input("Cuál es tu nombre: \r\n")
# print(f"Hola {nombre}")

# Leer datos que serán números

edad = input("Cual es tu edad?")
# convertir edad (string) a un entero (int)
edad = int(edad)  #tambien existen float, int, str

if edad >= 18:
    print("Ya puedes votar")
else:
    print("Aún no puedes votar")

# Mezclarlo con operadores

numero = input("Agrega un numero y te dire si es un par o no \r\n")

numero = int(numero)

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")