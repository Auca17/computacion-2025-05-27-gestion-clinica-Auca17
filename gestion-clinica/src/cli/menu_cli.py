
class CLI:
    def __init__(self, clinica):
        self.clinica = clinica

    def mostrar_menu(self):
        while True:
            print("--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Agregar especialidad")
            print("5) Emitir receta")
            print("6) Ver historia clínica")
            print("7) Ver todos los turnos")
            print("8) Ver todos los pacientes")
            print("9) Ver todos los médicos")
            print("0) Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.agregar_medico()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.agregar_especialidad()
            elif opcion == "5":
                self.emitir_receta()
            elif opcion == "6":
                self.ver_historia_clinica()
            elif opcion == "7":
                self.ver_turnos()
            elif opcion == "8":
                self.ver_pacientes()
            elif opcion == "9":
                self.ver_medicos()
            elif opcion == "0":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def run(self):
        self.mostrar_menu()

    def agregar_paciente(self):
        try:
            nombre = input("Ingrese el nombre del paciente: ")
            dni = input("Ingrese el DNI del paciente: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
            from src.models.paciente import Paciente
            paciente = Paciente(nombre, dni, fecha_nacimiento)
            self.clinica.agregar_paciente(paciente)
            print(f"Paciente {nombre} registrado correctamente.")
        except Exception as e:
            print(f"Error: {e}")

    def agregar_medico(self):
        try:
            nombre = input("Ingrese el nombre del médico: ")
            matricula = input("Ingrese la matrícula del médico: ")
            from src.models.medico import Medico
            medico = Medico(nombre, matricula)
            self.clinica.agregar_medico(medico)
            print(f"Médico {nombre} registrado correctamente.")
        except Exception as e:
            print(f"Error: {e}")

    def agendar_turno(self):
        try:
            dni = input("Ingrese el DNI del paciente: ")
            matricula = input("Ingrese la matrícula del médico: ")
            especialidad = input("Ingrese la especialidad: ")
            fecha_hora_str = input("Ingrese la fecha y hora del turno (YYYY-MM-DD HH:MM): ")
            from datetime import datetime
            fecha_hora = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("Turno agendado correctamente.")
        except Exception as e:
            print(f"Error: {e}")

    def agregar_especialidad(self):
        try:
            matricula = input("Ingrese la matrícula del médico: ")
            especialidad_nombre = input("Ingrese la especialidad: ")
            dias_str = input("Ingrese los días de atención (separados por comas): ")
            dias = [dia.strip() for dia in dias_str.split(",")]
            
            from src.models.especialidad import Especialidad
            especialidad = Especialidad(especialidad_nombre, dias)
            
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            if not medico:
                print(f"No se encontró médico con matrícula {matricula}.")
                return
                
            medico.agregar_especialidad(especialidad)
            print(f"Especialidad {especialidad_nombre} agregada correctamente.")
        except Exception as e:
            print(f"Error: {e}")

    def emitir_receta(self):
        try:
            dni = input("Ingrese el DNI del paciente: ")
            matricula = input("Ingrese la matrícula del médico: ")
            medicamentos_str = input("Ingrese los medicamentos (separados por comas): ")
            medicamentos = [med.strip() for med in medicamentos_str.split(",")]
            
            self.clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida correctamente.")
        except Exception as e:
            print(f"Error: {e}")

    def ver_historia_clinica(self):
        try:
            dni = input("Ingrese el DNI del paciente: ")
            historia = self.clinica.obtener_historia_clinica(dni)
            print(historia)
        except Exception as e:
            print(f"Error: {e}")

    def ver_turnos(self):
        try:
            turnos = self.clinica.obtener_turnos()
            if not turnos:
                print("No hay turnos registrados.")
            else:
                print("Turnos registrados:")
                for turno in turnos:
                    print(turno)
        except Exception as e:
            print(f"Error al obtener turnos: {e}")

    def ver_pacientes(self):
        try:
            pacientes = self.clinica.obtener_pacientes()
            if not pacientes:
                print("No hay pacientes registrados.")
            else:
                print("Pacientes registrados:")
                for paciente in pacientes:
                    print(paciente)
        except Exception as e:
            print(f"Error al obtener pacientes: {e}")

    def ver_medicos(self):
        try:
            medicos = self.clinica.obtener_medicos()
            if not medicos:
                print("No hay médicos registrados.")
            else:
                print("Médicos registrados:")
                for medico in medicos:
                    print(medico)
        except Exception as e:
            print(f"Error al obtener médicos: {e}")