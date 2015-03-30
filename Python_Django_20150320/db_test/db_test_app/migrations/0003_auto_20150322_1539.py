# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0002_auto_20150322_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residence',
            name='name_adding',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
