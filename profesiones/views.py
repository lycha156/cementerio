from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesion
from .forms import ProfesionForm
from django.contrib import messages
from django.db.models import Q

template = 'profesiones'
titulo = 'PROFESIONES'

def index(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        profesiones = Profesion.objects.filter(profesion__icontains = query)
    else:
        profesiones = Profesion.objects.all()

    context = {
        'titulo': titulo,
        'profesiones': profesiones
    }
    return render(request, f'{template}/index.html', context)

def create(request):
    form = ProfesionForm()
    if request.method == 'POST':
        form = ProfesionForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Nueva profesion guardadad con exito.')
                return redirect(f'{template}_index')
            else:
                messages.warning(request, 'Error durante la carga de datos')
                return render(request, f'{template}_create.html', context = {'titulo': titulo, 'form': form})
        except Exception as e:
            messages.warning(request, f'Error al realizar la carga de datos. {e}')
            return redirect(f'{template}_index')

    context = {
        'titulo': titulo,
        'form': form,
    }
    return render(request, f'{template}/create.html', context)

def update(request, id=id):
    obj = get_object_or_404(Profesion, pk=id)
    form = ProfesionForm(request.POST or None, instance=obj)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos actualizados con exito.-')
            return redirect(f'{template}_index')
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect(f'{template}_index')

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, f'{template}/create.html', context)

def delete(request, id=id):
    profesion = get_object_or_404(Profesion, pk=id)
    if request.method == 'POST':
        try:
            profesion.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect(f'{template}_index')
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos del socio, posee registros relacionados. {e}')
            return redirect(f'{template}_index')
    context = {
        'titulo': titulo,
        'nacionalidad': profesion
    }
    return render(request, f'{template}/delete.html', context)
