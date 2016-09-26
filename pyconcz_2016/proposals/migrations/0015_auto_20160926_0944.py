# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-09-26 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0014_auto_20160919_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialaid',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talk',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workshop',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
