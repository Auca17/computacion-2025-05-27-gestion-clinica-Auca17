import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.models.medico import Medico
from src.models.especialidad import Especialidad

class TestMedico(unittest.TestCase):

    def setUp(self):
        self.medico = Medico("Dr. Juan Pérez", "12345")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles", "viernes"])

    def test_agregar_especialidad(self):
        self.medico.agregar_especialidad(self.especialidad)
        self.assertIn(self.especialidad, self.medico.__especialidades__)

    def test_obtener_matricula(self):
        self.assertEqual(self.medico.obtener_matricula(), "12345")

    def test_obtener_especialidad_para_dia(self):
        self.medico.agregar_especialidad(self.especialidad)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("lunes"), "Cardiología")
        self.assertIsNone(self.medico.obtener_especialidad_para_dia("martes"))

    def test_str_representation(self):
        self.medico.agregar_especialidad(self.especialidad)
        expected_str = "Dr. Juan Pérez (Matrícula: 12345, Especialidades: Cardiología)"
        self.assertEqual(str(self.medico), expected_str)

if __name__ == '__main__':
    unittest.main()