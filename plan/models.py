from django.db import models
from django.forms import ModelForm
import datetime

# Create your models here.
class Inversion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion =models.CharField(max_length=50)
    codigo = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now_add=True)
    def publicado(self):
        return self.pub_date.date() == datetime.date.today()
    publicado.short_description = 'Publicado hoy?'
    def __unicode__(self):
        return u'%s %s %s' % (self.codigo, self.nombre, self.descripcion)
    
class Linea_accion(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    def publicado(self):
        return self.pub_date.date() == datetime.date.today()
    def __unicode__(self):
        return u'%s' % (self.nombre)
    
class Inversion_lineas_accion(models.Model):
    inversion = models.ForeignKey(Inversion)
    lineas_accion = models.ForeignKey(Linea_accion)
    
    
class Vocero(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo_electronico = models.CharField(max_length=80)
    cedula_identidad = models.CharField(max_length=11)
    pub_date = models.DateTimeField(auto_now_add=True)
    def publicado(self):
        return self.pub_date.date() == datetime.date.today()
    def __unicode__(self):
        return u'%s %s %s %s' % (self.nombre, self.apellido, self.correo_electronico, self.cedula_identidad)

class Inversion_vocero(models.Model):
    vocero = models.ForeignKey(Vocero)
    plan = models.ForeignKey(Inversion)
    pub_date = models.DateTimeField(auto_now_add=True)
    def publicado(self):
        return self.pub_date.date() == datetime.date.today()
    
class InversionForm(ModelForm):
    class Meta:
        model = Inversion
        fields = ('codigo','nombre', 'descripcion')
        

    

