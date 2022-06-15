import consultas.consulta as modelo

class Acciones:
    def crear(self, doctor):
        print(f"OK, {doctor[1]}. Ingrese datos de consulta ")
        
        paciente = input("Introduzca nombre de su paciente: ")
        apellidos = input("Introduzca los apellidos de su paciente: ")
        edad = input("Introduzca la edad de su paciente: ")
        telefono = input("Induzca el telefono de su paciente: ")
        consultorio = input("Ingrese consultorio: ")
        asunto = input("Introduzca el asunto de su paciente: ")
        sexo = input("Introduzca el genero de su paciente(m/f): ")

        consulta = modelo.Consulta(doctor[0], paciente, apellidos, edad, telefono, consultorio, asunto, sexo)
        guardar = consulta.guardar()
        if guardar[0] >= 1:
            print(f"\n Perfecto! has guardado la consulta de: {consulta.paciente}")
        else:
            print(f"\nNo se guardo tu consulta {doctor[1]}!!!")

    def listar(self, doctor):
        print(f"\n{doctor[1]}, {doctor[0]}!! Estas son sus consultas: ")
        consulta = modelo.Consulta(doctor[0])
        consultas = consulta.listar()

        #print(consultas)
        for consulta in consultas:
            print("\n***********")
            print(f"Nombre del paciente: {consulta[2]}")
            print(f"Fecha de la consulta: {consulta[9]}")
            print(f"Asunto: {consulta[7]}")
            print(f"consultorio: {consulta[6]}")
            print("\n***********")

    def actualizar(self, doctor):
        print(f"\n[{doctor[0]}]Dr. {doctor[1]}.  Modifique una consulta")

        paciente = input("Introduzca el nombre de su  paciente para modificar sus datos: ")

        consulta = modelo.Consulta(doctor[0], paciente)
        validar = consulta.validar()
        if validar[0] != 0:
            self.modificar(doctor, paciente)
        else:
            print(f"\nNo se encontró ninguna consulta con el nombre del paciente {paciente}")

    def modificar(self, doctor, nombre):
        print(f"\n[{doctor[0]}]Dr. {doctor[1]} Ingrese los nuevos datos de su paciente {nombre}")

        paciente = input("Introduzca nombre de su paciente: ")
        apellidos = input("Introduzca los apellidos de su paciente: ")
        edad = input("Introduzca la edad de su paciente: ")
        telefono = input("Induzca el telefono de su paciente: ")
        consultorio = input("Ingrese consultorio: ")
        asunto = input("Introduzca el asunto de su paciente: ")
        sexo = input("Introduzca el genero de su paciente(m/f): ")

        consulta = modelo.Consulta(doctor[0], paciente, apellidos, edad, telefono, consultorio, asunto, sexo, nombre)
        guardar = consulta.actualizar()
        if guardar[0] >= 1:
            print(f"\nSe han modificado correctamente los datos de su paciente: {consulta.paciente}.\n")
        else:
            print(f"\nNo se pudo modificar la consulta agendada del paciente, intentelo más tarde: {doctor[1]}")


    def eliminar(self, doctor):
        print(f"\n[{doctor[1]}] {doctor[1]} {doctor[2]}. Elimine una consulta")
        paciente = input("Introduzca el nombre del paciente para eliminar su consulta: ")

        nota = modelo.Consulta(doctor[0], paciente)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"\nSe eliminó la consulta de {nota.paciente}")
        else:
            print("\nNo se puedo eliminar la consulta, intentelo más tarde...")
