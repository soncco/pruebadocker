from django.urls import path
from .views import oficinas

app_name = 'base'
urlpatterns = [
    path('oficinas/', oficinas, name='oficinas'),
]
