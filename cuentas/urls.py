# cuentas/urls.py
from django.urls import path
from .views import VistaRegistro
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('registration/signup',VistaRegistro.as_view(), name='signup'),

  #  path('login/',VistaRegistro.as_view(), name='signup'),
 #  path('login/',TemplateView.as_view(template_name="registration/loginLocal.html")),
   
]
