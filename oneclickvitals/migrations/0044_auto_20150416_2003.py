# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0043_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmedicalhistory',
            name='blood_type',
            field=models.CharField(null=True, max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patientmedicalhistory',
            name='height',
            field=models.PositiveIntegerField(null=True, max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patientmedicalhistory',
            name='weight',
            field=models.FloatField(null=True, max_length=10),
            preserve_default=True,
        ),
    ]
