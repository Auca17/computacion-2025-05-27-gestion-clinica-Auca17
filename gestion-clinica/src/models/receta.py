from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos, fecha=None):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = fecha if fecha is not None else datetime.now()

    def __str__(self):
        return (f"Receta para {self.__paciente__.obtener_dni()} "
                f"emitida por {self.__medico__.obtener_matricula()} "
                f"con medicamentos: {', '.join(self.__medicamentos__)}")