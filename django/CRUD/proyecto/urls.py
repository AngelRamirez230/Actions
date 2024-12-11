from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('principal', views.principal, name='principal'),
    path('index', views.index, name='index'),
    path('crear', views.crearL, name='crear'),
    path('editar', views.editarL, name='editar'),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path('editar/<int:id>', views.editarL, name='editar'),
    path('indexP', views.indexP, name='indexP'),
    path('crearP', views.crearP, name='crearP'),
    path('editarP', views.editarP, name='editarP'),
    path('editarP/<int:id>', views.editarP, name='editarP'),
    path('borrarP/<int:id>', views.borrarP, name='borrarP'),
]
