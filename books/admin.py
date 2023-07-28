from django.contrib import admin
from .models import Book

# Register your models here.
# Añadir el modelo para poder utilizarlo en el panel de administrador.
admin.site.register(Book)
