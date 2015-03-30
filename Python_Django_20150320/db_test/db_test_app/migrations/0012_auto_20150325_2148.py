# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0011_auto_20150325_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset_category',
            name='parent_category',
            field=models.ForeignKey(to='db_test_app.Asset_Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='date_acquired',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='date_sold',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='next_sched_maint',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
    ]
