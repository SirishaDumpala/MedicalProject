# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0024_auto_20150427_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
