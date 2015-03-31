# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0011_auto_20150330_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
