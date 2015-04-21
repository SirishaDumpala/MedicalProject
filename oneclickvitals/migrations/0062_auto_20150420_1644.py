# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0061_auto_20150420_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='patient',
            new_name='user',
        ),
    ]
