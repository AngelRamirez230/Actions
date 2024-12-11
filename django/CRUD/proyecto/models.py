from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(max_length=100, verbose_name='Descripcion de categoria')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos', verbose_name='Categoría')

    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio} - Categoría ID: {self.categoria.id}"









