
from dataclasses import fields
from pyexpat import model
from re import M
from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms
from django.forms import ModelForm
from .models import Producto, Usuario, Arriendo, Reparacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegistrarUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields =['idUsuario','nombres','apellidos','nombreUsuario','contrasena']

class RegistrarProducto(ModelForm):

    class Meta:
        model = Producto
        fields =['idProducto','nombreProducto','descripcionProducto','precioProducto','imagen','categoria','stock']

    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data


class CustomerUserCreationForm (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","password1","password2"]

class ModificarUsuario (ModelForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email"]

class CrearCuentaAdmin (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","is_superuser","password1","password2"]
 

class Arriendo(ModelForm):  
    class Meta:
        
        model = Arriendo
        fields =[
            'tipoArriendo',
            'tipoBicicleta',
            'fechaRetiro',
            'valorArriendo',
            'cantidad',
            'nombreArrendatario',
            'rutArrendatario',
            'mailArrendatario'
            ]           
        widgets={
                'fechaRetiro': forms.SelectDateWidget() 
            }


class Reparacion(ModelForm):
    class Meta:
        model = Reparacion
        fields =[
            'tipoReparacion',
            'detalleReparacion',
            'fechaReparacion',
            'valorReparacion'
            ]
        widgets={
                'fechaReparacion': forms.SelectDateWidget() 
            }    