# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-14 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0002_auto_20181115_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketapp.Place')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketapp.Room')),
            ],
        ),
    ]