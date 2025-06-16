class Medico:
    def __init__(self, nombre: str, matricula: str):
        self.__nombre__ = nombre  
        self.__matricula__ = matricula  
        self.__especialidades__ = []  

    def agregar_especialidad(self, especialidad):
        self.__especialidades__.append(especialidad)  

    def obtener_matricula(self) -> str:
        return self.__matricula__  

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for especialidad in self.__especialidades__:  
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None

    def __str__(self) -> str:
        especialidades_str = ', '.join(e.obtener_especialidad() for e in self.__especialidades__)  
        return f"{self.__nombre__} (Matrícula: {self.__matricula__}, Especialidades: {especialidades_str})"  