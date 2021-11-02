from django.shortcuts import redirect, render
from .models import Vehiculo
from .formulario import formularioVehiculo

# Create your views here.


def listarvehiculo(request):

    vehiculo = Vehiculo.objects.all()
    diccionario_lista_vehiculo = {
        'vehiculos':vehiculo
    }
    return render(request,'index.html',diccionario_lista_vehiculo)


def crearVehiculo(request):
    ctx = None
    if request.method == "GET":
      formulario = formularioVehiculo()
      ctx = {'formulario':formulario}
    else:
      formulario = formularioVehiculo(request.POST)
      ctx = {'formulario':formulario}
      if formulario.is_valid():
          formulario.save()
          return redirect('index')
    return render(request,'crear.html',ctx)


def editarVehiculo(request,id):
    vehiculo = Vehiculo.objects.get(id = id)
    if request.method == "GET":
        formulario = formularioVehiculo(instance=vehiculo)
        ctx = {"formulario":formulario}
    else:
        formulario = formularioVehiculo(request.POST,instance=vehiculo)
        ctx = {"formulario":formulario}
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    return render(request,'crear.html', ctx)


def eliminar(request,id):
    vehiculo = Vehiculo.objects.get(id = id)
    vehiculo.delete()
    return redirect('index')
