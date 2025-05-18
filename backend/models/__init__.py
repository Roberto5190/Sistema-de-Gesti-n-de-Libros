from flask_sqlalchemy import SQLAlchemy

# Creamos la instancia de SQLAlchemy
db = SQLAlchemy()

from .libro import Libro
from .inventario import Inventario
from .usuario import Usuario, Moderador, Admin, login




__all__ = [
    "db",
    "Libro",
    "Inventario",
    "Usuario",
    "Moderador",
    "Admin",
    "login",
]
# Exponemos los modelos para que puedan ser utilizados en otras partes de la aplicación