# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0031_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='relationship',
            field=models.CharField(null=True, choices=[('spouse', 'Spouse'), ('parent', 'Parent'), ('brother', 'Brother'), ('sister', 'Sister'), ('boyfriend', 'Boyfriend'), ('girlfriend', 'Girlfriend'), ('other', 'Other')], max_length=50),
            preserve_default=True,
        ),
    ]
