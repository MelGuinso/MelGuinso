from django.test import TestCase
from django.contrib.auth.models import User
from control_estudios.models import Curso

class CursoTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
    def test_creacion_curso(self):
        curso = Curso(nombre="Titulo", comision=1000, creador=self.user)
        curso.save()

        self.assertEqual(Curso.objects.count(), 1)
        self.assertEqual(curso.nombre, "Titulo")
        self.assertEqual(curso.comision, 1000)
        self.assertEqual(curso.creador, self.user)

    def test_curso_str(self):
        curso = Curso(nombre="Python", comision=20000, creador=self.user)
        curso.save()

        self.assertEqual(curso.__str__(), "Python, 20000")