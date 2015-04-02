# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0020_auto_20150401_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='relationship',
            field=models.CharField(choices=[('parent', 'Parent'), ('brother', 'Brother'), ('sister', 'Sister'), ('boyfriend', 'Boyfriend'), ('girlfriend', 'Girlfriend'), ('other', 'Other')], max_length=50),
            preserve_default=True,
        ),
    ]
