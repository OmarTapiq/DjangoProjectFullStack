
from django import forms
from .models import Comentario

class FormularioComentario(forms.ModelForm):
    class Meta:#configurar el comportamiento de la clase 
        model=Comentario
        fields=('comentario',)
        
        
    def __init__(self, *args, **kwargs):
        usuario_autenticado = kwargs.pop('usuario_autenticado', None)
        super().__init__(*args, **kwargs)
        
        # Asegúrate de que el campo 'autor' esté en los campos definidos
        if 'autor' in self.fields:
            self.fields['autor'].initial = usuario_autenticado
            self.fields['autor'].widget = forms.HiddenInput()