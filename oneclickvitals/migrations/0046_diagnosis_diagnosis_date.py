# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0045_auto_20150416_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='diagnosis_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
