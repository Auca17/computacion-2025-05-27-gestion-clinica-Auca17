from datetime import datetime


class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        self.__nombre__ = nombre
        self.__dni__ = dni
        self.__fecha_nacimiento__ = fecha_nacimiento
        if not dni.isdigit() or len(dni) != 8:
            raise ValueError("El DNI debe tener exactamente 8 dígitos numéricos.")
        if not self._validar_fecha(fecha_nacimiento):
            raise ValueError(
                "La fecha de nacimiento debe tener formato dd/mm/aaaa y ser válida."
            )

    def _validar_fecha(self, fecha: str) -> bool:
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def obtener_dni(self) -> str:
        return self.__dni__

    def __str__(self) -> str:
        return f"Paciente: {self.__nombre__}, DNI: {self.__dni__}, Fecha de Nacimiento: {self.__fecha_nacimiento__}"
