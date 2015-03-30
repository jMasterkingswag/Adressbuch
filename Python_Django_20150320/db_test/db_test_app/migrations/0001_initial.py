# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('second_name', models.CharField(max_length=128, blank=True)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('birth_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
