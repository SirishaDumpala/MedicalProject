# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0015_auto_20150424_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsigns',
            name='blood_pressure',
            field=models.CharField(max_length=6),
            preserve_default=True,
        ),
    ]
