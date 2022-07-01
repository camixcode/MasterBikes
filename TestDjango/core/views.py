from ast import Try
from distutils.command import clean
from email import message
from itertools import product
#from math import prod
from pyexpat.errors import messages
from re import U
from sqlite3 import DateFromTicks
from tokenize import Triple
from urllib import request
from warnings import catch_warnings
from xml.dom.minidom import Document
from xml.parsers.expat import model
import django
from django.shortcuts import redirect, render
from core.forms import RegistrarProducto, RegistrarUsuario , CustomerUserCreationForm, ModificarUsuario, CrearCuentaAdmin, Arriendo, Reparacion
from django.contrib.auth import authenticate, login
from core.Carrito import Carrito
from django.contrib import messages
from django.contrib.auth.models import User 
from .models import Producto, Usuario


# Create your views here.
def home(request):
    productos = Producto.objects.all()
    
    datos = {
        'productos': productos,
        "nombre": "diego araya"
    }  
    return render(request, 'core/home.html', datos)


def Producto1(request):
    productos =Producto.objects.all()
    datos = {
        'productos':productos
    }
    return render(request, 'core/Producto1.html', datos)  

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar_producto(producto)
    return redirect("Producto")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.eliminar(producto)
    return redirect("Producto")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.restar(producto)
    return redirect("Producto") 

def limpiar_carrito(request):
    carrito = Carrito(request)   
    carrito.limpiar()
    return redirect("Producto") 

def Arbusto(request):
    return render(request, 'core/Arbusto.html')

def P_Arriendo(request):
    return render(request, 'core/P_Arriendo.html')

def Servicios_M(request):
    return render(request, 'core/Servicios_M.html')

def P_Promociones(request):
    return render(request, 'core/P_Promociones.html')    

def Contacto(request):
    return render(request, 'core/Contacto.html')

def Categoria1(request):
    return render(request, 'core/Categoria1.html')

def F_Crear_Cuenta(request):

    return render(request, 'core/F_Crear_Cuenta.html')

def form_mod_usuario(request):
    return render(request, 'core/form_mod_usuario.html')

def Admin_E_Servicios(request):
    return render(request, 'core/Admin_E_Servicios.html')

def form_borrar_producto(request,id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    productos =Producto.objects.all()
    
    datos = {
        'productos':productos
    }
    return render(request, 'core/listado_producto.html',datos)

def form_borrar_usuario(request,id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    usuarios =User.objects.all()
    
    datos = {
        'usuarios':usuarios
    }
    return render(request, 'core/listado_usuario.html',datos)

def HistoricoCompra(request):
    return render(request, 'core/HistoricoCompra.html')

def index_home(request):
    return render(request, 'core/index_home.html')    

def index_homeOG(request):
    return render(request, 'core/index_homeOG.html')    

def InicioSesion1(request):
    return render(request, 'core/InicioSesion1.html')             

def listado_producto(request):
    productos =Producto.objects.all()
    datos = {
        'productos':productos
    }
    return render(request, 'core/listado_producto.html',datos) 

def listado_usuario(request):
    usuarios =User.objects.all()
    datos = {
        'usuarios': usuarios
    }
    return render(request, 'core/listado_usuario.html',datos)   

def Macetero(request):
    return render(request, 'core/Macetero.html')    

def Nosotros(request):
    return render(request, 'core/Nosotros.html')                

def Paypal(request):
    return render(request, 'core/Paypal.html')   

def PerfilProducto(request,id):
    datos ={
        'producto' : Producto.objects.get(idProducto= id)
    }
    
    return render(request, 'core/PerfilProducto.html',datos)      

def Seguimiento(request):
    return render(request, 'core/Seguimiento.html')      

def Tierra(request):
    return render(request, 'core/Tierra.html')     

def form_usuario(request):
    datos = {
        'form': CrearCuentaAdmin()
    }

    if request.method == 'POST':
        formmulario = CrearCuentaAdmin(request.POST)
        if formmulario.is_valid:
            formmulario.save()
            datos['mensaje'] = "Guardados Correctamente"

    return render(request, 'core/form_usuario.html',datos)          

def form_producto(request):
    datos = {
        'form': RegistrarProducto()
    }
    if request.method == 'POST':

        formmulario = RegistrarProducto(request.POST , request.FILES)

        if formmulario.is_valid():
            formmulario.save()
            datos['mensaje'] = "Guardados Correctamente"
    return render(request, 'core/form_producto.html',datos)                          


def F_Crear_Cuenta(request):
    datos = {
        'form': RegistrarUsuario()
    }

    if request.method == 'POST':

        formmulario = RegistrarUsuario(request.POST)

        if formmulario.is_valid:
            formmulario.save()
            datos['mensaje'] = "Guardados Correctamente"

    return render(request, 'core/F_Crear_Cuenta.html',datos)

def form_mod_usuario(request,id):
    usuario =User.objects.get(id = id)
    datos={
        'form': ModificarUsuario(instance=usuario)
    }
    if request.method == 'POST':
        formulario = ModificarUsuario(data=request.POST, instance= usuario)
        if formulario.is_valid:
            formulario.save()
            datos={
        'form': ModificarUsuario(instance=usuario),
        'mensaje' : "Usuario Modificado corrctamente"
            }

    return render(request, 'core/form_mod_usuario.html',datos)

def form_mod_producto(request,id):
    producto =Producto.objects.get(idProducto = id)
    datos={
        'form': RegistrarProducto(instance=producto)
    }
    if request.method == 'POST':
        formulario = RegistrarProducto(data=request.POST,files=request.FILES, instance= producto)
        if formulario.is_valid():
            formulario.save()
            datos={
                'form': RegistrarProducto(instance=producto),
                'mensaje' : "Modificado corretamente"
                }

    return render(request, 'core/form_mod_producto.html',datos)


def registro (request):
    data ={
        'form':CustomerUserCreationForm
    }
    if request.method =='POST':
        formulario = CustomerUserCreationForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="index_home")
        data["form"] = formulario
    return render(request, 'registration/registro.html',data)

#def NavBar(request):
 #   return render(request, 'core/NavBar.html')  
     
def form_arriendo(request):
    datos = {
        'form': Arriendo()
    }
    if request.method == 'POST':

        formmulario = Arriendo(request.POST,files=request.FILES)

        if formmulario.is_valid():
            formmulario.save()
            datos['mensaje'] = "Arriendo registrado correctamente"
        else:
            datos['form'] = formmulario
    return render(request, 'core/form_arriendo.html',datos)    
                          

def form_reparacion(request):
    datos = {
        'form': Reparacion
    }
    
    return render(request, 'core/form_reparacion.html',datos)