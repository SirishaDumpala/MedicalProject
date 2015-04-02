# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0023_auto_20150401_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='chief_complaint',
            field=models.TextField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='current_medications',
            field=models.TextField(max_length=100),
            preserve_default=True,
        ),
    ]
