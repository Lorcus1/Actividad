from core.models import Perro,Raza
from django.shortcuts import render,redirect

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
    Nro_chip = request.POST.get('nro_chip','')
    Nombre_Perro = request.POST.get('nombre','')
    Edad_Perro = request.POST.get('edad','')
    id_raza = request.POST.get('Raza','')
    Sexo = request.POST.get('Sexo','')
    Adapt = request.POST.get('Adapt','')
    C_ninos = request.POST.get('c_ninos','')
    C_perros = request.POST.get('c_perros','')
    C_gatos = request.POST.get('c_gatos','')
    Energia = request.POST.get('energia','')
    Esteril = request.POST.get('Esteril','')
    imagen = request.FILES.get('imagen','')

    raza= Raza.objects.get(id=id_raza)

    perro = Perro(Nro_chip=Nro_chip,Nombre_Perro=Nombre_Perro,Edad_Perro=Edad_Perro,Raza=raza, Sexo=Sexo,Adapt=Adapt,C_ninos=C_ninos,C_perros=C_perros,C_gatos=C_gatos,Energia=Energia,Esteril=Esteril,imagen=imagen)
    perro.save()

    return redirect('perro')

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