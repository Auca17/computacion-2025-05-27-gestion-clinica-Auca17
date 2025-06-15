import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime
from src.models.turno import Turno
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dr. Smith", "M1234")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)
        self.fecha_hora = datetime(2025, 6, 15, 10, 0)
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora, self.especialidad.obtener_especialidad())

    def test_obtener_medico(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico)

    def test_obtener_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_str_representation(self):
        expected_str = f"Turno: {self.paciente}, Médico: {self.medico}, Especialidad: {self.especialidad.obtener_especialidad()}, Fecha/Hora: {self.fecha_hora}"
        self.assertEqual(str(self.turno), expected_str)

if __name__ == '__main__':
    unittest.main()