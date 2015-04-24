# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0049_auto_20150420_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='day_supply',
            new_name='days_supply',
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='patient',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='prescription',
            name='refills',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
