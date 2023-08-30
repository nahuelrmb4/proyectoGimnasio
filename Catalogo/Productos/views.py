from django.shortcuts import render, redirect
from .forms import *
from .models import Producto

# Create your views here.

def productos(request):
    return render(request, 'Productos/index.html')

def crearProducto(request):
    #Se crea la instancia del formulario
    formulario = productoForm()
    #Se crea el contexto para enviar valores al template
    contexto = {
        'form': formulario,
        'mensaje': 'Crear Producto'
    }
    #Si la petición es por POST se procesan los valores ingresados
    if request.method == 'POST':
        formularioPOST = productoForm(request.POST)
        #Si los valores son válidos se crea un nuevo registro
        if formularioPOST.is_valid:
            formularioPOST.save()
            #Luego de guardar se redirecciona a la ruta de Productos
            return redirect('productos')
        #Si no son válidos
        else:
            #Se actualizan los valores del contexto
            contexto['mensaje']  += '-Error en el formulario.'
            contexto['form'] = formularioPOST
            #Se vuelve a mostrar el template con los valores del formulario para que el usuario encuentre el error.
            return render(request, 'Productos/formProducto.html', contexto)
    #Si la petición no es por POST entonces es por GET. Se muestra el formulario en blanco para que el usuario cargue los valores.
    else:
        return render(request, 'Productos/formProducto.html', contexto)
     

def listarProductos(request):
    #Consulta a la BDD a través del ORM de Django
    productos = Producto.objects.all()

    contexto = {
        'titulo': 'Lista de Productos',
        'productos': productos
    }

    return render(request, 'Productos/listaProductos.html', contexto)


def editarProducto(request, id):
    #se obtiene el registro en base a su id
    productoEditar = Producto.objects.get(pk=id)
    contextoGet = {
        'form': formEditar,
        'mensaje': 'Editar Producto'
    }
    if request.method == 'GET':
        formEditar = productoForm(instance=productoEditar)
        return render(request, 'Productos/formProducto.html', contextoGet)

    else:
        formGuardar = productoForm(request.POST, instance=productoEditar)
        if formGuardar.is_valid():
            formGuardar.save()
            #Redirecciona a la url que lista los productos
            return redirect('listarProductos')


def borrarProducto(request, id):
    productoBorrar = Producto.objects.get(pk=id)
    productoBorrar.delete()
    return redirect('listarProductos')