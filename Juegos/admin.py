from django.contrib import admin
from .models import Juegos
from .models import Tienda
from .models import Desarrollador

admin.site.register(Juegos)
admin.site.register(Tienda)
admin.site.register(Desarrollador)