# Generated by Django 3.0.3 on 2020-07-15 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('hora_registro', models.DateTimeField(auto_now_add=True)),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Persona')),
            ],
        ),
    ]