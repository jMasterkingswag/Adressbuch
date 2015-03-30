# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0005_auto_20150323_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adress',
            name='residence',
        ),
    ]
