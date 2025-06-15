import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.receta import Receta

class TestReceta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dr. Smith", "M12345")
        self.medicamentos = ["Paracetamol", "Ibuprofeno"]
        self.receta = Receta(self.paciente, self.medico, self.medicamentos)

    def test_crear_receta(self):
        self.assertEqual(self.receta.__paciente__, self.paciente)
        self.assertEqual(self.receta.__medico__, self.medico)
        self.assertEqual(self.receta.__medicamentos__, self.medicamentos)

    def test_str_receta(self):
        expected_str = f"Receta para {self.paciente.obtener_dni()} emitida por {self.medico.obtener_matricula()} con medicamentos: {', '.join(self.medicamentos)}"
        self.assertEqual(str(self.receta), expected_str)

    def test_fecha_emision(self):
        self.assertIsInstance(self.receta.__fecha__, datetime)

if __name__ == '__main__':
    unittest.main()