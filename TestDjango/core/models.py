from ast import Delete
from asyncio.windows_events import NULL
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria
   

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='Id de producto')
    nombreProducto = models.CharField(max_length=50,verbose_name='Nombre del producto')
    descripcionProducto = models.CharField(max_length=50,verbose_name='Descripcion del producto')
    precioProducto = models.IntegerField(verbose_name='Precio del producto')
    imagen = models.ImageField ( upload_to= 'producto', null= True, default=None)
    categoria = models.CharField(max_length=50,verbose_name='categoria')
    stock= models.IntegerField(null= True,default=None,verbose_name='Stock')

    def __str__(self):
        return self.nombreProducto

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name='Id de usuario')
    nombreUsuario = models.CharField(max_length=50,verbose_name='Nombre de usuario')
    nombres = models.CharField(max_length=50,verbose_name='Nombres')
    apellidos = models.CharField(max_length=50,verbose_name='apellidos')
    contrasena = models.CharField(max_length=50, verbose_name='contrasena')
    def __str__(self):
        return self.nombreUsuario

class TypeTipoArriendo(models.Model):
    idTipoArriendo=models.AutoField(primary_key=True,verbose_name='Id tipo arriendo')
    descripTipoArriendo=models.CharField(max_length=100,verbose_name='Descripcion tipo arriendo')

    def __str__(self):
        return self.descripTipoArriendo

class TypeTipoBicicleta(models.Model):
    idTipoBicicleta=models.AutoField(primary_key=True,verbose_name='Id tipo bicicleta')
    descripTipoBicicleta=models.CharField(max_length=100,verbose_name='Descripcion tipo bicicleta')
    

    def __str__(self):
        return self.descripTipoBicicleta        

class Arriendo(models.Model):
    idArriendo=models.AutoField(primary_key=True, verbose_name='Id arriendo')
    tipoArriendo=models.CharField(max_length=200,verbose_name='Tipo arriendo')
    tipoBicicleta=models.CharField(max_length=200,verbose_name='Tipo bicicleta')
    fechaRetiro=models.DateField(verbose_name='Fecha retiro')
    fechaEntrega=models.DateField(null= True,default=None,verbose_name='Fecha entrega')
    abonoUSD=models.IntegerField(verbose_name='Abono USD')
    abonoUSDvalorArriendo=models.IntegerField(verbose_name='AbonoUSD valor arriendo')
    valorArriendo=models.IntegerField(verbose_name='Valor USD')
    cantidad=models.IntegerField(verbose_name='Cantidad')
    nombreArrendatario=models.CharField(max_length=200,verbose_name='Nombre arrendatario')
    rutArrendatario=models.CharField(max_length=50,verbose_name='Rut arrendatario')
    mailArrendatario=models.CharField(max_length=150,verbose_name='Mail arrendatario')

    def __str__(self):
        return self.idArriendo

class TypeReparaciones(models.Model):
    idTipoReparacion=models.AutoField(primary_key=True,verbose_name='Id tipo reparacion')
    descripReparacion=models.CharField(max_length=100,verbose_name='Descripcion reparacion')

    def __str__(self):
        return self.descripReparacion        

        
class Reparacion(models.Model):
    idReparacion=models.AutoField(primary_key=True, verbose_name='Id reparacion')
    fechaReparacion=models.DateField(verbose_name='Fecha reparacion')
    tipoReparacion=models.CharField(max_length=200,verbose_name='Tipo reparacion')
    detalleReparacion=models.TextField(max_length=500,verbose_name='Detalle reparacion')
    valorReparacion=models.IntegerField(verbose_name='Valor reparacion')
    estado=models.CharField(max_length=50,null= True,default=None,verbose_name='Estado')
    fechaEstado=models.DateField(null= True,default=None,verbose_name='Fecha actualizacion estado')

    def __str__(self):
        return self.idReparacion


class Promociones(models.Model):
    idPromocion=models.AutoField(primary_key=True,verbose_name='Id promocion')
    descuento=models.IntegerField(verbose_name='descuento')

    def __str__(self):
        return str(self.descuento)


class BiciletaArriendo(models.Model):
    idBicileta = models.AutoField(primary_key=True, verbose_name='Id de bicicleta')
    nombreBicileta = models.CharField(max_length=50,verbose_name='Nombre del bicicleta')
    descripcionBicileta = models.CharField(max_length=50,verbose_name='Descripcion de bicicleta')
    precioProducto = models.IntegerField(verbose_name='Precio de bicicleta')
    imagen = models.ImageField ( upload_to= 'producto', null= True, default=None)
    stock= models.IntegerField(null= True,default=None,verbose_name='Stock')

    def __str__(self):
        return self.nombreBicileta
