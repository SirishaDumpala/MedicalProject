# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0044_auto_20150416_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='patient_vital_signs',
            field=models.OneToOneField(to='oneclickvitals.VitalSigns', default=1),
            preserve_default=True,
        ),
    ]
