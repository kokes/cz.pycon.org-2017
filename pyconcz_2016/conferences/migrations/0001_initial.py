# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-16 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('edition', models.CharField(max_length=50)),
                ('date_started', models.DateField()),
                ('date_ended', models.DateField()),
            ],
            options={
                'ordering': ['date_started'],
            },
        ),
    ]