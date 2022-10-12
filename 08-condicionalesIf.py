from traceback import print_tb


# Revisar si una condicion es mayor a
balance = 0
if balance > 0:
    print("Puedes pagar")
else:
    print("No puedes pagar")

# Likes
likes = 200
if likes >= 200:
    print("Bien, tienes 200 likes")
else:
    print("No tienes amigos")

# if con texto
lenguaje = "PHP"
if not lenguaje == "Python":
    print("Excelente decision")

# Evaluar un booleano
usuario_autenticado = True
if usuario_autenticado:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")