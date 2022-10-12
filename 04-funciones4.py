# Declaramos una variable
nombre = "Alexis"

# Le pasamos la variable a nuestra funcion y la imprimimos
def mostrar_nombre(nombre):
    print(f"Hola {nombre}")

mostrar_nombre(nombre)      # 

# Imprimimos 2 veces la variable con 2 metodos
print(nombre.upper())       # Imprime toda la cadena en MAYUSCULAS
print(nombre.lower())       # Imprime toda la cadena en minusculas