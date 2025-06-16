class Especialidad:
    DIAS_VALIDOS = [
        "lunes",
        "martes",
        "miércoles",
        "jueves",
        "viernes",
        "sábado",
        "domingo",
    ]

    def __init__(self, tipo: str, dias: list[str]):
        self.__tipo__ = tipo
        # Solo acepta días válidos
        self.__dias__ = [d for d in dias if d.lower() in self.DIAS_VALIDOS]

    def obtener_especialidad(self) -> str:
        return self.__tipo__

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in (d.lower() for d in self.__dias__)

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias__)
        return f"{self.__tipo__} (Días: {dias_str})"
