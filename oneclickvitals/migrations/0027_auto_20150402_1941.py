# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0026_auto_20150402_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='allergies',
            field=models.TextField(max_length=100),
            preserve_default=True,
        ),
    ]
