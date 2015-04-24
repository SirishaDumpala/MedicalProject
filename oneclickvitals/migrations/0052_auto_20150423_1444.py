# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0051_auto_20150422_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordetail',
            name='license_number',
            field=models.CharField(max_length=8, default='A8039V92'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vitalsigns',
            name='notes',
            field=models.TextField(max_length=500, blank=True, null=True),
            preserve_default=True,
        ),
    ]
