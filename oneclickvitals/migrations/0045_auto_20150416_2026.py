# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0044_auto_20150416_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True),
            preserve_default=True,
        ),
    ]
