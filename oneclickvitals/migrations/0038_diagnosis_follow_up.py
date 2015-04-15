# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0037_auto_20150414_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='follow_up',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
