from core.views import CreateUser, Deslogeo, Logeando, SignIn, SignUp, modificarPerro
from core.views import FormularioModPerro
from core.views import añadirPerro
from core.views import nosotros
from core.views import contacto
from core.views import gato
from core.views import eliminarPerro

from django.contrib import admin
from django.urls import path, include
from core import views
from core.views import agregarPerro

urlpatterns = [
    path('', views.index, name='index'),
    path('perro/', views.perro, name='perro'),
    path('perro/agregarPerro', agregarPerro, name='agregarPerro'),
    path('perro/add', añadirPerro, name='añadirPerro'),

    path('perro/FormularioModPerro/<int:Nro_chip>/', FormularioModPerro, name='FormularioModPerro'),
    path('perro/mod/<int:Nro_chip>/', modificarPerro, name='modificarPerro'),

     path('perro/del/<int:Nro_chip>/', eliminarPerro, name='eliminarPerro'),


    path('perro/1', views.perro1, name='perro1'),

    path('gato/', gato, name='gato'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/', nosotros, name='nosotros'),
    
    #signin
    path('signin/', SignIn, name='SignIn'),
    path('signin/logeando/', Logeando, name='Logeando'),
    path('signin/deslogeando/', Deslogeo, name='Deslogeo'),

    path('signup/', SignUp, name='SignUp'),
     path('signup/createuser', CreateUser, name='CreateUser'),

]

""" ,
    path('perro/1', views.perro1, name='perro1'),
    path('perro/2', views.perro2, name='perro2'),
    path('perro/3', views.perro3, name='perro3'),
    path('perro/4', views.perro4, name='perro4'),
    path('perro/5', views.perro5, name='perro5'),


    path('gato/1', views.gato1, name='gato1'),
    path('gato/2', views.gato2, name='gato2'),
    path('gato/3', views.gato3, name='gato3'),
    path('gato/4', views.gato4, name='gato4'),
    path('gato/5', views.gato5, name='gato5'),

path('nosotros/', views.nosotros, name='nosotros'),


path('contacto/', views.contacto, name='contacto'),"""