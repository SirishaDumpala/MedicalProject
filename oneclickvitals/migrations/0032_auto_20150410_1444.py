# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0031_appointment_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiology',
            name='caption',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='radiology',
            name='image',
            field=models.ImageField(upload_to='image'),
            preserve_default=True,
        ),
    ]
