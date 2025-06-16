class Medico:
    def __init__(self, nombre: str, matricula: str):
        # Validación de nombre
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del médico no puede estar vacío.")
        if any(char.isdigit() for char in nombre):
            raise ValueError("El nombre del médico no puede contener números.")

        # Validación de matrícula
        if not matricula or not matricula.strip():
            raise ValueError("La matrícula no puede estar vacía ni ser solo espacios.")

        self.__nombre__ = nombre  
        self.__matricula__ = matricula  
        self.__especialidades__ = []  

    def agregar_especialidad(self, especialidad):
        # Evitar duplicados por nombre de especialidad
        nombres = [e.obtener_especialidad().lower() for e in self.__especialidades__]
        if especialidad.obtener_especialidad().lower() not in nombres:
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