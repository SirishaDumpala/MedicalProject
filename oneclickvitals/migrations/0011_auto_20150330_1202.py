# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0010_auto_20150317_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='insurance',
            field=models.CharField(null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
