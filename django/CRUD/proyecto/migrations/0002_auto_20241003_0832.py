# Generated by Django 3.2.8 on 2024-10-03 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(max_length=100, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.TextField(max_length=100, verbose_name='Nombre'),
        ),

    ]
