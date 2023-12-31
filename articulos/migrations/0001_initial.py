# Generated by Django 4.2 on 2023-12-11 19:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('genero', models.CharField(blank=True, max_length=20)),
                ('categoria', models.CharField(max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('costo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=140)),
                ('Articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.articulo')),
            ],
        ),
    ]
