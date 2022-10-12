# Evaluar un elemento de un lista
lenguajes = ["Python", "Kotlin", "Java", "JavaScript", "PHP"]
if "PHP" in lenguajes:
    print("PHP si existe")
else:
    print("No está en la lista")


# If anidados
usuario_autenticado = False
usuario_admin = False
if usuario_autenticado:
    if usuario_admin:
        print("Acceso total")
    else:
        print("Acceso al sistema")
else:
    print("Debes iniciar sesion")