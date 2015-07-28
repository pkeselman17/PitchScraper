# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150723_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('description', models.CharField(max_length=300)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('sport', models.ForeignKey(to='app.Sport')),
            ],
            options={
                'db_table': 'game',
            },
        ),
    ]
