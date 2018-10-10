# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saltstack', '0003_auto_20181009_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='permission',
        ),
        migrations.AddField(
            model_name='role',
            name='permission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saltstack.Permission'),
        ),
    ]
