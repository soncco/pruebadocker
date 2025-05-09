from django.urls import path
from .views import oficina_lista, oficina_detalle

app_name = 'base'
urlpatterns = [
    path('oficinas/', oficina_lista, name='oficinas'),
    path('oficina/<int:id>/', oficina_detalle, name='oficina_detalle'),
]
