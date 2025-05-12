from django.shortcuts import render, get_object_or_404

from .models import Oficina


def oficinas(request):
    oficinas = Oficina.objects.all()
    context = {
        'oficinas': oficinas
    }
    return render(request, 'base/oficinas.html', context=context)

def detalle_oficina(request, oficina_id):
    oficina = get_object_or_404(Oficina, id=oficina_id)
    context = {
        'oficina': oficina
    }
    return render(request, 'base/detalle_oficina.html', context=context)