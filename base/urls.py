from django.urls import path
from .views import oficinas
from . import views
app_name = 'base'

urlpatterns = [
    path('oficinas/', views.oficinas, name='oficinas'),
    path('oficina/<int:oficina_id>/', views.detalle_oficina, name='detalle_oficina')
]
