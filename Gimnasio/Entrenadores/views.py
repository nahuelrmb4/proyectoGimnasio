from django.shortcuts import render, redirect
from .models import Entrenador, Clase
from .forms import entrenadorForm, claseForm

# Create your views here.

def listarEntrenadores(request):
    entrenadores = Entrenador.objects.all()
    contexto = {
        'titulo': 'Lista de Entrenadores',
        'entrenadores': entrenadores
    }
    return render(request, 'Entrenadores/listaEntrenadores.html', contexto)

def crearEntrenador(request):
    formulario = entrenadorForm()
    contexto = {
        'form': formulario,
        'mensaje': 'Nuevo Entrenador'
    }
    if request.method == 'POST':
        formularioPOST = entrenadorForm(request.POST)
        if formularioPOST.is_valid():
            formularioPOST.save()
            return redirect('listaEntrenadores')
        else:
            contexto['mensaje'] += 'Error en el formulario'
            contexto['form'] = formularioPOST
            return render(request, 'Entrenadores/formEntrenador.html', contexto)
    else:
        return render(request, 'Entrenadores/formEntrenador.html', contexto)

def editarEntrenador(request, id):
    entrenadorEditar = Entrenador.objects.get(pk=id)
    formEditar = entrenadorForm(instance=entrenadorEditar)
    contextoGet = {
        'form': formEditar,
        'mensaje': 'Editar Entrenador'
    }
    if request.method == 'GET':
        return render(request, 'Entrenadores/formEntrenador.html', contextoGet)

    else:
        formGuardar = entrenadorForm(request.POST, instance=entrenadorEditar)
        if formGuardar.is_valid():
            formGuardar.save()
            return redirect('listaEntrenadores')

def borrarEntrenador(request, id):
    entrenadorBorrar = Entrenador.objects.get(pk=id)
    entrenadorBorrar.delete()
    return redirect('listaEntrenadores')


def listarClases(request):
    clases = Clase.objects.all()
    contexto = {
        'titulo': 'Lista de Clases',
        'clases': clases
    }
    return render(request, 'Entrenadores/listaClases.html', contexto)

def crearClase(request):
    formulario = claseForm()
    contexto = {
        'form': formulario,
        'mensaje': 'Agregar Clase'
    }
    if request.method == 'POST':
        formularioPOST = claseForm(request.POST)
        if formularioPOST.is_valid():
            formularioPOST.save()
            return redirect('listaClases')
        else:
            contexto['mensaje'] += 'Error en el formulario'
            contexto['form'] = formularioPOST
            return render(request, 'Entrenadores/formClase.html', contexto)
    else:
        return render(request, 'Entrenadores/formClase.html', contexto)