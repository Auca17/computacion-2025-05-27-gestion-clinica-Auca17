from .historia_clinica import HistoriaClinica
from .turno import Turno
from .receta import Receta
from src.exceptions.clinica_exceptions import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException, 
    TurnoOcupadoException,
    RecetaInvalidaException
)

class Clinica:
    def __init__(self):
        self.__pacientes__ = {}
        self.__medicos__ = {}
        self.__turnos__ = []
        self.__historias_clinicas__ = {}

    def agregar_paciente(self, paciente):
        if paciente.obtener_dni() in self.__pacientes__:
            raise ValueError("El paciente ya está registrado.")
        self.__pacientes__[paciente.obtener_dni()] = paciente
        self.__historias_clinicas__[paciente.obtener_dni()] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        if medico.obtener_matricula() in self.__medicos__:
            raise ValueError("El médico ya está registrado.")
        self.__medicos__[medico.obtener_matricula()] = medico

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException("Paciente no encontrado.")
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException("Médico no encontrado.")

        medico = self.__medicos__[matricula]
        # Traduce el día a español
        dia_espanol = self.obtener_dia_semana_en_espanol(fecha_hora)
        if not medico.obtener_especialidad_para_dia(dia_espanol.lower()):
            raise MedicoNoDisponibleException("El médico no atiende esa especialidad en el día solicitado.")

        if any(turno.obtener_fecha_hora() == fecha_hora and turno.obtener_medico().obtener_matricula() == matricula for turno in self.__turnos__):
            raise TurnoOcupadoException("El turno ya está ocupado.")

        paciente = self.__pacientes__[dni]
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos__.append(turno)
        self.__historias_clinicas__[dni].agregar_turno(turno)

    def emitir_receta(self, dni, matricula, medicamentos):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException("Paciente no encontrado.")
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException("Médico no encontrado.")
        if not medicamentos:
            raise RecetaInvalidaException("La receta debe contener al menos un medicamento.")

        paciente = self.__pacientes__[dni]
        medico = self.__medicos__[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas__[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni):
        if dni not in self.__historias_clinicas__:
            raise PacienteNoEncontradoException("Historia clínica no encontrada.")
        return self.__historias_clinicas__[dni]

    def obtener_pacientes(self):
        return list(self.__pacientes__.values())

    def obtener_medicos(self):
        return list(self.__medicos__.values())

    def obtener_medico_por_matricula(self, matricula):
        return self.__medicos__.get(matricula)

    def validar_existencia_paciente(self, dni):
        return dni in self.__pacientes__

    def validar_existencia_medico(self, matricula):
        return matricula in self.__medicos__

    def validar_turno_no_duplicado(self, matricula, fecha_hora):
        return not any(turno.obtener_fecha_hora() == fecha_hora and turno.obtener_medico().obtener_matricula() == matricula for turno in self.__turnos__)

    def obtener_dia_semana_en_espanol(self, fecha_hora):
        """Traduce un objeto datetime al día de la semana en español."""
        dias = {
            "Monday": "lunes",
            "Tuesday": "martes", 
            "Wednesday": "miércoles",
            "Thursday": "jueves",
            "Friday": "viernes",
            "Saturday": "sábado",
            "Sunday": "domingo"
        }
        return dias[fecha_hora.strftime("%A")]

    def obtener_especialidad_disponible(self, medico, dia_semana):
        """Obtiene la especialidad disponible para un médico en un día."""
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico, especialidad_solicitada, dia_semana):
        """Verifica que el médico atienda esa especialidad ese día."""
        especialidad_disponible = self.obtener_especialidad_disponible(medico, dia_semana)
        if not especialidad_disponible:
            return False
        return especialidad_disponible.lower() == especialidad_solicitada.lower()
