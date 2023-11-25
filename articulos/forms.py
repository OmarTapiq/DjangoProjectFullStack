
from django import forms
from .models import Comentario

class FormularioComentario(forms.ModelForm):
     class Meta:#configurar el comportamiento de la clase 
         model=Comentario
         fields=('comentario','autor')
