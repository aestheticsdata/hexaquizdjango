# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuizQuestions',
            new_name='QuizQuestion',
        ),
    ]
