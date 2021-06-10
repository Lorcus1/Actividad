from django.db import models
from django.contrib.auth.models import User

class Raza(models.Model):
    id      = models.AutoField(primary_key=True)
    Raza        = models.CharField(max_length=99)
    Descripcion = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.Raza 


class Perro (models.Model):
    Nro_chip=models.IntegerField(primary_key=True)
    Nombre_Perro= models.CharField(max_length=99)
    Edad_Perro = models.IntegerField(null=True)
    Raza     = models.ForeignKey(Raza, on_delete=models.CASCADE)
    Sexo     = models.CharField(max_length=99)
    Adapt    = models.CharField(max_length=2)
    C_ninos  = models.CharField(max_length=2)
    C_perros = models.CharField(max_length=2)
    C_gatos  = models.CharField(max_length=2)
    Energia  = models.CharField(max_length=8)
    Esteril  = models.CharField(max_length=2)

    def ruta_imagen(self, filename):
            return f'perros/{self.Nro_chip}/{filename}'

    imagen = models.ImageField(upload_to = ruta_imagen, max_length = 9999, null = True, blank = True)

    def __str__(self):
        return self.Nombre_Perro + ' (' + str(self.Nro_chip) + ' )'

class Cuenta(models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE) 
    def __str__(self):
        return str(self.Usuario)