from flask_sqlalchemy import SQLAlchemy

# Creamos la instancia de SQLAlchemy
db = SQLAlchemy()

# Importamos los modelos de la aplicación
# Estos modelos representan la lógica de negocio y no están directamente relacionados con la base de datos
from .libro import Libro
from .inventario import Inventario
from .usuario import Usuario, Moderador, Admin, login

# Importamos los modelos de la base de datos
from .libro_model import LibroModel


__all__ = [
    "db",
    "Libro",
    "Inventario",
    "Usuario",
    "Moderador",
    "Admin",
    "login",
    "LibroModel",
]
# Exponemos los modelos para que puedan ser utilizados en otras partes de la aplicación