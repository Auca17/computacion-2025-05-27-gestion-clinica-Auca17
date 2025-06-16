from datetime import datetime


class Receta:
    def __init__(self, paciente, medico, medicamentos, fecha=None):
        if paciente is None:
            raise ValueError("El paciente no puede ser None.")
        if medico is None:
            raise ValueError("El médico no puede ser None.")
        if (
            not medicamentos
            or not isinstance(medicamentos, list)
            or any(not m or not isinstance(m, str) for m in medicamentos)
        ):
            raise ValueError("La receta debe contener al menos un medicamento válido.")
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = fecha if fecha is not None else datetime.now()

    def __str__(self):
        return (
            f"Receta para {self.__paciente__.obtener_dni()} "
            f"emitida por {self.__medico__.obtener_matricula()} "
            f"con medicamentos: {', '.join(self.__medicamentos__)}"
        )
