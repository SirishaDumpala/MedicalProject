# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0052_auto_20150423_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetail',
            name='dea',
            field=models.CharField(max_length=8, default='83059667'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='doctor_first_name',
            field=models.CharField(max_length=50, default='Victor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='doctor_last_name',
            field=models.CharField(max_length=50, default='Vitals'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='name_suffix',
            field=models.CharField(max_length=10, default='M.D.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='prescription_network_id',
            field=models.CharField(max_length=13, default='8841038281943'),
            preserve_default=True,
        ),
    ]
