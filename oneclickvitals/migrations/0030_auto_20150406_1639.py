# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0029_auto_20150406_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='pharmacy_address',
            field=models.CharField(null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='pharmacy_name',
            field=models.CharField(null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='pharmacy_phone_number',
            field=models.CharField(null=True, max_length=10),
            preserve_default=True,
        ),
    ]
