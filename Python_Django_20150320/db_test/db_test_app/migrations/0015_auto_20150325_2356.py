# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0014_auto_20150325_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset_category',
            name='level',
            field=models.PositiveIntegerField(default=2, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset_category',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset_category',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset_category',
            name='tree_id',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
