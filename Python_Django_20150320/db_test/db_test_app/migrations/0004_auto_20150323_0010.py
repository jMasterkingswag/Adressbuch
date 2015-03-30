# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0003_auto_20150322_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_number', models.IntegerField()),
                ('contact', models.ForeignKey(to='db_test_app.Contact')),
                ('residence', models.ForeignKey(to='db_test_app.Residence')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_name', models.CharField(max_length=128)),
                ('residence', models.ForeignKey(to='db_test_app.Residence')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='adress',
            name='street',
            field=models.ForeignKey(to='db_test_app.Street'),
            preserve_default=True,
        ),
    ]
