
class Usuario:
    def __init__(self, username, password):
        self.username = username
        self._password = password  # Atributo privado de la contraseña

    def autenticar(self, pwd):
        """Método base de autenticación. Compara la contraseña."""
        return pwd == self._password

class Moderador(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password)

    def autenticar(self, pwd):
        """Autenticación personalizada para moderadores. La contraseña debe empezar con 'mod_'."""
        if pwd.startswith('mod_'):
            return super().autenticar(pwd)  # Llamamos al método de la clase base
        return False

class Admin(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password)

    def autenticar(self, pwd):
        """Autenticación personalizada para admin. La contraseña debe tener un carácter especial."""
        if any(char in pwd for char in ['@', '#', '$', '%', '^', '&', '*', '!', '?']):
            return super().autenticar(pwd)  # Llamamos al método de la clase base
        return False




# Función de login
def login(usuario: Usuario, pwd: str) -> bool:
    """Función que utiliza el método autenticar de las clases Usuario, Moderador o Admin."""
    return usuario.autenticar(pwd)
