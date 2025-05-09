from django.shortcuts import render, get_object_or_404

from .models import Oficina

'''
def oficinas(request):
    oficinas = Oficina.objects.all()
    context = {
        'oficinas': oficinas
    }
    return render(request, 'base/oficinas.html', context=context)
'''

def oficina_detalle(request, id):
    oficina = get_object_or_404(Oficina, id=id)
    return render(request, 'base/oficina.html', {'oficina': oficina})

def oficina_lista(request):
    oficinas = Oficina.objects.all()
    return render(request, 'base/oficinas.html', {'oficinas': oficinas})

