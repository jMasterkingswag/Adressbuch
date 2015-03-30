# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0006_remove_adress_residence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='contact',
            field=models.ForeignKey(to='db_test_app.Contact', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adress',
            name='street',
            field=models.ForeignKey(to='db_test_app.Street', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='street',
            name='residence',
            field=models.ForeignKey(to='db_test_app.Residence', null=True),
            preserve_default=True,
        ),
    ]
