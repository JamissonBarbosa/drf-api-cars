# Generated by Django 5.1.4 on 2024-12-12 14:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Marca',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, verbose_name='Modelo')),
                ('factory_year', models.IntegerField(null=True, verbose_name='Ano de fabricação')),
                ('model_year', models.IntegerField(null=True, verbose_name='Ano do modelo')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cor')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.brand', verbose_name='Marca')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Proprietário')),
            ],
            options={
                'verbose_name': 'Carro',
                'ordering': ['model'],
            },
        ),
    ]