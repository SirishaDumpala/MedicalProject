# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0051_auto_20150418_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='contact_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='pharmacy_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(null=True, max_length=50),
            preserve_default=True,
        ),
    ]
