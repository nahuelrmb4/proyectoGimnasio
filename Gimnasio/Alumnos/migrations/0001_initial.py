# Generated by Django 4.2.4 on 2023-11-08 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('edad', models.PositiveIntegerField()),
                ('dni', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['apellido'],
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emision', models.DateField(auto_now_add=True)),
                ('vencimiento', models.DateField()),
                ('pago', models.DateField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Alumnos.alumno')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Alumnos.plan'),
        ),
    ]