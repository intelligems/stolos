# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-03 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_server_unison_id_rsa'),
    ]

    operations = [
        migrations.AddField(
            model_name='stack',
            name='description',
            field=models.CharField(default='', editable=False, max_length=140),
        ),
    ]
