# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0037_doctordetail_pharmacydetail_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], null=True, max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='doctor_address',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='doctor_city',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='day_supply',
            field=models.CharField(blank=True, null=True, max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='dosage_form',
            field=models.CharField(blank=True, null=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='drug_name',
            field=models.CharField(blank=True, null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='drug_strength',
            field=models.CharField(blank=True, null=True, max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='quantity',
            field=models.CharField(blank=True, null=True, max_length=6),
            preserve_default=True,
        ),
    ]
