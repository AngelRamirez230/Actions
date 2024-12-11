from django import forms
from .models import Categoria
from .models import Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),  # Obtén todas las categorías
        widget=forms.Select,  # Usa un dropdown (select) para mostrar las opciones
        label="Selecciona una categoría",  # Etiqueta para el campo
        empty_label="Elige una categoría",  # Opción vacía por defecto
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria']  # Incluye los campos que quieras mostrar