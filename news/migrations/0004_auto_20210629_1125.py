# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-06-29 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.tags'),
        ),
    ]
