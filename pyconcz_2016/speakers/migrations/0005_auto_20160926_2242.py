# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-09-26 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_speaker_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='biography',
        ),
        migrations.AddField(
            model_name='speaker',
            name='bio',
            field=models.TextField(default='', help_text='Tell us a bit about yourself! Who you are, where are you from, what are your experiences with Python. Be wild, be creative!'),
            preserve_default=False,
        ),
    ]