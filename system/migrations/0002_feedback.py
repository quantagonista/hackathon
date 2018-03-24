# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Message')),
            ],
        ),
    ]
