#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('donaciones', views.donaciones, name='donaciones'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('tienda', views.tienda, name='tienda'),
    path('inicia_sesion', views.inicia_sesion, name='inicia_sesion'),
    path('crear_cuenta', views.crear_cuenta, name='crear_cuenta'),
    path('listadoSQL', views.listadoSQL, name='listadoSQL')
]
