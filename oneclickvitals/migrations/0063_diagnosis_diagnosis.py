# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0062_auto_20150420_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='diagnosis',
            field=models.TextField(null=True, max_length=500),
            preserve_default=True,
        ),
    ]
