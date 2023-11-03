from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.productos, name='productos'),
    path('crearProducto', views.crearProducto, name='crearProducto'),
    path('listarProductos', views.listarProductos, name='listarProductos'),
    path('editarProducto/<int:id>', views.editarProducto, name='editarProducto'),
    path('borrarProducto/<int:id>', views.borrarProducto, name='borrarProducto')
]