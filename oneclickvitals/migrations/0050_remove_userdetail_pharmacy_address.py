# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0049_auto_20150418_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='pharmacy_address',
        ),
    ]
