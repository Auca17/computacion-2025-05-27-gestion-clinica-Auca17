import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.turno import Turno
from src.models.receta import Receta
from src.models.historia_clinica import HistoriaClinica


class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Ana Gómez", "98765432", "02/02/1980")
        self.medico = Medico("Dr. House", "M9999")
        self.especialidad = Especialidad("Clínica Médica", ["lunes", "jueves"])
        self.medico.agregar_especialidad(self.especialidad)
        self.turno = Turno(
            self.paciente, self.medico, datetime(2025, 7, 3, 9, 0), "Clínica Médica"
        )
        self.receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_y_obtener_turno(self):
        self.historia.agregar_turno(self.turno)
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0], self.turno)

    def test_agregar_y_obtener_receta(self):
        self.historia.agregar_receta(self.receta)
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertEqual(recetas[0], self.receta)

    def test_historia_clinica_vacia(self):
        self.assertEqual(self.historia.obtener_turnos(), [])
        self.assertEqual(self.historia.obtener_recetas(), [])

    def test_str_historia_clinica(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        texto = str(self.historia)
        self.assertIn("Historia Clínica de", texto)
        self.assertIn("Turnos:", texto)
        self.assertIn("Recetas:", texto)
        self.assertIn(str(self.turno), texto)
        self.assertIn(str(self.receta), texto)


if __name__ == "__main__":
    unittest.main()
