# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0033_familymedicalhistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familymedicalhistory',
            old_name='storke',
            new_name='stroke',
        ),
    ]
