class PacienteNoEncontradoException(Exception):
    """Excepción lanzada cuando un paciente no se encuentra en el sistema."""

    def __init__(self, dni):
        super().__init__(f"Paciente con DNI {dni} no encontrado.")
        self.dni = dni


class MedicoNoDisponibleException(Exception):
    """Excepción lanzada cuando un médico no está disponible para un turno."""

    def __init__(self, matricula):
        super().__init__(f"Médico con matrícula {matricula} no disponible.")
        self.matricula = matricula


class TurnoOcupadoException(Exception):
    """Excepción lanzada cuando se intenta agendar un turno que ya está ocupado."""

    def __init__(self, fecha_hora):
        super().__init__(f"Turno ya ocupado para la fecha y hora {fecha_hora}.")
        self.fecha_hora = fecha_hora


class RecetaInvalidaException(Exception):
    """Excepción lanzada cuando una receta es inválida."""

    def __init__(self, mensaje):
        super().__init__(mensaje)
