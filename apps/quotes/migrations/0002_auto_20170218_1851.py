# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-19 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.TextField(max_length=250),
        ),
    ]
