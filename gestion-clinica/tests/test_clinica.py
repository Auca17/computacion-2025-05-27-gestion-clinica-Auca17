import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime
from src.models.clinica import Clinica
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.turno import Turno
from src.models.receta import Receta
from src.models.historia_clinica import HistoriaClinica
from src.exceptions.clinica_exceptions import PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException, RecetaInvalidaException

class TestClinica(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dr. Smith", "M1234")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.turno = Turno(self.paciente, self.medico, datetime(2025, 6, 16, 10, 0), "Cardiología")
        self.receta = Receta(self.paciente, self.medico, ["Aspirina"], datetime.now())

        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)

    def test_agregar_paciente(self):
        self.assertIn(self.paciente.obtener_dni(), self.clinica._Clinica__pacientes__)

    def test_agregar_medico(self):
        self.assertIn(self.medico.obtener_matricula(), self.clinica._Clinica__medicos__)

    def test_agendar_turno(self):
        # Using getter methods instead of direct attribute access
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), 
                                  "Cardiología", self.turno.obtener_fecha_hora())
        self.assertIn(self.turno, self.clinica._Clinica__turnos)

    def test_emitir_receta(self):
        # Using getter methods
        self.clinica.emitir_receta(self.paciente.obtener_dni(), 
                                 self.medico.obtener_matricula(), ["Aspirina"])
        self.assertIn(self.receta, self.clinica.__historias_clinicas__[self.paciente.obtener_dni()].obtener_recetas())

    def test_turno_no_duplicado(self):
        # Using getter methods
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), 
                                  "Cardiología", self.turno.obtener_fecha_hora())
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), 
                                      "Cardiología", self.turno.obtener_fecha_hora())

    def test_paciente_no_encontrado(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.obtener_historia_clinica("99999999")

    def test_medico_no_disponible(self):
        # Using getter methods
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno(self.paciente.obtener_dni(), "M0000", 
                                      "Cardiología", self.turno.obtener_fecha_hora())

if __name__ == '__main__':
    unittest.main()