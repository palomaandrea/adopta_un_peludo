from django.shortcuts import render

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