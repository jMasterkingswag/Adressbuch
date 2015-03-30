# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0016_auto_20150325_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='date_acquired',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='date_sold',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='next_sched_maint',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
