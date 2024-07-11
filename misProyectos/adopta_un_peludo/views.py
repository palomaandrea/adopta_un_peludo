from django.shortcuts import render

from .models import Usuario,Genero

# Create your views here.
def index(request):
    context={}
    return render(request, 'adopta_un_peludo/index.html', context)

def contacto(request):
    context={}
    return render(request, 'adopta_un_peludo/contacto.html', context)

def donaciones(request):
    context={}
    return render(request, 'adopta_un_peludo/donaciones.html', context)

def nosotros(request):
    context={}
    return render(request, 'adopta_un_peludo/nosotros.html', context)

def tienda(request):
    context={}
    return render(request, 'adopta_un_peludo/tienda.html', context)

def inicia_sesion(request):
    context={}
    return render(request, 'adopta_un_peludo/inicia_sesion.html', context)

def crear_cuenta(request):
    context={}
    return render(request, 'adopta_un_peludo/crear_cuenta.html', context)

def listadoSQL(request):
    usuarios= Usuario.objects.raw('SELECT * FROM instituto_usuario')
    print(usuarios)
    context={"usuarios":usuarios}
    return render(request, 'adopta_un_peludo/listadoSQL.html',context)