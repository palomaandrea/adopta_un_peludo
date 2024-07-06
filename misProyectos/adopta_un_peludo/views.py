from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'adopta_un_peludo/index.html', context)