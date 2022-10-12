#Creando un diccionario

cancion = {
    "Artista" : "Bad Bunny",
    "Cancion" : "La Santa",
    "Reproducciones" : "Un chingo",
    "Lanzamiento" : 2019
}
#Acceder a los elementos del diccionario
print(cancion["Cancion"])
print(cancion["Reproducciones"])

#Mezclar con un string
artista = cancion["Cancion"]
artist = cancion["Artista"]
print(f"Estoy escuchando {artista} de {artist}")
print(cancion)

#Agregar nuevos valores
cancion["playlist"] = "Reggaeton HP"
print(cancion)

#Remplzar un valor ya existente
cancion["cancion"] = "Haciendo que me amas"
print(cancion)

#Eliminar un valor
del cancion["Lanzamiento"]
print(cancion)