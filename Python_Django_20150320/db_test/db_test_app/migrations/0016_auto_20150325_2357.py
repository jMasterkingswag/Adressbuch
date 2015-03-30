# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0015_auto_20150325_2356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset_category',
            old_name='parent_category',
            new_name='parent',
        ),
    ]
