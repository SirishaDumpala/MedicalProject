# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oneclickvitals', '0046_diagnosis_diagnosis_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosis',
            name='patient_vital_signs',
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='patient',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
