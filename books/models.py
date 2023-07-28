from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Para que en el panel de administrador se vea el titulo y no se vea un object(object).
    def __str__(self):
        return self.title
    