# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0034_auto_20150413_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymedicalhistory',
            name='bleeding_tendency',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='familymedicalhistory',
            name='diabetes',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='familymedicalhistory',
            name='heart_attack',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='familymedicalhistory',
            name='heart_failure',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='familymedicalhistory',
            name='high_bp',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='familymedicalhistory',
            name='kidney_disease',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='familymedicalhistory',
            name='leukemia',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='familymedicalhistory',
            name='rheumatic_heart',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='familymedicalhistory',
            name='tuberculosis',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='familymedicalhistory',
            name='cancer',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='familymedicalhistory',
            name='stroke',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
