# Generated by Django 4.2.4 on 2023-12-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='asistencia',
            field=models.CharField(default='Presente', max_length=30),
        ),
    ]
