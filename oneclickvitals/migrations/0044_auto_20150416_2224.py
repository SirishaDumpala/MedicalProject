# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0043_auto_20150416_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsigns',
            name='blood_pressure',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vitalsigns',
            name='current_height',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vitalsigns',
            name='current_weight',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vitalsigns',
            name='heart_rate',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vitalsigns',
            name='temperature',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
    ]
