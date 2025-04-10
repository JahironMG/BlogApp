from django.db import models # libreria basica
from django.utils import timezone #Librerias para utilizar las fechas
from django.contrib.auth.models import User

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(estado=Post.Status.PUBLISHED)

# Modelo basico con la estuctura de los datos que almacenaremos.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # ELemos basicos de mi blog de notas:
    titulo = models.CharField(max_length=152)
    #slug = models.SlugField(unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blognotas')
    contenido = models.TextField()

    # Elementos con las fechas a mostrar:
    publicacion = models.DateTimeField(default=timezone.now)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLISHED)

    #Gestores de modelo
    objects = models.Manager()
    published = PublishedManager()
    # Clase para el ordenamiento por fecha en que se publicaron los blos:
    class Meta:
        ordering = ['-publicacion']

        # Ordenamiento del campo publicacion:
        indexes = [
            models.Index(fields=['-publicacion']),
        ]

    def __str__(self):
        return self.titulo



