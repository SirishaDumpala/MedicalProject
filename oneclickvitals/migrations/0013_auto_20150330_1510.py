# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0012_userdetail_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
