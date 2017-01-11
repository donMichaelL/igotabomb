# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bombs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bomb',
            name='location',
        ),
        migrations.AlterField(
            model_name='bomb',
            name='brange',
            field=models.IntegerField(help_text='in kms'),
        ),
    ]