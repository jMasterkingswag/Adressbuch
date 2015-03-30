# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0010_auto_20150325_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset_category',
            options={'verbose_name': 'Asset Category', 'verbose_name_plural': 'Asset Categories'},
        ),
        migrations.RenameField(
            model_name='asset_state',
            old_name='asset_name',
            new_name='state_name',
        ),
    ]
