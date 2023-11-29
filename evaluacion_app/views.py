from django.shortcuts import render,redirect
from .forms import ReservaForm
from evaluacion_app.models import Reservas

class Persona(object):
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

def index(request):
    persona1 = Persona("21", "Manuel Huenubil", "ManuelHuenubil@hotmail.com")
    context = {
        "id_persona": persona1.id,
        "nom_persona": persona1.nombre,
        "email_persona": persona1.email
    }
    return render(request, 'index.html', context)


def listadoReserva(request):
    reservas = Reservas.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)


def agregarReserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a donde quieras después de guardar la reserva
    else:
        form = ReservaForm()
    
    return render(request, 'agregar.html', {'form': form})

def modificarReserva(request, IN_id):
    reserva = Reservas.objects.get(id = IN_id)
    form = ReservaForm(instance=reserva)

    if (request.method == 'POST'):
        form = ReservaForm(request.POST, instance=reserva)
        if (form.is_valid()):
            form.save()
        return redirect('/reservas')
  
    data = {'form': form}
    return render (request, 'agregar.html', data)

def eliminarReserva(request, IN_id):
    reserva = Reservas.objects.get(id = IN_id)
    reserva.delete()
    return redirect('/reservas')