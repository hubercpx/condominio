# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-07 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcondominio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='residente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appcondominio.Residente'),
            preserve_default=False,
        ),
    ]
