# Generated by Django 4.1.3 on 2023-06-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0005_alter_entrega_calificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='calificacion',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
