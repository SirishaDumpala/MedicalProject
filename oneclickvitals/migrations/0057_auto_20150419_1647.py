# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0056_auto_20150419_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(null=True, max_length=13),
            preserve_default=True,
        ),
    ]
