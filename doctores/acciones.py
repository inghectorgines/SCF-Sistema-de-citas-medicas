import doctores.doctor as modelo
import consultas.acciones 

class Acciones:

    def registro(self):
        print("****** Se realizara tu registro en el sistema ******")

        nombre = input("¿Cual es su nombre? ")
        apellidos = input("¿Cuales son sus apellidos? ")
        consultorio = input("¿Cual es su numero de tu consultorio? ")
        direccion = input("¿Cual es tu direccion? ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        doctor = modelo.Doctor(nombre,apellidos,consultorio,direccion,email,password)
        registro = doctor.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre}, te haz registrado con el email {registro[1].email}")
        else:
            print("\nNo te haz registrado correctamente !!!")


    def login(self):
        print("*******Identificate en el sistema******")
        #try:
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")
        doctor = modelo.Doctor('', '', '', '', email, password)
        login = doctor.identificar()

        if email == login[5]:
            print(f"Bienvenido {login[1]},has ingresado con el email {login[5]} en el sistema")
            self.proximasAcciones(login)

        """ except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print("\n Login incorrecto intentalo mas tarde ") """
        
    def proximasAcciones(self, doctor):
        print("""
Menu de acciones 

    1. Crear consulta
    2. Mostrar consultas
    3. Modificar consulta
    4. Eliminar consulta
    5. salir
""")
        
        accion = input("Ingresa el número de opcion: ")
        op = consultas.acciones.Acciones()

        if accion == "1":
            op.crear(doctor)
            self.proximasAcciones(doctor)
        elif accion == "2":
            op.listar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "3":
            op.actualizar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "4":
            op.eliminar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "5":
            print("Adios")
            exit()
