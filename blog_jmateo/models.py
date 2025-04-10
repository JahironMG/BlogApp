from django.db import models # libreria basica
from django.utils import timezone #Librerias para utilizar las fechas

# Create your models here.
# Modelo basico con la estuctura de los datos que almacenaremos.
class Post(models.Model):
    # ELemos basicos de mi blog de notas:
    titulo = models.CharField(max_length=152)
    slug = models.SlugField(max_length=152)
    contenido = models.TextField()

    # Elementos con las fechas a mostrar:
    publicacion = models.DateTimeField(default=timezone.now)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    # Clase para el ordenamiento por fecha en que se publicaron los blos:
    class Meta:
        ordering = ['-publicacion']

    def __str__(self):
        return self.titulo



