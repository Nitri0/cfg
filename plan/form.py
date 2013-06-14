'''
Created on 12/06/2013

@author: edwin-ca
'''
from django import forms

class InversionForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=50)
    codigo = forms.CharField(max_length=20) 
    