class HistoriaClinica:
    def __init__(self, paciente):
        self.__paciente__ = paciente
        self.__turnos__ = []
        self.__recetas__ = []

    def agregar_turno(self, turno):
        self.__turnos__.append(turno)

    def agregar_receta(self, receta):
        self.__recetas__.append(receta)

    def obtener_turnos(self):
        return self.__turnos__.copy()

    def obtener_recetas(self):
        return self.__recetas__.copy()

    def __str__(self):
        turnos_str = "\n".join(str(turno) for turno in self.__turnos__)
        recetas_str = "\n".join(str(receta) for receta in self.__recetas__)
        return f"Historia Clínica de {self.__paciente__}:\nTurnos:\n{turnos_str}\nRecetas:\n{recetas_str}"
