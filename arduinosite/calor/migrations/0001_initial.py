# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemperaturaTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='Fecha')),
                ('temperatura', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Temperatura')),
            ],
        ),
    ]