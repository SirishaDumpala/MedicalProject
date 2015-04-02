# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0016_patientmedicalhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='allergies',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
