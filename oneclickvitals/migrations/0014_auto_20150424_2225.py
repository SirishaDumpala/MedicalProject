# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0013_remove_diagnosis_lab_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='contact_phone_number',
            field=models.CharField(null=True, max_length=14),
            preserve_default=True,
        ),
    ]
