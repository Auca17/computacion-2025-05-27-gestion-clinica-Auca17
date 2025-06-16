import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.models.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def setUp(self):
        self.especialidad = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])

    def test_obtener_especialidad(self):
        self.assertEqual(self.especialidad.obtener_especialidad(), "Pediatría")

    def test_verificar_dia_true(self):
        self.assertTrue(self.especialidad.verificar_dia("lunes"))
        self.assertTrue(self.especialidad.verificar_dia("Miércoles"))  # mayúsculas/minúsculas

    def test_verificar_dia_false(self):
        self.assertFalse(self.especialidad.verificar_dia("domingo"))

    def test_str(self):
        expected = "Pediatría (Días: lunes, miércoles, viernes)"
        self.assertEqual(str(self.especialidad), expected)

    def test_especialidad_dias_invalidos(self):
        # Días inválidos (no existen en español)
        especialidad = Especialidad("Dermatología", ["funday", "lunes"])
        self.assertTrue(especialidad.verificar_dia("lunes"))
        self.assertFalse(especialidad.verificar_dia("funday"))

if __name__ == '__main__':
    unittest.main()