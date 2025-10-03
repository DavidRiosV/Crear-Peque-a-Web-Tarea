from django.shortcuts import render
from .models import Juegos,Tienda,Desarrollador

# Create your views here.
def index(request):
    return render(request, 'Juegos/index.html') 

def juegos_list(request):
    juego=Juegos.objects.all()  
    return render(request, 'Juegos/Juegos_list.html',{'juegos_mostrar':juego})

def tienda_list(request):
    tienda=Tienda.objects.all()
    return render(request, 'Juegos/Tienda_list.html',{'tienda_mostrar':tienda})

def desarrollador_list(request):
    desarrollador=Desarrollador.objects.all()
    return render(request, 'Juegos/Desarrollador_list.html',{'desarrollador_mostrar':desarrollador})