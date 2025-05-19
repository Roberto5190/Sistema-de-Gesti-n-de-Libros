"""
LibroModel  ⇄  Tabla 'libros'
Convierte entre la capa de persistencia y la clase de dominio Libro.
"""
from . import db  # Importamos la instancia de SQLAlchemy
from .libro import Libro  # Importamos la clase Libro

# ——————————————————————————————
# 3. Definir el modelo LibroModel
# Modelo de SQLAlchemy para la tabla de libros
# Este modelo se utiliza para interactuar con la base de datos
# y representa la estructura de la tabla 'libros'.
# ——————————————————————————————

class LibroModel(db.Model):
    __tablename__ = 'libros'  # El nombre de la tabla en la base de datos

    # --- Columnas ---------------------------------
    id = db.Column(db.Integer, primary_key=True)  # Campo de identificación
    titulo = db.Column(db.String(255), nullable=False)  # Columna para el título
    autor = db.Column(db.String(255), nullable=False)  # Columna para el autor
    precio = db.Column(db.Float, nullable=False)  # Columna para el precio
    stock = db.column(db.Integer, nullable=False, default=0)  # Columna para el stock

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __repr__(self):
        return f"<Libro {self.titulo} de {self.autor}, Precio: {self.precio}>"