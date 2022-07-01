# Generated by Django 3.2.13 on 2022-06-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_producto_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arriendo',
            fields=[
                ('idArriendo', models.AutoField(primary_key=True, serialize=False, verbose_name='Id arriendo')),
                ('tipoArriendo', models.CharField(max_length=50, verbose_name='Tipo arriendo')),
                ('tipoBicicleta', models.CharField(max_length=50, verbose_name='Tipo bicicleta')),
                ('fechaRetiro', models.DateField(verbose_name='Fecha retiro')),
                ('fechaEntrega', models.DateField(default=None, null=True, verbose_name='Fecha entrega')),
                ('abonoUSD', models.IntegerField(verbose_name='Abono USD')),
                ('valorArriendo', models.IntegerField(verbose_name='Valor USD')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('nombreArrendatario', models.CharField(max_length=200, verbose_name='Nombre arrendatario')),
                ('rutArrendatario', models.CharField(max_length=50, verbose_name='Rut arrendatario')),
                ('mailArrendatario', models.CharField(max_length=150, verbose_name='Mail arrendatario')),
            ],
        ),
    ]
