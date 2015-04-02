# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0021_auto_20150401_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='social_habits',
            field=models.CharField(max_length=70, choices=[('smoking', 'Smoking'), ('alcohol', 'Alcohol'), ('exercise', 'Exercise'), ('street drugs', 'Street drugs')]),
            preserve_default=True,
        ),
    ]
