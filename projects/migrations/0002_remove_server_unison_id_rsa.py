# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-18 14:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='unison_id_rsa',
        ),
    ]
