from flask_sqlalchemy import SQLAlchemy
from models import db

class Libro:
    def __init__(self, titulo, autor, precio):
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = precio
    
    # TITULO
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    # AUTOR
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def titulo(self, nuevo_autor):
        self.__autor = nuevo_autor
    
    # PRECIO
    @property
    def precio(self):
        return self.__precio
    
    @autor.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("Precio negativo")
        self.__precio = valor


class LibroModel(db.Model):
    __tablename__ = 'libros'  # El nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Campo de identificación
    titulo = db.Column(db.String(255), nullable=False)  # Columna para el título
    autor = db.Column(db.String(255), nullable=False)  # Columna para el autor
    precio = db.Column(db.Float, nullable=False)  # Columna para el precio

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __repr__(self):
        return f"<Libro {self.titulo} de {self.autor}, Precio: {self.precio}>"