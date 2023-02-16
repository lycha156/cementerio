from django.shortcuts import render, redirect, get_object_or_404
from .models import CausaMuerte
from .forms import CausaMuerteForm
from django.contrib import messages
from django.db.models import Q

template = 'causasmuertes'
titulo = 'CAUSAS DE MUERTE'

def index(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        cmuertes = CausaMuerte.objects.filter(causa__icontains = query)
    else:
        cmuertes = CausaMuerte.objects.all()

    context = {
        'titulo': titulo,
        'cmuertes': cmuertes
    }
    return render(request, f'{template}/index.html', context)

def create(request):
    form = CausaMuerteForm()
    if request.method == 'POST':
        form = CausaMuerteForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Nueva Causa de Muerte guardadad con exito.')
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
    obj = get_object_or_404(CausaMuerte, pk=id)
    form = CausaMuerteForm(request.POST or None, instance=obj)

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
    cmuerte = get_object_or_404(CausaMuerte, pk=id)
    if request.method == 'POST':
        try:
            cmuerte.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect(f'{template}_index')
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos del socio, posee registros relacionados. {e}')
            return redirect(f'{template}_index')
    context = {
        'titulo': titulo,
        'cmuerte': cmuerte
    }
    return render(request, f'{template}/delete.html', context)
