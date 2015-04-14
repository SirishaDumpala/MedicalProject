# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0032_auto_20150410_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiology',
            name='created_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radiology',
            name='title',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
