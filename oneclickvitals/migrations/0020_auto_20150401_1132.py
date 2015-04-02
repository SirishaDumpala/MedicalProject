# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0019_auto_20150401_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='relationship',
            field=models.CharField(max_length=50, choices=[('parent', 'Parent'), ('brother', 'Brother')]),
            preserve_default=True,
        ),
    ]
