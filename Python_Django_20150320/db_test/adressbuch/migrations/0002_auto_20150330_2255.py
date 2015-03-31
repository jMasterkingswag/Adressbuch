# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adressbuch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adress',
            name='contact',
        ),
        migrations.AlterField(
            model_name='adress',
            name='object_id',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
    ]
