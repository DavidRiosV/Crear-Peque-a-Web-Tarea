from django.urls import path
from.import views

urlpatterns = [
        path('',views.index,name='index.html'),
        path('juegos',views.juegos_list, name='Juegos_list'),
        path('tienda',views.tienda_list, name='Tienda_list'),
        path('desarrollador',views.desarrollador_list, name='Desarrollador_list'),
]       