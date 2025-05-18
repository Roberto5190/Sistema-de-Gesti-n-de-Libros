from .libro import Libro

class Inventario:
    def __init__(self):
        self._libros : dict[str, Libro] = {}  # Diccionario que almacenará los libros

    # Método para agregar un libro al inventario
    def agregar_libro(self, libro) -> None:
        if not isinstance(libro, Libro):
            raise ValueError("El objeto no es una instancia de la clase Libro")
        
        if libro.titulo in self._libros:
            raise ValueError(f"El libro '{libro.titulo}' ya existe en el inventario")
        
        self._libros[libro.titulo] = libro # Agregamos el libro al diccionario usando su título como clave

    # Método para buscar un libro por su título
    def buscar_libro(self, titulo: str) -> Libro:
        titulo_lower = titulo.lower()
        for libro in self._libros.values():
            if libro.titulo.lower() == titulo_lower:
                return libro
        return None

    # Método para registrar una venta de un libro
    def registrar_venta(self, titulo: str, cantidad: int) -> None:
        libro = self.buscar_libro(titulo)
        if libro is None:
            raise ValueError('Libro no encontrado')
        
        # Verificamos si hay suficiente stock
        if libro.stock < cantidad:
            raise ValueError('No hay suficiente stock para esta venta')
        
        # Restamos la cantidad del stock
        libro.stock -= cantidad
        print(f"Venta registrada: {cantidad} ejemplares de '{libro.titulo}' vendidos.")

        # Log de la venta (puede ser una lista o simplemente imprimir en consola)
        print(f"Venta registrada en el log: {cantidad} ejemplares de '{libro.titulo}'.")



    #  -- HELPERS ----------------------------------------
    # -- LISTA LIBROS DEL INVENTARIO --
    def listar_libros(self) -> list[dict]:
        """
        Lista todos los libros en el inventario.

        Recorre todos los Libro almacenados y devuelve una lista de diccionarios,
        usando el método to_dict() de cada libro.

        Returns:
            list: Lista de libros en el inventario.
        """
        return [libro.to_dict() for libro in self._libros.values()]
    
    # -- LIBROS LENGTH --
    def __len__(self):
        """
        Devuelve la cantidad de libros en el inventario.

        Returns:
            int: Cantidad de libros en el inventario.
        """
        return len(self._libros)

    # -- LIBROS ITERATOR --
    def __iter__(self):
        """
        Permite iterar sobre los libros en el inventario.
        Devuelve un iterador sobre las instancias de Libro.

        ej: for libro in inv:
                print(libro.titulo, libro.stock)

        return:
            Libro: Cada libro en el inventario.
        """
        return iter(self._libros.values())