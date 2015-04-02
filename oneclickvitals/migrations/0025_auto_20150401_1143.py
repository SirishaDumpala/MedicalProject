# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0024_auto_20150401_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='allergies',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='chief_complaint',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='current_medications',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='medical_history',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='surgical_history',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
    ]
