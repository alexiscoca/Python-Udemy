# En Python los arreglos se representan como "list"

lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]
print(lenguajes)

# Los array (list) empiezan en la posicion 0
# Con el [x] se le indica el indice de la lista que queremos
print(lenguajes[0])         # Imprime Python

# Metodo que ordena los elementos
lenguajes.sort()            #.sort es un metodo que ordena alfabeticamente
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f"Estoy aprendiendo {lenguajes[3]}" 
print(aprendiendo)

# Remplazamos el valor del indice 2 por otro valor
lenguajes[2] = "PHP"
print(lenguajes)

# Agregar un elemento a la lista con el metodo "append"
lenguajes.append("Ruby")
print(lenguajes)

# Eliminamos el indice 1 de la lista con el metodo "del"
del lenguajes[1]
print(lenguajes)

# Eliminar el ultimo elemento
lenguajes.pop()
print(lenguajes)

# Eliminar con pop una pocision en especifico
lenguajes.pop(0)
print(lenguajes)

# Eliminar por nombre con el metodo "remove"
lenguajes.remove("PHP")
print(lenguajes)