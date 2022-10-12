#Operadores AND y OR

# Variables con 2 booleanos
usuario_logeado = True
usuario_admin = False

# Si el usuario_logeado y el usuario_admin son ambos TRUE entonces imprime "Administrador"
# Si usuario_logeado es TRUE imprime "Acceso al sistema"
# Y si ninguna de las anteriores es verdad (TRUE) imprime "Debes iniciar sesion"
if usuario_logeado and usuario_admin:
    print("Administrador")
elif usuario_logeado: 
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")


#OR
usuario_logeado = False
usuario_admin = True

if usuario_logeado or usuario_admin:
    print("Administrador")
elif usuario_logeado: 
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")