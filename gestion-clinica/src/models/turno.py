class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad

    def obtener_medico(self):
        return self.__medico__

    def obtener_fecha_hora(self):
        return self.__fecha_hora__

    def __str__(self):
        return f"Turno: {self.__paciente__}, Médico: {self.__medico__}, Especialidad: {self.__especialidad__}, Fecha/Hora: {self.__fecha_hora__}"

    @staticmethod
    def verificar_conflicto(turnos, fecha_hora, matricula):
        return any(
            turno.obtener_fecha_hora() == fecha_hora
            and turno.obtener_medico().obtener_matricula() == matricula
            for turno in turnos
        )
