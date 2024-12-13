from django.test import TestCase
from .models import Categoria, Producto

class CategoriaModelTest(TestCase):
    
    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre='Electrónica',
            descripcion='Dispositivos y gadgets electrónicos.'
        )

    def test_categoria_creation(self):
        self.assertEqual(self.categoria.nombre, 'Electrónica')
        self.assertEqual(self.categoria.descripcion, 'Dispositivos y gadgets electrónicos.')

    def test_categoria_str(self):
        self.assertEqual(str(self.categoria), 'Electrónica')

class ProductoModelTest(TestCase):
    
    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre='Electrónica',
            descripcion='Dispositivos y gadgets electrónicos.'
        )
        self.producto = Producto.objects.create(
            nombre='Laptop',
            precio=999.99,
            categoria=self.categoria
        )

    def test_producto_creation(self):
        self.assertEqual(self.producto.nombre, 'Laptop')
        self.assertEqual(self.producto.precio, 999.99)
        self.assertEqual(self.producto.categoria, self.categoria)

    def test_producto_str(self):
        self.assertEqual(str(self.producto), 'Nombre: Laptop - Precio: 999.99 - Categoría ID: 5')

