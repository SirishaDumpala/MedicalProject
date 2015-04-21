# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0059_auto_20150420_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='refills',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
