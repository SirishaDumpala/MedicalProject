# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0057_auto_20150419_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='contact_phone_number',
            field=models.CharField(null=True, max_length=13),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='pharmacy_phone_number',
            field=models.CharField(null=True, max_length=13),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='phone_number',
            field=models.CharField(null=True, max_length=13),
            preserve_default=True,
        ),
    ]
