
import unittest
from .usuario import Usuario, Moderador, Admin
from .usuario import login

class TestUsuarios(unittest.TestCase):

    def setUp(self):
        """Este método se ejecuta antes de cada prueba."""
        # Crear instancias de Usuario, Moderador y Admin con contraseñas específicas
        self.usuario_normal = Usuario("usuario1", "12345")
        self.moderador = Moderador("moderador1", "mod_123")
        self.admin = Admin("admin1", "admin@123")

    def test_autenticar_usuario_normal(self):
        """Verifica que un Usuario normal solo acepte la contraseña exacta."""
        self.assertTrue(login(self.usuario_normal, "12345"))  # Contraseña correcta
        self.assertFalse(login(self.usuario_normal, "wrongpass"))  # Contraseña incorrecta

    def test_autenticar_moderador(self):
        """Verifica que un Moderador solo acepte contraseñas que empiecen con 'mod_'."""
        self.assertTrue(login(self.moderador, "mod_123"))  # Contraseña correcta para Moderador
        self.assertFalse(login(self.moderador, "123mod"))  # Contraseña no válida

    def test_autenticar_admin(self):
        """Verifica que un Admin solo acepte contraseñas con caracteres especiales."""
        self.assertTrue(login(self.admin, "admin@123"))  # Contraseña válida con '@'
        self.assertFalse(login(self.admin, "admin123"))  # Contraseña no válida sin caracteres especiales

if __name__ == "__main__":
    unittest.main()
