from django.shortcuts import render

from .models import Oficina


def oficinas(request):
    oficinas = Oficina.objects.all()
    context = {
        'oficinas': oficinas
    }
    return render(request, 'base/oficinas.html', context=context)
