# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0047_auto_20150417_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='relationship',
            field=models.CharField(null=True, max_length=50, choices=[('Spouse', 'spouse'), ('Parent', 'parent'), ('Brother', 'brother'), ('Sister', 'sister'), ('Boyfriend', 'boyfriend'), ('Girlfriend', 'girlfriend'), ('Other', 'other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='social_habits',
            field=models.CharField(max_length=50, choices=[('Smoking', 'smoking'), ('Alcohol', 'alcohol'), ('Exercise', 'exercise'), ('Street drugs', 'street drugs'), ('Other', 'other'), ('None', 'none')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='frequency',
            field=models.CharField(max_length=50, choices=[('Daily', 'daily'), ('Every Other Day', 'every other day'), ('Twice a Day', 'BID/b.i.d.'), ('Three Times a Day', 'TID/t.id'), ('Four Times a Day', 'QID/q.i.d.'), ('Every Bedtime', 'QHS'), ('Every 4 Hours', 'Q4h'), ('Every 4 to 6 Hours', 'Q4-6h'), ('Every Week', 'QWK')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='gender',
            field=models.CharField(null=True, max_length=10, choices=[('Male', 'male'), ('Female', 'female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='refills',
            field=models.CharField(max_length=5, choices=[('Yes', 'yes'), ('No', 'no')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='gender',
            field=models.CharField(null=True, max_length=50, choices=[('Female', 'female'), ('Male', 'male')]),
            preserve_default=True,
        ),
    ]
