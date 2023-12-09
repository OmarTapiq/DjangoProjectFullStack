from django.db import models
from django.conf import settings
from django.urls import reverse
import uuid
#cada vez que se modifica un modelo se tiene que hacer la migracion
# Create your models here.
class Articulo(models.Model):
    id = models.UUIDField(#se intenta agregar lo de los identificadores universales
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    titulo=models.CharField(max_length=255)
    cuerpo=models.TextField()
    fecha= models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=20, blank=True)#nuevo
    categoria = models.CharField(max_length=20,blank=False) 
    imagen = models.ImageField(blank=True,null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,  # Permite que el campo sea nulo en la base de datos
        blank=True,  # Permite que el formulario se envíe sin un autor seleccionado
    )
  
    def __str__(self):
        return self.titulo
    
    #vistas dinamicas
    # def get_absolute_url(self):
    #         #cargar la url apartir del nombre
    #     return reverse("detalle_articulo", kwargs={"pk": self.pk})
    def get_absolute_url(self):
        return reverse("detalle_articulo", args=[str(self.id)])
    
class Comentario(models.Model):
    Articulo=models.ForeignKey(Articulo,on_delete=models.CASCADE)
    comentario=models.CharField(max_length=140)
    autor=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.comentario
    
    #caudno creamos un comentario nos lleva a esta url
    def get_absolute_url(self):
        return reverse("lista_articulos")
