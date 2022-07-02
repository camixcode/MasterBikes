# Generated by Django 4.0.4 on 2022-07-02 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arriendo',
            fields=[
                ('idArriendo', models.AutoField(primary_key=True, serialize=False, verbose_name='Id arriendo')),
                ('tipoArriendo', models.CharField(max_length=200, verbose_name='Tipo arriendo')),
                ('tipoBicicleta', models.CharField(max_length=200, verbose_name='Tipo bicicleta')),
                ('fechaRetiro', models.DateField(verbose_name='Fecha retiro')),
                ('fechaEntrega', models.DateField(default=None, null=True, verbose_name='Fecha entrega')),
                ('abonoUSD', models.IntegerField(verbose_name='Abono USD')),
                ('abonoUSDvalorArriendo', models.IntegerField(verbose_name='AbonoUSD valor arriendo')),
                ('valorArriendo', models.IntegerField(verbose_name='Valor USD')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('nombreArrendatario', models.CharField(max_length=200, verbose_name='Nombre arrendatario')),
                ('rutArrendatario', models.CharField(max_length=50, verbose_name='Rut arrendatario')),
                ('mailArrendatario', models.CharField(max_length=150, verbose_name='Mail arrendatario')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de producto')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='Nombre del producto')),
                ('descripcionProducto', models.CharField(max_length=50, verbose_name='Descripcion del producto')),
                ('precioProducto', models.IntegerField(verbose_name='Precio del producto')),
                ('imagen', models.ImageField(default=None, null=True, upload_to='producto')),
                ('categoria', models.CharField(max_length=50, verbose_name='categoria')),
                ('stock', models.IntegerField(default=None, null=True, verbose_name='Stock')),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('idReparacion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id reparacion')),
                ('fechaReparacion', models.DateField(verbose_name='Fecha reparacion')),
                ('tipoReparacion', models.CharField(max_length=200, verbose_name='Tipo reparacion')),
                ('detalleReparacion', models.TextField(max_length=500, verbose_name='Detalle reparacion')),
                ('valorReparacion', models.IntegerField(verbose_name='Valor reparacion')),
                ('estado', models.CharField(default=None, max_length=50, null=True, verbose_name='Estado')),
                ('fechaEstado', models.DateField(default=None, null=True, verbose_name='Fecha actualizacion estado')),
            ],
        ),
        migrations.CreateModel(
            name='TypeReparaciones',
            fields=[
                ('idTipoReparacion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id tipo reparacion')),
                ('descripReparacion', models.CharField(max_length=100, verbose_name='Descripcion reparacion')),
            ],
        ),
        migrations.CreateModel(
            name='TypeTipoArriendo',
            fields=[
                ('idTipoArriendo', models.AutoField(primary_key=True, serialize=False, verbose_name='Id tipo arriendo')),
                ('descripTipoArriendo', models.CharField(max_length=100, verbose_name='Descripcion tipo arriendo')),
            ],
        ),
        migrations.CreateModel(
            name='TypeTipoBicicleta',
            fields=[
                ('idTipoBicicleta', models.AutoField(primary_key=True, serialize=False, verbose_name='Id tipo bicicleta')),
                ('descripTipoBicicleta', models.CharField(max_length=100, verbose_name='Descripcion tipo bicicleta')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de usuario')),
                ('nombreUsuario', models.CharField(max_length=50, verbose_name='Nombre de usuario')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos')),
                ('contrasena', models.CharField(max_length=50, verbose_name='contrasena')),
            ],
        ),
    ]
