# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0046_auto_20150416_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='date_of_birth',
            field=models.CharField(null=True, choices=[('Year', (('1990', '1900'), ('1991', '1991'))), ('Month', (('january', 'January'), ('february', 'February'))), ('Day', (('1', '1'), ('2', '2')))], max_length=20),
            preserve_default=True,
        ),
    ]
