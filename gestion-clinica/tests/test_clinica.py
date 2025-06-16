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
        self.assertIn(self.paciente.obtener_dni(), self.clinica.__pacientes__)

    def test_agregar_medico(self):
        self.assertIn(self.medico.obtener_matricula(), self.clinica.__medicos__)

    def test_agendar_turno(self):
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), 
                                  "Cardiología", self.turno.obtener_fecha_hora())
        self.assertTrue(any(
            t.__paciente__ == self.turno.__paciente__ and
            t.__medico__ == self.turno.__medico__ and
            t.__fecha_hora__ == self.turno.__fecha_hora__ and
            t.__especialidad__ == self.turno.__especialidad__
            for t in self.clinica.__turnos__
        ))

    def test_emitir_receta(self):
        self.clinica.emitir_receta(self.paciente.obtener_dni(), 
                                   self.medico.obtener_matricula(), ["Aspirina"])
        recetas = self.clinica.__historias_clinicas__[self.paciente.obtener_dni()].obtener_recetas()
        self.assertTrue(any(
            r.__paciente__ == self.paciente and
            r.__medico__ == self.medico and
            r.__medicamentos__ == ["Aspirina"]
            for r in recetas
        ))

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta(self.paciente.obtener_dni(), self.medico.obtener_matricula(), [])

    def test_turno_no_duplicado(self):
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), 
                                  "Cardiología", self.turno.obtener_fecha_hora())
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), 
                                      "Cardiología", self.turno.obtener_fecha_hora())

    def test_paciente_no_encontrado(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.obtener_historia_clinica("99999999")

    def test_medico_no_disponible(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno(self.paciente.obtener_dni(), "M0000", 
                                      "Cardiología", self.turno.obtener_fecha_hora())

    def test_no_permite_paciente_duplicado(self):
        from src.models.paciente import Paciente
        paciente2 = Paciente("Juan Perez", "12345678", "01/01/1990")
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(paciente2)

    def test_no_permite_medico_duplicado(self):
        from src.models.medico import Medico
        medico2 = Medico("Dr. Smith", "M1234")
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(medico2)

    def test_agregar_especialidad_a_medico_no_registrado(self):
        from src.models.especialidad import Especialidad
        especialidad = Especialidad("Neurología", ["martes"])
        medico = self.clinica.obtener_medico_por_matricula("NOEXISTE")
        self.assertIsNone(medico)

    def test_turno_en_dia_no_atendido(self):
        from datetime import datetime
        # El médico solo atiende lunes y miércoles, probamos un viernes
        fecha_viernes = datetime(2025, 6, 20, 10, 0)  # viernes
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), "Cardiología", fecha_viernes)

    def test_historia_clinica_guarda_turnos_y_recetas(self):
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), "Cardiología", self.turno.obtener_fecha_hora())
        self.clinica.emitir_receta(self.paciente.obtener_dni(), self.medico.obtener_matricula(), ["Aspirina"])
        historia = self.clinica.obtener_historia_clinica(self.paciente.obtener_dni())
        self.assertTrue(len(historia.obtener_turnos()) > 0)
        self.assertTrue(len(historia.obtener_recetas()) > 0)

    def test_str_historia_clinica(self):
        historia = self.clinica.obtener_historia_clinica(self.paciente.obtener_dni())
        self.assertIn("Historia Clínica de", str(historia))

    def test_obtener_pacientes_y_medicos(self):
        pacientes = self.clinica.obtener_pacientes()
        medicos = self.clinica.obtener_medicos()
        self.assertIn(self.paciente, pacientes)
        self.assertIn(self.medico, medicos)

    def test_obtener_turnos(self):
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), 
                                   "Cardiología", self.turno.obtener_fecha_hora())
        turnos = self.clinica.obtener_turnos()
        self.assertTrue(any(
            t.__paciente__ == self.turno.__paciente__ and
            t.__medico__ == self.turno.__medico__ and
            t.__fecha_hora__ == self.turno.__fecha_hora__ and
            t.__especialidad__ == self.turno.__especialidad__
            for t in turnos
        ))

    def test_emitir_receta_paciente_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("99999999", self.medico.obtener_matricula(), ["Aspirina"])

    def test_emitir_receta_medico_inexistente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.emitir_receta(self.paciente.obtener_dni(), "NOEXISTE", ["Aspirina"])

    def test_historia_clinica_nueva_vacia(self):
        paciente_nuevo = Paciente("Nuevo Paciente", "87654321", "02/02/1990")
        self.clinica.agregar_paciente(paciente_nuevo)
        historia = self.clinica.obtener_historia_clinica(paciente_nuevo.obtener_dni())
        self.assertEqual(historia.obtener_turnos(), [])
        self.assertEqual(historia.obtener_recetas(), [])

if __name__ == '__main__':
    unittest.main()