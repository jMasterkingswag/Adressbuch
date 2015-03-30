# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0009_auto_20150325_1603'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset_category',
            options={'verbose_name_plural': 'Asset Categories'},
        ),
        migrations.RemoveField(
            model_name='asset_category',
            name='parent_category',
        ),
    ]
