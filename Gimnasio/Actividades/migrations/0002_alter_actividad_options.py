# Generated by Django 4.2.4 on 2023-11-08 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividad',
            options={'ordering': ['nombre']},
        ),
    ]