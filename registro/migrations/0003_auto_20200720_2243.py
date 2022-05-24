# Generated by Django 3.0.3 on 2020-07-21 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20200715_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registro.Cargo'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registro.Persona'),
        ),
    ]
