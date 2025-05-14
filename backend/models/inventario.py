class Inventario:
    def __init__(self):
        self._libros = []  # Lista que almacenará los libros

    # Método para agregar un libro al inventario
    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise ValueError("El objeto no es una instancia de la clase Libro")
        self._libros.append(libro)

    # Método para buscar un libro por su título
    def buscar_libro(self, titulo):
        for libro in self._libros:
            if libro.titulo == titulo:
                return libro
        return None

    # Método para registrar una venta de un libro
    def registrar_venta(self, titulo, cantidad):
        libro = self.buscar_libro(titulo)
        if libro is None:
            raise ValueError('Libro no encontrado')
        
        # Verificamos si hay suficiente stock
        if libro.cantidad < cantidad:
            raise ValueError('No hay suficiente stock para esta venta')
        
        # Restamos la cantidad del stock
        libro.cantidad -= cantidad
        print(f"Venta registrada: {cantidad} ejemplares de '{libro.titulo}' vendidos.")

        # Log de la venta (puede ser una lista o simplemente imprimir en consola)
        print(f"Venta registrada en el log: {cantidad} ejemplares de '{libro.titulo}'.")


