# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0052_auto_20150418_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='date_of_birth',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
