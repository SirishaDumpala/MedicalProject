# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0047_auto_20150418_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='city',
        ),
    ]
