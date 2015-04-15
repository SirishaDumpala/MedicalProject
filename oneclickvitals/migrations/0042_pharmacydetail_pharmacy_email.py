# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0041_auto_20150414_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacydetail',
            name='pharmacy_email',
            field=models.EmailField(max_length=75, blank=True, null=True),
            preserve_default=True,
        ),
    ]
