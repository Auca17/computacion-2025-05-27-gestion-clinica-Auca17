class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        self.__tipo__ = tipo
        self.__dias__ = dias

    def obtener_especialidad(self) -> str:
        return self.__tipo__

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in (d.lower() for d in self.__dias__)

    def __str__(self) -> str:
        dias_str = ', '.join(self.__dias__)
        return f"{self.__tipo__} (Días: {dias_str})"