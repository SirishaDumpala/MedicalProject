# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0028_auto_20150402_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(null=True, max_length=10),
            preserve_default=True,
        ),
    ]
