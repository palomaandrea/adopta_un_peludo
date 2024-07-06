from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

def __str__(self):
    return str(self.genero)

class Usuario(models.Model):
    usuario = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    activo = models.IntegerField()

def __str__(self):
    return str(self.nombre)+" "+str(self.apellido_paterno)

