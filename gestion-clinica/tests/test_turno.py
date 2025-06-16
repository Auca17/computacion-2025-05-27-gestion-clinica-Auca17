import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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
        self.turno = Turno(
            self.paciente,
            self.medico,
            self.fecha_hora,
            self.especialidad.obtener_especialidad(),
        )

    def test_obtener_medico(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico)

    def test_obtener_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_str_representation(self):
        expected_str = f"Turno: {self.paciente}, Médico: {self.medico}, Especialidad: {self.especialidad.obtener_especialidad()}, Fecha/Hora: {self.fecha_hora}"
        self.assertEqual(str(self.turno), expected_str)


class TestTurnoExtras(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dr. Smith", "M1234")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)
        self.fecha_hora = datetime(2025, 6, 16, 10, 0)
        self.turno = Turno(
            self.paciente,
            self.medico,
            self.fecha_hora,
            self.especialidad.obtener_especialidad(),
        )

    def test_str_incluye_todo(self):
        texto = str(self.turno)
        self.assertIn("Turno:", texto)
        self.assertIn("Paciente:", texto)
        self.assertIn("Médico:", texto)
        self.assertIn("Cardiología", texto)
        self.assertIn(str(self.fecha_hora), texto)

    def test_verificar_conflicto_true(self):
        turnos = [self.turno]
        self.assertTrue(
            Turno.verificar_conflicto(
                turnos, self.fecha_hora, self.medico.obtener_matricula()
            )
        )

    def test_verificar_conflicto_false(self):
        turnos = [self.turno]
        otra_fecha = datetime(2025, 6, 17, 10, 0)
        self.assertFalse(
            Turno.verificar_conflicto(
                turnos, otra_fecha, self.medico.obtener_matricula()
            )
        )


if __name__ == "__main__":
    unittest.main()
