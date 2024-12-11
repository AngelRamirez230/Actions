from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria
from .forms import CategoriaForm
from .models import Producto
from .forms import ProductoForm


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def principal(request):
    return render(request, 'paginas/principal.html')

def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/index.html', {'categorias': categorias})

def crearL(request):
    formulario = CategoriaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'categoria/crear.html', {'formulario':formulario})

def editarL(request,id):
    categoria=Categoria.objects.get(id=id)
    formulario = CategoriaForm(request.POST or None, request.FILES or None, instance=categoria)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index')
    return render(request, 'categoria/editar.html', {'formulario':formulario})

def borrar(request,id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('index')

def indexP(request):
    producto = Producto.objects.all()
    return render(request, 'producto/indexP.html', {'producto': producto})

def crearP(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('indexP')
    return render(request, 'producto/crearP.html', {'formulario': formulario})

def editarP(request, id):
    producto = Producto.objects.get(id=id)  # Busca el producto por su ID
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)  # Instancia del formulario
    if formulario.is_valid() and request.POST:
        formulario.save()  # Guarda el formulario actualizado
        return redirect('indexP')  # Redirige a la página principal (u otra)
    return render(request, 'producto/editarP.html', {'formulario': formulario})  # Renderiza la plantilla de edición

def borrarP(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('indexP')
