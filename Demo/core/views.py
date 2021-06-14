from core.models import Perro,Raza
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def perro(request):
    perros = Perro.objects.all()
    contexto = {'perros': perros}
    return render(request, 'perro.html',contexto)
def perro1(request):
    return render(request, 'perro1.html',{})
def perro2(request):
    return render(request, 'perro2.html',{})
def perro3(request):
    return render(request, 'perro3.html',{})
def perro4(request):
    return render(request, 'perro4.html',{})
def perro5(request):
    return render(request, 'perro5.html',{})

def agregarPerro(request):
    razas = Raza.objects.all()
    contexto = {'razas': razas}
    return render(request, 'agregarPerro.html',contexto)

def añadirPerro(request):
    Nro_chip = request.POST.get('Nro_chip','')
    Nombre_Perro = request.POST.get('Nombre_Perro','')
    Edad_Perro = request.POST.get('Edad_Perro','')
    id_raza = request.POST.get('Raza','')
    Sexo = request.POST.get('Sexo','')
    Adapt = request.POST.get('Adapt','')
    C_ninos = request.POST.get('C_ninos','')
    C_perros = request.POST.get('C_perros','')
    C_gatos = request.POST.get('C_gatos','')
    Energia = request.POST.get('Energia','')
    Esteril = request.POST.get('Esteril','')
    imagen = request.FILES.get('imagen','')

    raza= Raza.objects.get(id=id_raza)

    perro = Perro(Nro_chip=Nro_chip,Nombre_Perro=Nombre_Perro,Edad_Perro=Edad_Perro,Raza=raza, Sexo=Sexo,Adapt=Adapt,C_ninos=C_ninos,C_perros=C_perros,C_gatos=C_gatos,Energia=Energia,Esteril=Esteril,imagen=imagen)
    perro.save()

    return redirect('perro')

def FormularioModPerro(request,Nro_chip): 
    perro =  Perro.objects.get(Nro_chip=Nro_chip)
    razas = Raza.objects.all()
    contexto = {'razas': razas, 'perro':perro}

    return render(request, 'modificarPerro.html',contexto)

def modificarPerro(request, Nro_chip):
    

    Nro_chip = request.POST.get('Nro_chip','')
    Nombre_Perro = request.POST.get('Nombre_Perro','')
    Edad_Perro = request.POST.get('Edad_Perro','')
    id_raza = request.POST.get('Raza','')
    Sexo = request.POST.get('Sexo','')
    Adapt = request.POST.get('Adapt','')
    C_ninos = request.POST.get('C_ninos','')
    C_perros = request.POST.get('C_perros','')
    C_gatos = request.POST.get('C_gatos','')
    Energia = request.POST.get('Energia','')
    Esteril = request.POST.get('Esteril','')
    imagen = request.FILES.get('imagen','')


    
    perro = Perro.objects.get(Nro_chip=Nro_chip)
    perro.Nombre_Perro= Nombre_Perro
    perro.Edad_Perro=Edad_Perro
    perro.id_raza=Raza
    perro.Sexo = Sexo
    perro.Adapt = Adapt
    perro.C_ninos = C_ninos
    perro.C_perros = C_perros
    perro.C_gatos = C_gatos
    perro.Energia = Energia
    perro.Esteril = Esteril
    print(imagen)
        
    if(imagen!=''):
        perro.imagen = imagen

    perro.save()

    return redirect('perro')


def eliminarPerro (request, Nro_chip):
    perro = Perro.objects.get(Nro_chip=Nro_chip)
    perro.delete()

    return redirect('perro')


def SignIn(request):
    contexto={}
    return render(request,'signin.html',contexto)

def Logeando(request):
    username = request.POST.get('usuario','default')
    password = request.POST.get('clave','default')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        
        return redirect('index')
    else:
        return redirect(SignIn)

def Deslogeo(request):
    logout(request)
    return redirect ('index')

def SignUp(request):
    contexto={}
    return render(request,'signup.html',contexto)

def CreateUser(request):
    contexto={}
    username = request.POST.get('usuario','default')
    email = request.POST.get('email','default')
    password = request.POST.get('clave','default')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return redirect('SignUp')
        messages.error(request, 'El usuario ya existe')
    else:
        user = User.objects.create_user(username, email, password)
        return redirect('index')
        user.save()


    return render(request,'signin.html')

def gato(request):
    return render(request, 'gato.html',{})
def gato1(request):
    return render(request, 'gato1.html',{})
def gato2(request):
    return render(request, 'gato2.html',{})
def gato3(request):
    return render(request, 'gato3.html',{})
def gato4(request):
    return render(request, 'gato4.html',{})
def gato5(request):
    return render(request, 'gato5.html',{})


def contacto(request):
    return render(request, 'contacto.html',{})

def nosotros(request):
    return render(request, 'nosotros.html',{})    