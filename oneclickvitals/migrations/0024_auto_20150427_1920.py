# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0023_auto_20150427_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labresults',
            name='test_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='labtest',
            name='test_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
