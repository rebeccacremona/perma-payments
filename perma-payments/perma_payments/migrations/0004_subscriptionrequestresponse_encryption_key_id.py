# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perma_payments', '0003_subscriptionrequestresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionrequestresponse',
            name='encryption_key_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]