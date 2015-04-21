# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0050_remove_userdetail_pharmacy_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emergencycontact',
            name='contact_address',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='contact_city',
        ),
    ]
