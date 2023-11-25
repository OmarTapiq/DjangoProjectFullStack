from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView,FormView
from .models import Articulo
from django.urls import reverse_lazy,reverse #modificada
from .forms import FormularioComentario
from django.views import View #movida
from django.views.generic.detail import SingleObjectMixin  #nueva
from .models import Articulo
from .forms import FormularioComentario

# Create your views here.
class VistaListaArticulos(ListView):
    model = Articulo
    template_name = 'lista_articulos.html'
    context_object_name = 'articulo_list'

    def get_queryset(self):
        # Obtén el parámetro de la URL llamado 'genero'
        genero = self.kwargs.get('genero', None)

        # Filtra los artículos por género si se proporciona el parámetro, de lo contrario, devuelve todos los artículos
        if genero:
            return Articulo.objects.filter(genero=genero)
        else:
            return Articulo.objects.all()
        
        
class VistaListaArticulosPorCategoria(ListView):
    model = Articulo
    template_name = 'lista_articulos_por_categoria.html'
    context_object_name = 'articulo_list'

    def get_queryset(self):
        # Obtén el parámetro de la URL llamado 'categoria'
        categoria = self.kwargs.get('categoria', None)

        # Filtra los artículos por categoría si se proporciona el parámetro, de lo contrario, devuelve todos los artículos
        if categoria:
            return Articulo.objects.filter(categoria=categoria)
        else:
            return Articulo.objects.all()

        
        
class VistaListaCategorias(ListView):
    model = Articulo
    template_name = 'lista_categorias.html'  # Crea este template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Articulo.objects.values_list('categoria', flat=True).distinct()
        return context
    
# class VistaArticulosPorCategoria(ListView):
#     model = Articulo
#     template_name = 'articulos_por_categoria.html'
#     context_object_name = 'articulo_list'

#     def get_queryset(self):
#         categoria_seleccionada = self.kwargs['categoria']
#         return Articulo.objects.filter(categoria=categoria_seleccionada)
    
# class VistaListaArticulos(ListView):
#     model=Articulo
#     template_name='lista_articulos.html'

class VistaDetalleArticulo(DetailView):
    model = Articulo
    template_name='detalle_articulo.html'

class VistaModificacionArticulo(UpdateView):
    model=Articulo
    fields=(
        'titulo',
        'cuerpo',
        'genero',
    )
    template_name='editar_articulo.html'
    success_url=reverse_lazy('lista_articulos')

class VistaEliminacionArticulo(DeleteView): 
    model = Articulo
    template_name= 'eliminar_articulo.html'
    success_url=reverse_lazy('lista_articulos')
    object_name = 'articulo'

class VistaCrearArticulo(CreateView):
        model=Articulo
        template_name='nuevo_articulo.html'
        fields=(
             'titulo',
             'cuerpo',
              'genero',
              'categoria',
              'costo',
              'imagen'
        )
        success_url=reverse_lazy('lista_articulos')
        
        
        def form_valid(self, form): 
            form.instance.autor = self.request.user
            return super().form_valid(form)
        
    
class ComentarioGet(DetailView):
     model=Articulo
     template_name='detalle_articulo.html'
     def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=FormularioComentario
        return context



class ComentarioPost(SingleObjectMixin,FormView,View):
    model=Articulo
    form_class = FormularioComentario
    template_name = 'detalle_articulo.html'

    def post(self,request,*args, **kwargs):
        self.Articulo=self.get_object()
        #form=self.get_form()
        return super().post(request,*args,**kwargs) 
    
    def form_valid(self,form):
        #comentario=self.form_get()
        comentario=form.save(commit=False)
        comentario.Articulo=self.Articulo
        comentario.save()
        return super().form_valid(form)

    def get_success_url(self):
        articulo=self.get_object()
        return reverse('detalle_articulo',kwargs={'pk':articulo.pk})   
