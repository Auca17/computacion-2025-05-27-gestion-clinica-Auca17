import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.models.medico import Medico
from src.models.especialidad import Especialidad


class TestMedico(unittest.TestCase):

    def setUp(self):
        self.medico = Medico("Dr. Juan Pérez", "12345")
        self.especialidad = Especialidad(
            "Cardiología", ["lunes", "miércoles", "viernes"]
        )

    def test_agregar_especialidad(self):
        self.medico.agregar_especialidad(self.especialidad)
        self.assertIn(self.especialidad, self.medico.__especialidades__)

    def test_obtener_matricula(self):
        self.assertEqual(self.medico.obtener_matricula(), "12345")

    def test_obtener_especialidad_para_dia(self):
        self.medico.agregar_especialidad(self.especialidad)
        self.assertEqual(
            self.medico.obtener_especialidad_para_dia("lunes"), "Cardiología"
        )
        self.assertIsNone(self.medico.obtener_especialidad_para_dia("martes"))

    def test_str_representation(self):
        self.medico.agregar_especialidad(self.especialidad)
        expected_str = "Dr. Juan Pérez (Matrícula: 12345, Especialidades: Cardiología)"
        self.assertEqual(str(self.medico), expected_str)

    def test_no_especialidad_duplicada(self):
        self.medico.agregar_especialidad(self.especialidad)
        # Intentar agregar la misma especialidad otra vez
        self.medico.agregar_especialidad(self.especialidad)
        especialidades = [
            e.obtener_especialidad() for e in self.medico.__especialidades__
        ]
        # Debe haber solo una especialidad "Cardiología"
        self.assertEqual(especialidades.count("Cardiología"), 1)


class TestMedicoValidaciones(unittest.TestCase):

    def test_matricula_vacia(self):
        with self.assertRaises(ValueError):
            Medico("Dr. House", "")

    def test_matricula_con_espacios(self):
        with self.assertRaises(ValueError):
            Medico("Dr. House", "   ")

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Medico("", "M1234")

    def test_nombre_con_numeros(self):
        with self.assertRaises(ValueError):
            Medico("Dr. 1234", "M1234")


if __name__ == "__main__":
    unittest.main()
