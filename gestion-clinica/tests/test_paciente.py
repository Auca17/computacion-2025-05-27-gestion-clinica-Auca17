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

class TestPacienteValidaciones(unittest.TestCase):

    def test_dni_con_mas_de_8_digitos(self):
        with self.assertRaises(ValueError):
            Paciente("Juan Perez", "1234567890123456789012345", "01/01/1990")

    def test_dni_con_letras(self):
        with self.assertRaises(ValueError):
            Paciente("Juan Perez", "12A4567B", "01/01/1990")

    def test_fecha_nacimiento_mes_invalido(self):
        with self.assertRaises(ValueError):
            Paciente("Juan Perez", "12345678", "01/39/1990")

    def test_fecha_nacimiento_dia_invalido(self):
        with self.assertRaises(ValueError):
            Paciente("Juan Perez", "12345678", "32/01/1990")

    def test_fecha_nacimiento_formato_invalido(self):
        with self.assertRaises(ValueError):
            Paciente("Juan Perez", "12345678", "1990-01-01")

if __name__ == '__main__':
    unittest.main()