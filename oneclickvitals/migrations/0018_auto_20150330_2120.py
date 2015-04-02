# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0017_auto_20150330_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='allergies',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]
