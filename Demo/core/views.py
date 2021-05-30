from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def perro(request):
    return render(request, 'perro.html',{})
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