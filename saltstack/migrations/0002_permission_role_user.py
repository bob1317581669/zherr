# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saltstack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=12, unique=True, verbose_name='\u6807\u9898')),
                ('url', models.CharField(max_length=12, unique=True, verbose_name='\u542b\u6b63\u5219\u7684URL')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=12, unique=True, verbose_name='\u804c\u4f4d')),
                ('permission', models.ManyToManyField(blank=True, null=True, to='saltstack.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12, unique=True, verbose_name='\u7528\u6237\u540d')),
                ('passwrod', models.CharField(max_length=24, verbose_name='\u5bc6\u7801')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saltstack.Role', verbose_name='\u5bf9\u5e94\u7684\u804c\u4f4d')),
            ],
        ),
    ]
