from django.shortcuts import render, redirect, get_object_or_404
from .models import Nacionalidad
from .forms import NacionalidadForm
from django.contrib import messages
from django.db.models import Q

template = 'nacionalidades'

def index(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        nacionalidades = Nacionalidad.objects.filter(nacionalidad__icontains = query)
    else:
        nacionalidades = Nacionalidad.objects.all()

    context = {
        'titulo': 'NACIONALIDADES',
        'nacionalidades': nacionalidades
    }
    return render(request, f'{template}/index.html', context)

def create(request):
    form = NacionalidadForm()
    if request.method == 'POST':
        form = NacionalidadForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Nueva nacionalidad guardadad con exito.')
                return redirect(f'{template}_index')
            else:
                messages.warning(request, 'Error durante la carga de datos')
                return render(request, f'{template}_create.html', context = {'titulo': 'NACIONALIDAD', 'form': form})
        except Exception as e:
            messages.warning(request, f'Error al realizar la carga de datos. {e}')
            return redirect(f'{template}_index')

    context = {
        'titulo': 'NACIONALIDAD',
        'form': form,
    }
    return render(request, f'{template}/create.html', context)

def update(request, id=id):
    obj = get_object_or_404(Nacionalidad, pk=id)
    form = NacionalidadForm(request.POST or None, instance=obj)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos actualizados con exito.-')
            return redirect(f'{template}_index')
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect(f'{template}_index')

    context = {
        'titulo': 'NACIONALIDAD',
        'form': form
    }
    return render(request, f'{template}/create.html', context)

def delete(request, id=id):
    nacionalidad = get_object_or_404(Nacionalidad, pk=id)
    if request.method == 'POST':
        try:
            nacionalidad.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect(f'{template}_index')
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos del socio, posee registros relacionados. {e}')
            return redirect(f'{template}_index')
    context = {
        'titulo': 'NACIONALIDAD',
        'nacionalidad': nacionalidad
    }
    return render(request, f'{template}/delete.html', context)
