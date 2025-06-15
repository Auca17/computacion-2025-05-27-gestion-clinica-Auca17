class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        self.__paciente__ = paciente          # Should be self.__paciente__
        self.__medico__ = medico              # Should be self.__medico__
        self.__fecha_hora__ = fecha_hora      # Should be self.__fecha_hora__
        self.__especialidad__ = especialidad  # Should be self.__especialidad__

    def obtener_medico(self):
        return self.__medico__  # Changed from __medico__

    def obtener_fecha_hora(self):
        return self.__fecha_hora__  # Changed from __fecha_hora__

    def __str__(self):
        return f"Turno: {self.__paciente__}, Médico: {self.__medico__}, Especialidad: {self.__especialidad__}, Fecha/Hora: {self.__fecha_hora__}"  # Changed all attributes

    @staticmethod
    def verificar_conflicto(turnos, fecha_hora, matricula):
        return any(turno.obtener_fecha_hora() == fecha_hora and turno.obtener_medico().obtener_matricula() == matricula for turno in turnos)