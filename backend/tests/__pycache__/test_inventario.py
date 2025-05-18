
import unittest
from models.inventario import Inventario
from models.libro import Libro


# EJECUTAR DESDE LA RAIZ DEL PROYECTO
# comando: python -m unittest discover -s tests -p "test_*.py" -v


class TestInventario(unittest.TestCase):

    def setUp(self):
        """Este método se ejecuta antes de cada prueba."""
        # Crear libros de prueba
        self.libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 20, 10)
        self.libro2 = Libro("1984", "George Orwell", 15, 5)
        self.libro_invalido = None  # Intentaremos crear un libro con precio negativo

        # Crear un inventario
        self.inventario = Inventario()
        self.inventario.agregar_libro(self.libro1)
        self.inventario.agregar_libro(self.libro2)

    def test_crear_libro_valido(self):
        """Prueba que un libro con precio válido se crea correctamente."""
        self.assertEqual(self.libro1.titulo, "Cien años de soledad")
        self.assertEqual(self.libro1.precio, 20)
        self.assertEqual(self.libro1.stock, 10)

    def test_crear_libro_con_precio_negativo(self):
        """Prueba que no se pueda crear un libro con precio negativo."""
        with self.assertRaises(ValueError):
            self.libro_invalido = Libro("Libro con precio negativo", "Autor Desconocido", -10, 5)

    def test_buscar_libro_existente(self):
        """Prueba la búsqueda de un libro existente."""
        libro_buscado = self.inventario.buscar_libro("1984")
        self.assertIsNotNone(libro_buscado)
        self.assertEqual(libro_buscado.titulo, "1984")

    def test_buscar_libro_no_existente(self):
        """Prueba la búsqueda de un libro que no existe."""
        libro_buscado = self.inventario.buscar_libro("El Quijote")
        self.assertIsNone(libro_buscado)

    def test_registrar_venta_libro_disponible(self):
        """Prueba que se pueda registrar una venta de un libro con suficiente stock."""
        self.inventario.registrar_venta("1984", 2)
        libro_buscado = self.inventario.buscar_libro("1984")
        self.assertEqual(libro_buscado.cantidad, 3)  # Debería restar el stock

    def test_registrar_venta_libro_sin_stock(self):
        """Prueba que no se pueda registrar una venta si no hay suficiente stock."""
        with self.assertRaises(ValueError):
            self.inventario.registrar_venta("1984", 10)  # Solo hay 5 ejemplares

if __name__ == '__main__':
    unittest.main()
