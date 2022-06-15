import doctores.acciones
print("Samara Castro Flores 9°A")
print("""
Accede al sistema:
    -Iniciar sesion
    -Registrarse
""")

opcion = doctores.acciones.Acciones()
accion = input("¿Que quieres hacer?: ")

if accion == "Iniciar sesion":
    opcion.login()
elif accion == "Registrarse":
    opcion.registro()
