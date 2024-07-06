#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('donaciones', views.donaciones, name='donaciones'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('tienda', views.tienda, name='tienda'),
]
