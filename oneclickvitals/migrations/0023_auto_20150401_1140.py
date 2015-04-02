# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0022_auto_20150401_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='social_habits',
            field=models.CharField(choices=[('smoking', 'Smoking'), ('alcohol', 'Alcohol'), ('exercise', 'Exercise'), ('street drugs', 'Street drugs')], max_length=50),
            preserve_default=True,
        ),
    ]
