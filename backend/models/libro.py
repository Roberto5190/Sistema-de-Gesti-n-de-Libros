from flask_sqlalchemy import SQLAlchemy
from . import db

class Libro:
    """
    Representa un libro en el sistema.

    Args:
        titulo (str)
        autor (str)
        precio (float): > 0
        stock (int): unidades disponibles (≥ 0)
    """

    def __init__(self, titulo: str, autor: str, precio: float, stock: int = 0) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = precio
        self.__stock = stock

    
    # -- TITULO ----------------------------------------
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    # -- AUTOR ----------------------------------------
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    # -- PRECIO ----------------------------------------
    @property
    def precio(self):
        return self.__precio
    
    @autor.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor

    # -- STOCK ----------------------------------------
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo")
        self.__stock = valor



    # -- HELPERS ----------------------------------------
    def to_dict(self) -> dict:
        """
        Convierte el libro a un diccionario.

        Returns:
            dict: Representación del libro como diccionario.
        """
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "precio": self.precio,
            "stock": self.stock
        }
    
    def __repr__(self) -> str:
        """
        Representación en cadena del libro.

        Returns:
            str: Representación del libro.
        """
        return f"Libro(titulo={self.titulo}, autor={self.autor}, precio={self.precio}, stock={self.stock})"




