# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-07-20 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shellbook', '0003_auto_20160720_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_info',
            name='bookid',
        ),
    ]
