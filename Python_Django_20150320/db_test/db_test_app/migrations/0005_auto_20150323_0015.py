# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0004_auto_20150323_0010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adress',
            options={'verbose_name_plural': 'Adresses'},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='residence',
        ),
    ]
