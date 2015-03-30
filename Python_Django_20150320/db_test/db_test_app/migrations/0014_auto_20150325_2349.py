# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0013_auto_20150325_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_category',
            name='parent_category',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='db_test_app.Asset_Category', null=True),
            preserve_default=True,
        ),
    ]
