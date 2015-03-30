# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_test_app', '0007_auto_20150323_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor', models.CharField(max_length=128, blank=True)),
                ('department', models.CharField(max_length=128)),
                ('next_sched_maint', models.DateField()),
                ('description', models.CharField(max_length=256, blank=True)),
                ('date_acquired', models.DateField()),
                ('date_sold', models.DateField()),
                ('model_number', models.CharField(max_length=128, blank=True)),
                ('serial_number', models.CharField(max_length=128, blank=True)),
                ('barcode_number', models.CharField(max_length=128, blank=True)),
                ('purchase_price', models.CharField(max_length=128, blank=True)),
                ('current_value', models.CharField(max_length=128, blank=True)),
                ('total_maintenance', models.CharField(max_length=128, blank=True)),
                ('total_depreciation', models.CharField(max_length=128, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Asset_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256, blank=True)),
                ('parent_category', models.ForeignKey(to='db_test_app.Asset_Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Asset_State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_category',
            field=models.ForeignKey(to='db_test_app.Asset_Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.ForeignKey(to='db_test_app.Asset_State'),
            preserve_default=True,
        ),
    ]
