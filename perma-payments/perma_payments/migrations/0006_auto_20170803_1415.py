# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perma_payments', '0005_auto_20170802_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionagreement',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Aborted', 'Aborted'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Current', 'Current'), ('Hold', 'Hold'), ('Superseded', 'Superseded')], max_length=20),
        ),
    ]