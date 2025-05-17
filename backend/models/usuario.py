# -- USUARIO ------------------------------
class Usuario:
    ROLE = "usuario"

    def __init__(self, username: str, password: str):
        self.username = username
        self._password = password  # Almacenamos la contraseña de forma privada

    def autenticar(self, pwd: str) -> bool:
        """
        Método base de autenticación. Compara la contraseña.
        Args:
            pwd (str): Contraseña proporcionada para la autenticación.
            Returns:
            bool: True si la contraseña es correcta, False en caso contrario."""
        return pwd == self._password

# -- MODERADOR ------------------------------
class Moderador(Usuario):
    ROLE = "moderador" 
    
    def __init__(self, username: str, password: str):
        super().__init__(username, password)

    def autenticar(self, pwd: str) -> bool:
        """
        Autenticación personalizada para moderadores.
        La contraseña debe empezar con 'mod_'.
        Args:
            pwd (str): Contraseña proporcionada para la autenticación.
        Returns:
            bool: True si la contraseña es correcta, False en caso contrario
        """
        if pwd.startswith('mod_'):
            return super().autenticar(pwd)  # Llamamos al método de la clase base
        return False


# -- ADMIN ------------------------------
class Admin(Usuario):
    ROLE = "admin"

    def __init__(self, username: str, password: str):
        super().__init__(username, password)

    def autenticar(self, pwd: str) -> bool:
        """
        Autenticación personalizada para admin. La contraseña debe tener un carácter especial.
        Args:
            pwd (str): Contraseña proporcionada para la autenticación.
        Returns:
            bool: True si la contraseña es correcta, False en caso contrario
        """
        if any(char in pwd for char in ['@', '#', '$', '%', '^', '&', '*', '!', '?']):
            return super().autenticar(pwd)  # Llamamos al método de la clase base
        return False




# Función de login
def login(usuario: Usuario, pwd: str) -> bool:
    """Función que utiliza el método autenticar de las clases Usuario, Moderador o Admin."""
    return usuario.autenticar(pwd)
