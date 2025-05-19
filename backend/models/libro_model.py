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
    stock = db.Column(db.Integer, nullable=False, default=0)  # Columna para el stock

    def to_dict(self):
        return {
            "id":    self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "precio": self.precio,
            "stock":  self.stock,
        }



    def update_from_dict(self, data: dict) -> None:
        """
        Actualiza solo los campos permitidos a partir de un dict.
        Valida tipos y reglas de negocio (precio>=0, stock>=0).
        """
        # Título y autor: si vienen, actualízalos
        if 'titulo' in data:
            nuevo = data['titulo'].strip()
            if not nuevo:
                raise ValueError("El título no puede quedar vacío")
            self.titulo = nuevo

        if 'autor' in data:
            nuevo = data['autor'].strip()
            if not nuevo:
                raise ValueError("El autor no puede quedar vacío")
            self.autor = nuevo

        # Precio: convertir a float y validar
        if 'precio' in data:
            try:
                p = float(data['precio'])
            except (TypeError, ValueError):
                raise ValueError("El precio debe ser un número")
            if p < 0:
                raise ValueError("El precio no puede ser negativo")
            self.precio = p

        # Stock: convertir a int y validar
        if 'stock' in data:
            try:
                s = int(data['stock'])
            except (TypeError, ValueError):
                raise ValueError("El stock debe ser un entero")
            if s < 0:
                raise ValueError("El stock no puede ser negativo")
            self.stock = s



    def __repr__(self):
        return f"<Libro {self.titulo} de {self.autor}, Precio: {self.precio}, Stock: {self.stock}>"