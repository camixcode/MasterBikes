# Generated by Django 3.2.13 on 2022-07-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_arriendo_abonousdvalorarriendo'),
    ]

    operations = [
        migrations.AddField(
            model_name='arriendo',
            name='estadoArriendo',
            field=models.CharField(max_length=50, null=True, verbose_name='Estado Arriendo'),
        ),
    ]