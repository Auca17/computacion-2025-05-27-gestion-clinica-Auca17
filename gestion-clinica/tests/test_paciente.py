import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.models.paciente import Paciente

class TestPaciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")

    def test_obtener_dni(self):
        self.assertEqual(self.paciente.obtener_dni(), "12345678")

    def test_str_representation(self):
        self.assertEqual(str(self.paciente), "Paciente: Juan Perez, DNI: 12345678, Fecha de Nacimiento: 01/01/1990")

    def test_fecha_nacimiento(self):
        self.assertEqual(self.paciente.__fecha_nacimiento__, "01/01/1990")

if __name__ == '__main__':
    unittest.main()